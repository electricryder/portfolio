# app.py
# CS50x Final Project (Flask + SQLite)
# Some parts of this project were developed with assistance from ChatGPT (OpenAI).
# All code was reviewed and adapted by the author.

import sqlite3
from datetime import date, timedelta

from flask import Flask, render_template, request, redirect, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash

from helpers import login_required, dues_required, admin_required, is_dues_ok

app = Flask(__name__)
app.secret_key = "change-me"

DATABASE = "association.db"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


# -------------------------
# DB
# -------------------------
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.before_request
def load_logged_in_user():
    g.user = None
    user_id = session.get("user_id")
    if user_id is None:
        return

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    db.close()

    if user:
        user_dict = dict(user)
        user_dict["dues_ok"] = is_dues_ok(user_dict["dues_paid_until"])
        g.user = user_dict


# -------------------------
# Formatting filters
# -------------------------
@app.template_filter("eur")
def eur_filter(cents):
    try:
        cents = int(cents)
    except Exception:
        cents = 0
    return f"€{cents/100:.2f}"


@app.template_filter("dt")
def dt_filter(value):
    """
    Datetime: DD/MM/YYYY hh:mmh
    Accepts: "YYYY-MM-DD HH:MM:SS" (SQLite) or similar.
    """
    if not value:
        return ""
    s = str(value)
    try:
        year = s[0:4]
        month = s[5:7]
        day = s[8:10]
        hour = s[11:13]
        minute = s[14:16]
        return f"{day}/{month}/{year} {hour}:{minute}h"
    except Exception:
        return s


@app.template_filter("d")
def d_filter(value):
    """
    Date only: DD/MM/YYYY
    Accepts: "YYYY-MM-DD"
    """
    if not value:
        return ""
    s = str(value)
    try:
        year = s[0:4]
        month = s[5:7]
        day = s[8:10]
        return f"{day}/{month}/{year}"
    except Exception:
        return s


# -------------------------
# PT parsing helpers
# -------------------------
def parse_date_ddmmyyyy(date_str):
    """
    Input: DD/MM/YYYY
    Output: YYYY-MM-DD
    """
    if not date_str:
        raise ValueError("Missing date")

    s = date_str.strip()
    if len(s) != 10 or s[2] != "/" or s[5] != "/":
        raise ValueError("Invalid date format")

    day = int(s[0:2])
    month = int(s[3:5])
    year = int(s[6:10])

    _ = date(year, month, day)
    return f"{year:04d}-{month:02d}-{day:02d}"


def parse_time_hhmm(time_str):
    """
    Input: HH:MM
    Output: HH:MM
    """
    if not time_str:
        raise ValueError("Missing time")

    s = time_str.strip()
    if len(s) != 5 or s[2] != ":":
        raise ValueError("Invalid time format")

    hh = int(s[0:2])
    mm = int(s[3:5])

    if hh < 0 or hh > 23 or mm < 0 or mm > 59:
        raise ValueError("Invalid time value")

    return f"{hh:02d}:{mm:02d}"


def sqlite_dt_from_pt(date_ddmmyyyy, time_hhmm):
    """
    Input: date DD/MM/YYYY + time HH:MM
    Output: YYYY-MM-DD HH:MM:00
    """
    iso_date = parse_date_ddmmyyyy(date_ddmmyyyy)
    iso_time = parse_time_hhmm(time_hhmm)
    return f"{iso_date} {iso_time}:00"


def pt_date_from_iso(iso_date):
    """
    Input: YYYY-MM-DD
    Output: DD/MM/YYYY
    """
    if not iso_date:
        return ""
    s = str(iso_date)
    try:
        year = s[0:4]
        month = s[5:7]
        day = s[8:10]
        return f"{day}/{month}/{year}"
    except Exception:
        return s


def pt_time_from_sqlite_dt(sqlite_dt):
    """
    Input: YYYY-MM-DD HH:MM:SS
    Output: HH:MM
    """
    if not sqlite_dt:
        return ""
    s = str(sqlite_dt)
    try:
        return s[11:16]
    except Exception:
        return ""


# -------------------------
# Routes
# -------------------------
@app.route("/")
def index():
    return redirect("/events")


# Events (public + admin mode)
@app.route("/events")
def events():
    db = get_db()

    upcoming = db.execute(
        """
        SELECT * FROM events
        WHERE starts_at >= datetime('now')
        ORDER BY starts_at ASC
        """
    ).fetchall()

    past = db.execute(
        """
        SELECT * FROM events
        WHERE starts_at < datetime('now')
        ORDER BY starts_at DESC
        """
    ).fetchall()

    db.close()
    return render_template("events.html", upcoming=upcoming, past=past)


