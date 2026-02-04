from flask import Flask, render_template, request, redirect, url_for
from model import LibraryModel

app = Flask(__name__)
library = LibraryModel()  

@app.route("/")
def index():
    books = library.get_all_books()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        library.create_book(title, author)
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        library.update_book(id, title, author)
        return redirect(url_for("index"))

    book = library.get_book_by_id(id)
    return render_template("edit.html", book=book)


@app.route("/delete/<int:id>")
def delete(id):
    library.delete_book(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
