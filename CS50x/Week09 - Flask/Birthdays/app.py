from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Add the user's entry into the database
        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))

        db.execute("INSERT INTO birthdays (name, day, month) VALUES(?, ?, ?)", name, day, month)

        return redirect("/")

    else:  # request.method == "GET"

        # Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    # Inline edit: read updated values from the row’s form
    name = request.form.get("name")
    day = request.form.get("day")
    month = request.form.get("month")
    db.execute("UPDATE birthdays SET name = ?, day = ?, month = ? WHERE id = ?", name, day, month, id)
    return redirect("/")