@app.route("/events/<int:event_id>")
def event_detail(event_id):
    db = get_db()
    ev = db.execute(
        """
        SELECT *,
               (starts_at < datetime('now')) AS is_past
        FROM events
        WHERE id = ?
        """,
        (event_id,),
    ).fetchone()
    db.close()

    if ev is None:
        flash("Event not found.", "danger")
        return redirect("/events")

    return render_template("event.html", event=ev)


# Ticket checkout
@app.route("/events/<int:event_id>/checkout", methods=["GET", "POST"])
@login_required("You must log in to buy a ticket.")
@dues_required
def checkout(event_id):
    db = get_db()

    ev = db.execute(
        """
        SELECT *,
               (starts_at < datetime('now')) AS is_past
        FROM events
        WHERE id = ?
        """,
        (event_id,),
    ).fetchone()

    if ev is None:
        db.close()
        flash("Event not found.", "danger")
        return redirect("/events")

    if ev["is_past"]:
        db.close()
        flash("This event is in the past. Tickets are no longer available.", "warning")
        return redirect(f"/events/{event_id}")

    already = db.execute(
        "SELECT id FROM tickets WHERE user_id = ? AND event_id = ?",
        (g.user["id"], event_id),
    ).fetchone()

    if request.method == "GET":
        db.close()
        return render_template("checkout.html", event=ev, already_bought=(already is not None))

    if already is not None:
        db.close()
        flash("You already bought a ticket for this event.", "warning")
        return redirect("/tickets")

    db.execute(
        "INSERT INTO tickets (user_id, event_id, status) VALUES (?, ?, 'paid')",
        (g.user["id"], event_id),
    )
    db.commit()
    db.close()

    flash("Payment confirmed. Ticket created.", "success")
    return redirect("/tickets")


# Member login/logout
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        next_url = request.args.get("next", "")
        return render_template("login.html", next=next_url)

    next_url = request.form.get("next", "")

    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    db.close()

    if user is None or not check_password_hash(user["password_hash"], password):
        flash("Invalid email or password.", "danger")
        return redirect(f"/login?next={next_url}")

    session["user_id"] = user["id"]
    flash("Logged in.", "success")

    if next_url and next_url.startswith("/"):
        return redirect(next_url)

    return redirect("/member")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out.", "info")
    return redirect("/events")


# Member area
@app.route("/member")
@login_required()
def member():
    return render_template("member.html")


@app.route("/card")
@login_required()
@dues_required
def card():
    return render_template("card.html")


# -------------------------
# Change password (member)
# -------------------------
@app.route("/password", methods=["GET", "POST"])
@login_required()
def change_password():
    if request.method == "GET":
        return render_template("password.html")

    current_password = request.form.get("current_password", "")
    new_password = request.form.get("new_password", "")
    confirm_password = request.form.get("confirm_password", "")

    if not current_password or not new_password or not confirm_password:
        flash("All fields are required.", "danger")
        return redirect("/password")

    if new_password != confirm_password:
        flash("New password and confirmation do not match.", "danger")
        return redirect("/password")

    if len(new_password) < 6:
        flash("New password must be at least 6 characters long.", "danger")
        return redirect("/password")

    db = get_db()
    row = db.execute("SELECT password_hash FROM users WHERE id = ?", (g.user["id"],)).fetchone()
    if row is None:
        db.close()
        flash("User not found.", "danger")
        return redirect("/member")

    if not check_password_hash(row["password_hash"], current_password):
        db.close()
        flash("Current password is incorrect.", "danger")
        return redirect("/password")

    new_hash = generate_password_hash(new_password)
    db.execute("UPDATE users SET password_hash = ? WHERE id = ?", (new_hash, g.user["id"]))
    db.commit()
    db.close()

    flash("Password updated successfully.", "success")
    return redirect("/member")


# Dues payment (simulated)
@app.route("/dues", methods=["GET"])
@login_required()
def dues():
    return render_template("dues.html")


@app.route("/dues/checkout", methods=["POST"])
@login_required()
def dues_checkout():
    months_str = request.form.get("months", "12").strip()
    try:
        months = int(months_str)
    except ValueError:
        months = 12

    if months < 1:
        months = 1
    if months > 24:
        months = 24

    total_cents = months * 100
    return render_template("dues_checkout.html", months=months, total_cents=total_cents)


