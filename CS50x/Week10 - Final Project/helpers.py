# helpers.py
# Some parts of this project were developed with assistance from ChatGPT (OpenAI).

from functools import wraps
from datetime import date
from flask import session, redirect, url_for, flash, g, request


def login_required(message="Please log in first."):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get("user_id") is None:
                flash(message, "warning")
                next_url = request.full_path if request.query_string else request.path
                return redirect(url_for("login", next=next_url))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def dues_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user["dues_ok"]:
            flash("Your membership dues are not up to date.", "danger")
            return redirect(url_for("dues"))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("is_admin"):
            flash("Admin access required.", "danger")
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)
    return decorated_function


def is_dues_ok(dues_paid_until):
    """
    Check if membership dues are up to date.
    dues_paid_until format: YYYY-MM-DD
    """
    try:
        paid_until = date.fromisoformat(dues_paid_until)
    except ValueError:
        return False

    return paid_until >= date.today()
