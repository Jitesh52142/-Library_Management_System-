
import sqlite3 # call sqllite to create a local db to save logs.


# create a class to generate a local db structure. 
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


    ## starting a curd opreation in the class for liberary management ------------


    # start a function to create or add books details
    def create_book(self, title, author): 
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author)
        )
        conn.commit()
        conn.close()

    # start a function to view all avalibles.
    def get_all_books(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return books

    #start a function to search book by id.
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

    #a function to update details of books avalible 
    def update_book(self, book_id, title, author):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE books SET title=?, author=? WHERE id=?",
            (title, author, book_id)
        )
        conn.commit()
        conn.close()

    # a function to delete books entire
    def delete_book(self, book_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM books WHERE id=?",
            (book_id,)
        )
        conn.commit()
        conn.close()
