#task
#Щоб виконати принцип єдиної відповідальності (SRP), створіть клас Book, який відповідатиме за зберігання інформації про книгу.
#Щоб забезпечити принцип відкритості/закритості (OCP), зробіть так, щоб клас Library міг бути розширений для нової функціональності без зміни його коду.
#Щоб виконати принцип підстанови Лісков (LSP), переконайтеся, що будь-який клас, який наслідує інтерфейс LibraryInterface, може замінити клас Library без порушення роботи програми.
#Щоб виконати принцип розділення інтерфейсів (ISP), використовуйте інтерфейс LibraryInterface для чіткої специфікації методів, які необхідні для роботи з бібліотекою library.
#Щоб виконати принцип інверсії залежностей (DIP), зробіть так, щоб класи вищого рівня, такі як LibraryManager, залежали від абстракцій (інтерфейсів), а не від конкретних реалізацій класів.


from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(
    level=logging.INFO,
    format='\n%(message)s',
)
logger = logging.getLogger(__name__)

def log_and_flush(message: str) -> None:
    logger.info(message)
    for handler in logger.handlers:
        handler.flush()

class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        original_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < original_count:
            logger.info(f"Book removed: {title}")
        else:
            logger.info(f"No book found with title: {title}")

    def get_books(self) -> List[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("Library is empty.")
        else:
            for book in books:
                logger.info(str(book))


def main() -> None:
    library: LibraryInterface = Library()
    manager = LibraryManager(library)

    while True:
        log_and_flush("Enter command (add, remove, show, exit):")
        command = input().strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                log_and_flush("Exiting program...")
                break
            case _:
                log_and_flush("Invalid command. Please try again.")


if __name__ == "__main__":
    main()