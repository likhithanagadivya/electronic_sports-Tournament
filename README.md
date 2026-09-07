# 🎮 Electronic Sports Tournament Management System

## Player, Tournament & Registration Management System

**Electronic Sports Tournament Management System** is a professional **Python + MySQL terminal/CLI application** designed to manage **players, esports tournaments, and tournament registrations** in one complete system.

> **Player → Tournament → Registration → Management**

---

## 🌟 Project at a Glance

### 👤 Player

* 📝 Add Player
* 👀 View Players
* ✏️ Update Player
* 🗑️ Delete Player
* 🎮 Register Player for Tournament

### 🏆 Tournament

* ➕ Add Tournament
* 👀 View Tournaments
* 📅 Manage Tournament Details
* 🎮 Register Players
* 📋 View Tournament Information

### 📋 Registration

* 📝 Register Player
* 🔗 Connect Players with Tournaments
* 👀 View Registrations
* 📊 Track Tournament Registrations

---

# 🎯 Why Electronic Sports Tournament Management System?

Electronic sports tournaments require proper management of players, tournaments, and registrations.

This project provides a simple and efficient way to manage tournament-related information using **Python and MySQL**.

### Main Benefits

* 👤 Easy Player Management
* 🏆 Easy Tournament Management
* 🎮 Simple Player Registration
* 🗄️ Database Storage
* 🔄 CRUD Operations
* 🔗 Relationship Between Tables
* 💻 Simple CLI Interface

The project is designed to demonstrate how a real-world management system can be developed using **Python with MySQL**.

---

# ✨ Main Features

| **Feature**           | **Description**                    |
| --------------------- | ---------------------------------- |
| 👤 Add Player         | Add new player information         |
| 👀 View Players       | Display all players                |
| ✏️ Update Player      | Update existing player information |
| 🗑️ Delete Player     | Delete player information          |
| 🏆 Add Tournament     | Create a new tournament            |
| 👀 View Tournaments   | Display available tournaments      |
| 🎮 Register Player    | Register a player for a tournament |
| 📋 View Registrations | Display tournament registrations   |
| 🗄️ MySQL Database    | Store project data                 |

---

# 👤 Player Management

The Player Management module allows the system to manage player information.

### Player Operations

```text
========== PLAYER MENU ==========

1. Add Player
2. View Players
3. Update Player
4. Delete Player
5. Back
```

Player information can include:

```text
Player ID
Player Name
Email
Phone Number
Game Name
Team Name
```

Example:

```text
PLAYER DETAILS

Player ID   : 101
Player Name : Likhitha
Email       : likhitha@example.com
Game Name   : BGMI
Team Name   : Thunder Squad
```

---

# 🏆 Tournament Management

The Tournament Management module allows tournaments to be created and viewed.

### Tournament Operations

```text
======== TOURNAMENT MENU ========

1. Add Tournament
2. View Tournaments
3. Back
```

Tournament information can include:

```text
Tournament ID
Tournament Name
Game Name
Tournament Date
Location
Prize Pool
```

Example:

```text
TOURNAMENT DETAILS

Tournament ID   : 1
Tournament Name : BGMI Championship
Game Name       : BGMI
Tournament Date : 15 September 2026
Location        : Hyderabad
Prize Pool      : ₹50,000
```

---

# 🎮 Player Registration

Players can register for available tournaments.

### Registration Workflow

```text
👤 Player
     │
     ▼
🏆 View Tournament
     │
     ▼
🎮 Select Tournament
     │
     ▼
📝 Register Player
     │
     ▼
✅ Registration Successful
```

The registration system connects a player with a tournament.

---

# 📋 Registration Management

The Registration module stores the relationship between players and tournaments.

Example:

```text
REGISTRATION DETAILS

Registration ID : 1
Player ID       : 101
Player Name     : Likhitha
Tournament ID   : 1
Tournament Name : BGMI Championship
Registration Date : 2026-09-07
```

---

# 🗄️ Database Design

The project contains **3 main tables**.

## 1️⃣ Players Table

The `players` table stores player information.

```text
players
│
├── player_id
├── player_name
├── email
├── phone
├── game_name
└── team_name
```

---

## 2️⃣ Tournaments Table

The `tournaments` table stores tournament information.

```text
tournaments
│
├── tournament_id
├── tournament_name
├── game_name
├── tournament_date
├── location
└── prize_pool
```

---

## 3️⃣ Registrations Table

The `registrations` table connects players with tournaments.

```text
registrations
│
├── registration_id
├── player_id
├── tournament_id
└── registration_date
```

### 🔗 Table Relationship

```text
              PLAYERS
                 │
                 │
             player_id
                 │
                 ▼
          REGISTRATIONS
                 ▲
                 │
          tournament_id
                 │
                 │
            TOURNAMENTS
```

The `registrations` table works as the connection between the `players` and `tournaments` tables.

---

# 🔄 CRUD Operations

The project demonstrates the four basic **CRUD operations**.

```text
C → Create
R → Read
U → Update
D → Delete
```

### Create

```text
Add Player
Add Tournament
Register Player
```

### Read

```text
View Players
View Tournaments
View Registrations
```

### Update

```text
Update Player
```

### Delete

```text
Delete Player
```

---

# 🏗️ Project Architecture

