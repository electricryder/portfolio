import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# ----------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------HEADERS
# ----------------------------------------------------------------------------------------------------------------------------
# Check if str is an int


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# ----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------INDEX
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    stock_total_sum = 0
    # Passes the informations required for the portfolio, in the form of a list of dicts
    register = db.execute(
        "SELECT *, SUM(shares) as sum_shares FROM transactions WHERE user_id = ? GROUP BY symbol", session["user_id"])
    for _ in register:

        # Checks if there are shares to show. This number can't be 0 or negative to show in the portfolio
        if _["sum_shares"] <= 0:
            continue

        # Get the symbol from the database, already joined by symbol
        portfolio_symbol = _["symbol"]

        # Get the price with the lookup function
        stock_price = lookup(portfolio_symbol)["price"]

        # Add to the dict the uds value of the stock price
        _.update({"stock_price": usd(stock_price)})

        # Add to the dict the total amount of money worth on owned stocks
        stock_total = float(stock_price * _["sum_shares"])
        stock_total_usd = usd(stock_total)
        _.update({"stock_total": stock_total_usd})

        # Calculate the total value of owned stocks (sum of all stocks)
        stock_total_sum += stock_total

    # Get the user's cash
    row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    current_cash = row[0]["cash"]

    # Calculate the total cash balance
    cash_balance = usd(stock_total_sum + current_cash)

    return render_template("index.html", holdings=register, cash_balance=cash_balance, current_cash=usd(current_cash))


# ----------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------BUY
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")
    else:  # POST method

        # Values posted
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validations
        if symbol == '':
            return apology("MUST PROVIDE SYMBOL!", 400)

        quote = lookup(symbol)
        if not quote:
            return apology("INVALID SYMBOL!", 400)
        elif shares == '':
            return apology("MUST PROVIDE NUMBER OF SHARES!", 400)
        elif not is_int(shares) or int(shares) <= 0:
            return apology("MUST PROVIDE A POSITIVE INTEGER!", 400)

        # Current user's money
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]

        # Purchase price
        price = quote["price"]
        total_cost = int(shares) * price

        # Check if user has enough money
        if total_cost > cash:
            return apology("NOT ENOUGH MONEY!", 400)

        # After purchase
        remaining_cash = cash - total_cost

        # Record the transaction
        db.execute("INSERT INTO transactions (user_id, symbol, name, shares, price) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], symbol.upper(), quote["name"], int(shares), quote["price"]
                   )

        # Update the user's cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, session["user_id"])

        return redirect("/")


# ----------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------HISTORY
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])

    return render_template("history.html", transactions=transactions)


# ----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------LOGIN
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------LOGOUT
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# ----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------QUOTE
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        quote = lookup(symbol)

        if symbol == '':
            return apology("The space is empty!", 400)
        elif not quote:
            return apology("Invalid symbol!", 400)

        quote["price"] = usd(quote["price"])

        return render_template("quoted.html", quote=quote)


# ----------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------REGISTER
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    else:
        # Credentials
        if not request.form.get("username"):
            return apology("Username is required!", 400)
        elif not request.form.get("password"):
            return apology("Password is required!", 400)
        elif not request.form.get("confirmation"):
            return apology("You must confirm your password!", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match!")

        # Checking for duplicates
        # Search for username in database
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 0:
            return apology("Username already registred!", 400)

        # Register new valid user
        username = request.form.get("username")
        hash = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)

        # Search for newly added user
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # New session for the user
        session["user_id"] = rows[0]["id"]

        # Redirects home
        return redirect("/")


# ----------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------SELL
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Passes the informations required for the selling list; the symbols of the available stocks and the total ammount of each
    register = db.execute("SELECT symbol, SUM(shares) "
                          "AS sum_shares "
                          "FROM transactions "
                          "WHERE user_id = ? "
                          "GROUP BY symbol",
                          session["user_id"])

    if request.method == "GET":
        return render_template("sell.html", stocks=register)
    else:
        # Get posted values
        submited_symbol = request.form.get("symbol")

        # Chech the actual sell price for this stock
        if not submited_symbol:
            return apology("STOCK SPACE EMPTY", 400)
        quote = lookup(submited_symbol)
        stock_price = quote["price"]

        # Available number of stocks for the submited symbol
        rows_1 = db.execute(
            "SELECT SUM(shares) AS sum_shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol ", session["user_id"], submited_symbol)
        stock_number = rows_1[0]["sum_shares"]

        # Submited number of stocks to sell
        submited_stocks_number = int(request.form.get("shares"))

        # Checks if there are enough owned stocks to sell
        if submited_stocks_number > stock_number:
            return apology("NOT ENOUGH STOCKS TO SELL", 400)
        else:
            # Subtracts sold stocks to the owned
            db.execute("INSERT INTO transactions (user_id, symbol, name, shares, price) VALUES (?, ?, ?, ?, ?)",
                       session["user_id"], submited_symbol.upper(), quote["name"], -submited_stocks_number, stock_price)

            # Sell price
            sell_price = submited_stocks_number * stock_price

            # Current user's money
            rows_2 = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
            cash = rows_2[0]["cash"]

            # After sell
            remaining_cash = cash + sell_price

            # Update the user's cash
            db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, session["user_id"])

            return redirect("/")

# ----------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------ADD CASH
# ----------------------------------------------------------------------------------------------------------------------------
@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Allow user to add more cash to their account"""

    if request.method == "GET":
        return render_template("add_cash.html")

    else:
        # Get input from form
        amount_str = request.form.get("amount")

        # Validate input
        if not amount_str:
            return apology("ENTER AMOUNT", 400)

        try:
            amount = float(amount_str)
        except ValueError:
            return apology("INVALID AMOUNT", 400)

        if amount <= 0:
            return apology("AMOUNT MUST BE POSITIVE", 400)

        # Update user's cash balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, session["user_id"])

        # Record it in transactions for full history
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], "CASH", 0, amount)

        return redirect("/")
