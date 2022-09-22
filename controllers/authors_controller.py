from http.client import USE_PROXY
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import author_repository, book_repository
from models.author import Author
from models.book import Book

authors_blueprint = Blueprint("authors", __name__)

# restful roots

# INDEX
# GET /authors
@authors_blueprint.route("/authors")
def authors():
    authors=author_repository.select_all()
    return render_template("authors/index.html", all_authors=authors)

# # NEW
# # GET /authors/new
@authors_blueprint.route("/authors/new")
def new_author():
    return render_template("/authors/new.html")

# # CREATE
# # POST /authors
@authors_blueprint.route("/authors", methods = ['POST'])
def create_author():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    new_author = Author(first_name, last_name)
    author_repository.save(new_author)
    return redirect ('/authors')

# # SHOW
# # GET /books/<id>
@authors_blueprint.route("/authors/<id>")
def show_author(id):
    author = author_repository.select(id)
    return render_template("authors/show.html", author = author)

# # EDIT
# # GET /books/<id>/edit
@authors_blueprint.route("/authors/<id>/edit")
def edit_author(id):
    author = author_repository.select(id)
    return render_template('authors/edit.html', author=author, all_authors=authors)

# # UPDATE
# # PUT /books/<id>
@authors_blueprint.route("/authors/<id>", methods=['POST'])
def update_task(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    author_to_update = Author(first_name, last_name, id)
    author_repository.update(author_to_update)
    return redirect ('/authors/' + id)

# # DELETE
# # DELETE /books/<id>/delete
@authors_blueprint.route("/authors/<id>/delete", methods=['POST'])
def delete_task(id):
    author_to_delete = id
    author_repository.delete(author_to_delete)
    return redirect ('/authors')