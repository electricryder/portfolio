# 💰 Finance — CS50x Week 9 (Flask)

**Goal:** Build a Flask web application that simulates a stock trading platform where users can register, log in, and buy or sell stocks in real time.

---

### 🧠 Key Concepts
- Flask routing and Jinja2 templating  
- User registration and login with password hashing  
- Integration with external APIs for real-time stock quotes  
- SQLite database for transactions and user data  
- Session management and CSRF protection  
- Input validation and error handling  

---

### 📁 Project Structure


finance/
├── app.py
├── helpers.py
├── finance.db
├── static/
│ └── styles.css
├── templates/
│ ├── layout.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── quote.html
│ ├── buy.html
│ ├── sell.html
│ └── history.html
└── README.md


---

### ⚙️ Features
✅ Register & Log In — Secure authentication using hashed passwords  
✅ Get Quotes — Fetch real-time stock prices from an external API  
✅ Buy & Sell Stocks — Simulate trading and portfolio management  
✅ Transaction History — Record every buy/sell with timestamps  
✅ Dynamic Portfolio — Real-time updates of user holdings and total value  
✅ Error Handling — Clean messages and flash alerts for invalid actions  

---

### ▶️ Running Locally
```bash
flask run
```

If you use the CS50 IDE, start the app with:

flask run


Then open the displayed URL in your browser.

# 💡 What I Learned

How to design a full-stack web application using Flask, integrate APIs, handle databases, and ensure user security.
This project ties together everything from CS50x — Python, SQL, HTML, CSS, and backend logic — into a working, real-world app.