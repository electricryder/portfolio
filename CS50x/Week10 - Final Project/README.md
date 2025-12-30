# Vortex

## Description

Vortex is a web-based application developed as my final project for CS50x.
It simulates the internal management system of a small cultural association, focusing on members, events, ticket sales, and membership dues.

The application was designed to resemble a real-world scenario, where an association organizes events, manages members internally, and provides members with access to tickets and membership information through a secure login system.

This project makes use of Flask, SQLite, HTML, CSS, and Python, and applies several of the core concepts learned throughout the course, including authentication, database design, server-side logic, and templating.

---

## Main Features

### Public Area
- Anyone can access the application without logging in.
- Upcoming and past events are listed separately.
- Each event includes a title, description, date, time, and an optional image.
- All dates are displayed in Portuguese format (`DD/MM/YYYY hh:mmh`).

### Member Area
Members can log in using their email and password. Once logged in, members gain access to:

- A personal member area.
- A digital membership card.
- A list of purchased tickets.
- Membership dues status.

Members can:
- Buy tickets for upcoming events (one ticket per event).
- Pay membership dues (1€ per month).
- Pay dues in advance, even if their dues are already up to date.
- Change their password securely by confirming their current password.

Ticket purchases and member features are restricted if membership dues are not valid.

---

## Ticket System

- Each ticket corresponds to one event and one member.
- Tickets are assigned a unique ID, generated automatically in order of purchase.
- Duplicate ticket purchases for the same event are prevented.
- Purchased tickets are listed in the member’s ticket area with event details and purchase date.

---

## Admin Area

The application includes a separate administrator mode.

Administrators can:
- Log in using dedicated admin credentials.
- Create, edit, and delete events.
- Add new members manually.
- Edit existing members, including updating dues status.
- Remove members, which also removes their associated tickets.

The admin interface uses the same event list as the public view, with additional management actions available.

---

## Date and Time Handling

Internally, all dates and times are stored in the database using ISO format for reliability.

For user interaction:
- Dates are displayed as `DD/MM/YYYY`
- Times are displayed as `hh:mmh`
- Admin forms accept dates and times in Portuguese-friendly formats and convert them internally.

This approach ensures consistency while maintaining user-friendly input and output.

---

## Project Structure

- `app.py`
  The main Flask application file.
  Contains all routes, authentication logic, admin logic, formatting filters, and business rules.

- `helpers.py`
  Contains decorators and helper functions used to enforce login, admin access, and membership dues validation.

- `schema.sql`
  Defines the SQLite database schema, including tables for users, events, and tickets.

- `association.db`
  SQLite database file used by the application.

- `templates/`
  Contains all HTML templates rendered by Flask, including public pages, member pages, and admin pages.

- `static/`
  Contains static files such as CSS and images used by the application.

---

## Design Choices

- Flask was chosen for its simplicity and flexibility.
- SQLite was used to keep the project lightweight and easy to deploy.
- Membership dues are handled using a “paid until” date instead of individual transactions.
- The ticket system is intentionally limited to one ticket per member per event to simplify logic and prevent abuse.
- A high-contrast black-and-white design was chosen for clarity and visual consistency.
- Admin operations are intentionally separated from public member functionality to reflect real-world workflows.

---

## How to Run the Application

1. Install dependencies:
```bash
pip install -r requirements.txt

2. Initialize the database:

sqlite3 association.db < schema.sql

3. Run the application:

flask run

4. Open the browser and go to:

http://127.0.0.1:5000
```

---

## Use of AI
Some parts of this project were developed with assistance from ChatGPT (OpenAI), mainly to help structure the application and refine logic.
All generated code was reviewed, understood, and adapted by the author before being included in the final project.

## Final Notes
This project represents the practical application of the concepts learned throughout CS50x and aims to simulate a realistic association management system rather than a purely academic exercise.
