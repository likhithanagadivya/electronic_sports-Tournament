# 🎮 Electronic Sports Tournament Management System

## 📌 Project Overview

The **Electronic Sports (E-Sports) Tournament Management System** is a Python and MySQL-based application designed to manage and organize gaming tournaments efficiently.

The system allows administrators to manage **players, teams, tournaments, matches, scores, and results**. It reduces manual work and provides an organized way to maintain tournament information using a MySQL database.

---

## 🎯 Objectives

* Manage E-Sports tournaments efficiently.
* Register and manage players and teams.
* Schedule and manage tournament matches.
* Record match scores and results.
* Track team/player performance.
* Store tournament information securely in MySQL.
* Reduce manual record-keeping.
* Provide an easy-to-use management system.

---

## 🛠️ Technologies Used

| Technology                 | Purpose                   |
| -------------------------- | ------------------------- |
| **Python**                 | Application development   |
| **MySQL**                  | Database management       |
| **MySQL Connector/Python** | Connect Python with MySQL |
| **SQL**                    | Database queries          |
| **Git & GitHub**           | Version control           |

---

## ✨ Features

### 👤 Player Management

* Add new players
* View player details
* Update player information
* Delete player records

### 👥 Team Management

* Create teams
* Add players to teams
* View team details
* Update team information
* Delete teams

### 🏆 Tournament Management

* Create tournaments
* View tournament details
* Update tournament information
* Delete tournaments
* Manage tournament status

### 🎮 Match Management

* Schedule matches
* Assign teams to matches
* Record match scores
* Update match results
* View match history

### 📊 Results & Performance

* Display tournament results
* Track team scores
* Identify winners
* View player/team performance

---

## 🗄️ Database Structure

The project uses MySQL to store and manage application data.

### Main Tables

```text
Players
--------
player_id
player_name
email
phone
team_id

Teams
--------
team_id
team_name
captain
created_date

Tournaments
--------
tournament_id
tournament_name
game_name
start_date
end_date
status

Matches
--------
match_id
tournament_id
team1_id
team2_id
match_date
team1_score
team2_score
winner_id
```

### Relationship

```text
Players
   |
   | belongs to
   ↓
Teams
   |
   | participates in
   ↓
Tournaments
   |
   | contains
   ↓
Matches
```

---

## 📁 Project Structure

```text
electronic_sports-Tournament/
│
├── main.py
├── database.py
├── player.py
├── team.py
├── tournament.py
├── match.py
├── requirements.txt
├── README.md
│
└── sql/
    └── database.sql
```

> You can change the file names above according to your actual project structure.

---

## ⚙️ Requirements

Before running the project, install:

* Python 3.x
* MySQL Server
* MySQL Workbench (optional)
* Git

Install the required Python package:

```bash
pip install mysql-connector-python
```

---

## 🗃️ Database Setup

### 1. Start MySQL

Make sure your MySQL server is running.

### 2. Create the Database

Open MySQL and execute:

```sql
CREATE DATABASE esports_tournament;
```

### 3. Select the Database

```sql
USE esports_tournament;
```

### 4. Create Tables

Run the SQL commands from:

```text
sql/database.sql
```

or create the required tables manually.

---

## 🔌 Database Connection

Example Python database connection:

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="esports_tournament"
)

cursor = connection.cursor()

print("Database connected successfully!")
```

Replace:

```text
your_password
```

with your MySQL password.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/electronic_sports-Tournament.git
```

### Step 2: Open the Project

```bash
cd electronic_sports-Tournament
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure MySQL

Update the database username, password, and database name in your Python database connection file.

### Step 5: Run the Application

```bash
python main.py
```

---

## 🖥️ Sample Menu

```text
========================================
 Electronic Sports Tournament Management
========================================

1. Player Management
2. Team Management
3. Tournament Management
4. Match Management
5. View Results
6. Exit

Enter your choice:
```

---

## 🔄 System Workflow

```text
Admin
  ↓
Register Players
  ↓
Create Teams
  ↓
Create Tournament
  ↓
Schedule Matches
  ↓
Enter Match Scores
  ↓
Calculate Results
  ↓
Display Winner
```

---

## 🔐 Security

* Database credentials should not be hard-coded in production.
* User input should be validated.
* SQL queries should use parameterized statements to reduce SQL injection risks.

Example:

```python
query = "INSERT INTO players (player_name, email) VALUES (%s, %s)"

values = (player_name, email)

cursor.execute(query, values)
connection.commit()
```

---

## 🚀 Future Enhancements

The project can be extended with:

* 🔑 Admin login and authentication
* 🏅 Leaderboard
* 📈 Tournament statistics
* 🌐 Web-based interface
* 📱 Mobile application
* 🏆 Automatic tournament bracket generation
* 📧 Email notifications
* 📊 Performance dashboards
* 👨‍💻 Player ranking system

---

## 🎓 Project Use

This project is suitable for:

* Python projects
* MySQL database projects
* College final-year projects
* Mini projects
* CRUD application practice
* Python + SQL interview demonstrations

---

## 👩‍💻 Author

**Likhitha**

B.Sc. Computer Science

---

## 📄 License

This project is created for educational and learning purposes.

