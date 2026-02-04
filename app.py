from flask import Flask, render_template, request, redirect, url_for #import requirements 
from model import LibraryModel # call the class by model.py 

app = Flask(__name__)#starting app 
library = LibraryModel()  

@app.route("/") # start a general route to redirect when click on link
def index():
    books = library.get_all_books()
    return render_template("index.html", books=books)

#start a route for adding books details 
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        library.create_book(title, author)
        return redirect(url_for("index"))
    return render_template("add.html")

#start a route for edit a details 
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        library.update_book(id, title, author)
        return redirect(url_for("index"))

    book = library.get_book_by_id(id)
    return render_template("edit.html", book=book)

#start a router for delete exist details of books 
@app.route("/delete/<int:id>")
def delete(id):
    library.delete_book(id)
    return redirect(url_for("index"))

# call a APP when file run 
if __name__ == "__main__":
    app.run(debug=True)
