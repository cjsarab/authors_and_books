from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import author_repository, book_repository
from models.author import Author
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# restful roots

# INDEX
# GET /books
@books_blueprint.route("/books")
def books():
    books=book_repository.select_all()
    return render_template("books/index.html", all_books=books)

# NEW
# GET /books/new
@books_blueprint.route("/books/new")
def new_book():
    all_authors=author_repository.select_all()
    return render_template("/books/new.html", all_authors=all_authors)

# CREATE
# POST /books
@books_blueprint.route("/books", methods = ['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    new_book = Book(title, genre, author)
    book_repository.save(new_book)
    return redirect ('/books')


# SHOW
# GET /books/<id>
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)

# EDIT
# GET /books/<id>/edit
@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('books/edit.html', book=book, all_authors=authors)

# UPDATE
# PUT /books/<id>
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_task(id):
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    author = author_repository.select(author_id)

    book_to_update = Book(title, genre, author, id)
    book_repository.update(book_to_update)
    return redirect ('/books/' + id)

# DELETE
# DELETE /books/<id>/delete
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_task(id):
    book_to_delete = id
    book_repository.delete(book_to_delete)
    return redirect ('/books')