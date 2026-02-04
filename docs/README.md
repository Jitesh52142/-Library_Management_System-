# Library Management System

This is a simple **Library Management System** built using **Flask** and **SQLite**.  
The application allows users to add, view, edit, and delete books.

The main goal of this project is to understand how Flask works with routing, templates, and a local database.

---

## What this project does

- Add book details (title and author)
- Show all books stored in the database
- Edit existing book information
- Delete books from the library
- Automatically creates a local SQLite database

---

## Folder Structure


library_system/
│
├── app.py # Flask app and routes
├── model.py # Database logic (SQLite + CRUD)
├── library.db # SQLite database (created automatically)
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── add.html
│ └── edit.html
│
├── static/
│ └── style.css
|
├── docs
 └── README.md
 └──requirements.txt
 └──.gitignore 


 
---

## Technologies Used

- Python
- Flask
- SQLite
- HTML & CSS

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