@app.route("/dues/pay", methods=["POST"])
@login_required()
def dues_pay():
    months_str = request.form.get("months", "12").strip()
    try:
        months = int(months_str)
    except ValueError:
        months = 12

    if months < 1:
        months = 1
    if months > 24:
        months = 24

    current_paid_until = g.user["dues_paid_until"]
    try:
        current_date = date.fromisoformat(current_paid_until)
    except ValueError:
        current_date = date(1970, 1, 1)

    start_date = max(date.today(), current_date)
    new_paid_until_date = start_date + timedelta(days=months * 30)
    new_paid_until_iso = new_paid_until_date.isoformat()

    db = get_db()
    db.execute(
        "UPDATE users SET dues_paid_until = ? WHERE id = ?",
        (new_paid_until_iso, g.user["id"]),
    )
    db.commit()
    db.close()

    flash(f"Payment confirmed. Dues extended by {months} month(s).", "success")
    return redirect("/member")


# Tickets list
@app.route("/tickets")
@login_required()
@dues_required
def tickets():
    db = get_db()
    rows = db.execute(
        """
        SELECT tickets.id, tickets.status, tickets.created_at,
               events.title, events.starts_at
        FROM tickets
        JOIN events ON events.id = tickets.event_id
        WHERE tickets.user_id = ?
        ORDER BY tickets.id DESC
        """,
        (g.user["id"],),
    ).fetchall()
    db.close()

    return render_template("tickets.html", tickets=rows)


# Admin login/logout
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        flash("Invalid admin credentials.", "danger")
        return redirect("/admin/login")

    session["is_admin"] = True
    flash("Admin logged in.", "success")
    return redirect("/events")


@app.route("/admin/logout")
def admin_logout():
    session.pop("is_admin", None)
    flash("Admin logged out.", "info")
    return redirect("/events")


# Admin: Events CRUD (forms use DD/MM/YYYY + HH:MM)
@app.route("/admin/events/new", methods=["GET", "POST"])
@admin_required
def admin_new_event():
    if request.method == "GET":
        return render_template("admin_edit_event.html", event=None, form_date="", form_time="")

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    date_pt = request.form.get("date", "").strip()
    time_pt = request.form.get("time", "").strip()
    image_url = request.form.get("image_url", "").strip()
    price_str = request.form.get("price_member_cents", "0").strip()

    try:
        price_member_cents = int(price_str)
    except ValueError:
        price_member_cents = 0

    if not title or not description or not date_pt or not time_pt:
        flash("Title, description, date and time are required.", "warning")
        return redirect("/admin/events/new")

    try:
        starts_at = sqlite_dt_from_pt(date_pt, time_pt)
    except ValueError:
        flash("Invalid date or time. Use DD/MM/AAAA and HH:MM.", "danger")
        return redirect("/admin/events/new")

    if image_url == "":
        image_url = None

    if price_member_cents < 0:
        price_member_cents = 0

    db = get_db()
    db.execute(
        """
        INSERT INTO events (title, description, starts_at, image_url, price_member_cents)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, description, starts_at, image_url, price_member_cents),
    )
    db.commit()
    db.close()

    flash("Event created successfully.", "success")
    return redirect("/events")


@app.route("/admin/events/<int:event_id>/edit", methods=["GET", "POST"])
@admin_required
def admin_edit_event(event_id):
    db = get_db()
    ev = db.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()

    if ev is None:
        db.close()
        flash("Event not found.", "danger")
        return redirect("/events")

    if request.method == "GET":
        starts_at = ev["starts_at"]
        form_date = pt_date_from_iso(str(starts_at)[0:10])
        form_time = pt_time_from_sqlite_dt(starts_at)
        db.close()
        return render_template("admin_edit_event.html", event=ev, form_date=form_date, form_time=form_time)

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    date_pt = request.form.get("date", "").strip()
    time_pt = request.form.get("time", "").strip()
    image_url = request.form.get("image_url", "").strip()
    price_str = request.form.get("price_member_cents", "0").strip()

    try:
        price_member_cents = int(price_str)
    except ValueError:
        price_member_cents = 0

    if not title or not description or not date_pt or not time_pt:
        db.close()
        flash("Title, description, date and time are required.", "warning")
        return redirect(f"/admin/events/{event_id}/edit")

    try:
        starts_at = sqlite_dt_from_pt(date_pt, time_pt)
    except ValueError:
        db.close()
        flash("Invalid date or time. Use DD/MM/AAAA and HH:MM.", "danger")
        return redirect(f"/admin/events/{event_id}/edit")

    if image_url == "":
        image_url = None

    if price_member_cents < 0:
        price_member_cents = 0

    db.execute(
        """
        UPDATE events
        SET title = ?, description = ?, starts_at = ?, image_url = ?, price_member_cents = ?
        WHERE id = ?
        """,
        (title, description, starts_at, image_url, price_member_cents, event_id),
    )
    db.commit()
    db.close()

    flash("Event updated.", "success")
    return redirect("/events")


@app.route("/admin/events/<int:event_id>/delete", methods=["POST"])
@admin_required
def admin_delete_event(event_id):
    db = get_db()
    ev = db.execute("SELECT id FROM events WHERE id = ?", (event_id,)).fetchone()
    if ev is None:
        db.close()
        flash("Event not found.", "danger")
        return redirect("/events")

    db.execute("DELETE FROM events WHERE id = ?", (event_id,))
    db.commit()
    db.close()

    flash("Event deleted.", "info")
    return redirect("/events")


# Admin: Members
@app.route("/admin/members")
@admin_required
def admin_members():
    db = get_db()
    rows = db.execute(
        "SELECT id, name, email, member_number, dues_paid_until FROM users ORDER BY id DESC"
    ).fetchall()
    db.close()
    return render_template("admin_members.html", members=rows)


@app.route("/admin/members/new", methods=["GET", "POST"])
@admin_required
def admin_new_member():
    if request.method == "GET":
        return render_template("admin_new_member.html")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    member_number = request.form.get("member_number", "").strip()
    temp_password = request.form.get("temp_password", "")
    dues_paid_until_pt = request.form.get("dues_paid_until", "").strip()

    if not name or not email or not member_number or not temp_password:
        flash("Name, email, member number and temporary password are required.", "warning")
        return redirect("/admin/members/new")

    if dues_paid_until_pt:
        try:
            dues_paid_until = parse_date_ddmmyyyy(dues_paid_until_pt)
        except ValueError:
            flash("Invalid dues date. Use DD/MM/AAAA.", "danger")
            return redirect("/admin/members/new")
    else:
        dues_paid_until = "1970-01-01"

    password_hash = generate_password_hash(temp_password)

    db = get_db()
    try:
        db.execute(
            """
            INSERT INTO users (name, email, password_hash, member_number, dues_paid_until)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, password_hash, member_number, dues_paid_until),
        )
        db.commit()
    except sqlite3.IntegrityError:
        db.close()
        flash("Email or member number already exists.", "danger")
        return redirect("/admin/members/new")

    db.close()
    flash("Member created successfully.", "success")
    return redirect("/admin/members")


