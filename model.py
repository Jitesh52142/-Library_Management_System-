
import sqlite3

class LibraryModel:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    # ---------- CRUD OPERATIONS here ----------

    def create_book(self, title, author):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author)
        )
        conn.commit()
        conn.close()

    def get_all_books(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    def get_book_by_id(self, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )
        book = cursor.fetchone()
        conn.close()
        return book

    def update_book(self, book_id, title, author):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE books SET title=?, author=? WHERE id=?",
            (title, author, book_id)
        )
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM books WHERE id=?",
            (book_id,)
        )
        conn.commit()
        conn.close()
