# 🎬 Movies — CS50x Week 7

**Goal:** Practice writing SQL queries to analyze data in a movie database, using multiple tables connected by foreign keys.

---

### 🧠 Key Concepts
- Relational databases and table design  
- Primary and foreign keys  
- SQL `SELECT`, `JOIN`, `WHERE`, `GROUP BY`, `ORDER BY`, `LIMIT`  
- Aggregation functions (`COUNT`, `AVG`, `MAX`, `MIN`)  
- Filtering and combining data from multiple tables  

---

### ⚙️ Example Queries
```sql
-- List all movies released in 2008
SELECT title FROM movies WHERE year = 2008;

-- Find movies starring Johnny Depp
SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE people.name = 'Johnny Depp';
💡 What I Learned
How to design and query relational databases, connect tables with JOINs, and extract meaningful insights from structured data.