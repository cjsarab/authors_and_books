from db.run_sql import run_sql

import repositories.author_repository as author_repository

from models.author import Author
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id=id
    return book

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        book = Book(result['title'], result['genre'], result['author_id'], result['id'])
    
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], author, row['id'])
        books.append(book)
        # print(books)
    return books

def update(book):
    sql = "UPDATE books SET (title, genre, author_id) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.author.id, book.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM books WHERE id= %s"
    values =[id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