```text
              ELECTRONIC SPORTS
           TOURNAMENT MANAGEMENT
                    │
                    ▼
             Python Application
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Players   Tournaments  Registrations
          │         │         │
          └─────────┼─────────┘
                    ▼
              MySQL Database
```

---

# 💻 Main Menu

The application provides a simple menu-driven terminal interface.

```text
=============================================
 ELECTRONIC SPORTS TOURNAMENT MANAGEMENT
=============================================

1. Player Management
2. Tournament Management
3. Register Player
4. View Registrations
5. Exit
```

---

# 🔄 Complete Project Workflow

```text
START
  │
  ▼
Open Application
  │
  ▼
Main Menu
  │
  ├──────────────► Player Management
  │                    │
  │                    ├── Add Player
  │                    ├── View Players
  │                    ├── Update Player
  │                    └── Delete Player
  │
  ├──────────────► Tournament Management
  │                    │
  │                    ├── Add Tournament
  │                    └── View Tournaments
  │
  └──────────────► Registration
                       │
                       ├── Select Player
                       ├── Select Tournament
                       └── Register Player
```

---

# 🛠️ Technology Stack

| **Technology**                |
| ----------------------------- |
| 🐍 **Python**                 |
| 🗄️ **MySQL**                 |
| 🔌 **mysql-connector-python** |
| 💻 **CLI / Terminal**         |

---

# 📁 Project Structure

```text
electronic_sports-Tournament/
│
├── main.py
├── tournament.py
├── database.py
├── README.md
│
└── requirements.txt
```

### Main Python File

```text
main.py
```

Used to start the application and display the main menu.

### Tournament Module

```text
tournament.py
```

Contains the tournament management functions such as:

```text
add_player()
view_players()
update_player()
delete_player()

add_tournament()
view_tournaments()

register_player()
view_registrations()
```

### Database Module

```text
database.py
```

Used for MySQL database connectivity and database operations.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Open the Project Folder

```bash
cd electronic_sports-Tournament
```

## 3. Install Required Package

```bash
pip install mysql-connector-python
```

Or:

```bash
pip install -r requirements.txt
```

---

# 🗄️ MySQL Database Setup

Make sure **MySQL Server** is installed and running.

Create the database:

```sql
CREATE DATABASE electronic_sports;
```

Select the database:

```sql
USE electronic_sports;
```

Create the required tables:

```text
Players
Tournaments
Registrations
```

Configure the MySQL connection in the Python database configuration.

---

# ▶️ Run the Project

Run the application using:

```bash
python main.py
```

For macOS/Linux:

```bash
python3 main.py
```

The application will display the main menu in the terminal.

---

# 🎯 Main Objectives

The main objectives of this project are:

* 👤 Manage esports player information
* 🏆 Manage tournament information
* 🎮 Register players for tournaments
* 🗄️ Store data using MySQL
* 🔗 Create relationships between tables
* 🔄 Perform CRUD operations
* 🐍 Practice Python programming
* 💻 Build a real-world CLI application

---

# 📚 Concepts Used

This project demonstrates the following concepts:

```text
🐍 Python Functions
🐍 Python Modules
🐍 Loops
🐍 Conditional Statements
🐍 Exception Handling

🗄️ MySQL Database
🔌 MySQL Connectivity

➕ INSERT
🔍 SELECT
✏️ UPDATE
🗑️ DELETE

🔗 Primary Key
🔗 Foreign Key
📋 CRUD Operations
```

---

# 🏆 Project Highlights

```text
┌──────────────────────────────────────────────────────┐
│       ELECTRONIC SPORTS TOURNAMENT SYSTEM            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  👤 Player Management                                │
│  🏆 Tournament Management                            │
│  🎮 Player Registration                              │
│  ✏️ Update Player Information                        │
│  🗑️ Delete Player Information                        │
│  👀 View Players                                     │
│  👀 View Tournaments                                 │
│  📋 View Registrations                               │
│  🗄️ MySQL Database                                  │
│  🐍 Python                                           │
│  💻 CLI / Terminal                                   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

# 🔮 Future Enhancements

```text
🌐 Web Application
📱 Mobile Application
🔐 User Login & Authentication
👥 Team Management
🏆 Tournament Brackets
📊 Leaderboards
🎮 Multiple Game Support
📅 Match Scheduling
💰 Prize Management
🔔 Notifications
📧 Email Notifications
📊 Tournament Analytics
☁️ Cloud Deployment
```

---

# 👥 Complete User Journey

### 👤 Player

**Add Player → View Tournament → Register → Participate**

### 🏆 Tournament

**Create Tournament → View Tournament → Register Players → Manage Tournament**

### 🗄️ System

**Store Data → Update Data → View Data → Delete Data**

---

# 🤝 Contributing

```text
Fork Repository
      ↓
Create Feature Branch
      ↓
Make Changes
      ↓
Test Application
      ↓
Commit Changes
      ↓
Push Changes
      ↓
Create Pull Request
```

---

# 📜 Project Usage & License

This project is created for **educational, academic, and project demonstration purposes**.

The project demonstrates Python programming, MySQL database management, CRUD operations, and database relationships.

Please respect the project owner's source code and documentation.

---

# 👩‍💻 Developed By

**Jonnalagadda Sri Likhitha**

---

# 🎮 Electronic Sports Tournament Management System

## Manage Players. Organize Tournaments. Build Champions.

> **Play. Compete. Win. 🏆**
