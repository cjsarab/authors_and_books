import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Stephen", "King")
author_repository.save(author_1)

author_2 = Author("Christopher", "Brookmyre")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("The Shining", "Horror", author_1)
book_repository.save(book_1)

book_2 = Book("IT", "Horror", author_1)
book_repository.save(book_2)

book_3 = Book("Quite Ugly One Morning", "Novel", author_2)
book_repository.save(book_3)

book_4 = Book("Boiling a Frog", "Novel", author_2)
book_repository.save(book_4)

book_repository.select_all()