@app.route("/admin/members/<int:user_id>/edit", methods=["GET", "POST"])
@admin_required
def admin_edit_member(user_id):
    db = get_db()
    user = db.execute(
        "SELECT id, name, email, member_number, dues_paid_until FROM users WHERE id = ?",
        (user_id,),
    ).fetchone()

    if user is None:
        db.close()
        flash("Member not found.", "danger")
        return redirect("/admin/members")

    if request.method == "GET":
        db.close()
        return render_template("admin_edit_member.html", member=user)

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    member_number = request.form.get("member_number", "").strip()
    dues_paid_until_pt = request.form.get("dues_paid_until", "").strip()
    new_password = request.form.get("new_password", "")

    if not name or not email or not member_number:
        db.close()
        flash("Name, email and member number are required.", "warning")
        return redirect(f"/admin/members/{user_id}/edit")

    if dues_paid_until_pt:
        try:
            dues_paid_until = parse_date_ddmmyyyy(dues_paid_until_pt)
        except ValueError:
            db.close()
            flash("Invalid dues date. Use DD/MM/AAAA.", "danger")
            return redirect(f"/admin/members/{user_id}/edit")
    else:
        dues_paid_until = "1970-01-01"

    try:
        if new_password:
            password_hash = generate_password_hash(new_password)
            db.execute(
                """
                UPDATE users
                SET name = ?, email = ?, member_number = ?, dues_paid_until = ?, password_hash = ?
                WHERE id = ?
                """,
                (name, email, member_number, dues_paid_until, password_hash, user_id),
            )
        else:
            db.execute(
                """
                UPDATE users
                SET name = ?, email = ?, member_number = ?, dues_paid_until = ?
                WHERE id = ?
                """,
                (name, email, member_number, dues_paid_until, user_id),
            )

        db.commit()
    except sqlite3.IntegrityError:
        db.close()
        flash("Email or member number already exists.", "danger")
        return redirect(f"/admin/members/{user_id}/edit")

    db.close()
    flash("Member updated.", "success")
    return redirect("/admin/members")


@app.route("/admin/members/<int:user_id>/delete", methods=["POST"])
@admin_required
def admin_delete_member(user_id):
    db = get_db()
    user = db.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
    if user is None:
        db.close()
        flash("Member not found.", "danger")
        return redirect("/admin/members")

    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    db.close()

    flash("Member deleted.", "info")
    return redirect("/admin/members")
