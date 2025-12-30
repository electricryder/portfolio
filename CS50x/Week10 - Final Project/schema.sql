-- schema.sql
-- CS50x Final Project (Flask + SQLite)
-- Note: Some parts were drafted with assistance from ChatGPT (OpenAI) and then adapted by the author.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

-- USERS
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    member_number TEXT NOT NULL UNIQUE,

    -- Date until the annual fee is paid (YYYY-MM-DD)
    dues_paid_until TEXT NOT NULL DEFAULT '1970-01-01',

    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- EVENTS
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    starts_at TEXT NOT NULL,          -- ISO: YYYY-MM-DD HH:MM:SS
    image_url TEXT,                   -- optional (URL)
    price_member_cents INTEGER NOT NULL DEFAULT 0,

    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- TICKETS (each ticket = 1 line; ID by order of buy/creation)
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Ticket ID (order of sale)
    user_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,

    status TEXT NOT NULL DEFAULT 'paid',

    created_at TEXT NOT NULL DEFAULT (datetime('now')),

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- SEED DATA (example events - later changed)
INSERT INTO events (title, description, starts_at, image_url, price_member_cents) VALUES
(
  'Titan Lion',
  'Titan Lion band from Lisbon, performing their first gig!',
  datetime('now', '+10 days'),
  'https://picsum.photos/seed/titanlion/240/160',
  600
),
(
  'Nagasaki Sunrise',
  'Punk metal from Portugal!',
  datetime('now', '+20 days'),
  'https://picsum.photos/seed/nagasaki/240/160',
  600
),
(
  'Karaoke Night',
  'A Karaoke event full of Rock N'' Roll!',
  datetime('now', '-5 days'),
  'https://picsum.photos/seed/karaoke/240/160',
  600
);
