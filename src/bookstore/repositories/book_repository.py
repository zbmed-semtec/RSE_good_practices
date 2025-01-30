"""Repository module for managing book storage and retrieval operations."""

from datetime import datetime
import pandas as pd
from typing import Dict, List, Optional, Protocol, TextIO

from ..exceptions.book_exceptions import (
    DuplicateBookError,
    BooksCSVEmpty,
    InvalidCSV,
    InvalidCSVHeader,
)
from ..models.book import Book


class StorageBackend(Protocol):
    """
    Protocol defining the interface for storage backends.

    This demonstrates the use of dependency injection and interface segregation.
    Different storage implementations (e.g., in-memory, file-based, database)
    can be used as long as they implement this protocol.
    """

    def save(self, key: str, data: dict) -> None:
        """Save data with the given key."""
        ...

    def load(self, key: str) -> Optional[dict]:
        """Load data for the given key."""
        ...

    def loadAll(self, key: str) -> Optional[dict]:
        """Load data for the given key."""
        ...

    def delete(self, key: str) -> None:
        """Delete data for the given key."""
        ...


class InMemoryStorage:
    """
    A simple in-memory storage implementation.

    This class demonstrates a concrete implementation of the StorageBackend
    protocol, using a dictionary as the storage mechanism.
    """

    def __init__(self) -> None:
        self._storage: Dict[str, dict] = {}

    def save(self, key: str, data: dict) -> None:
        """Save data to in-memory storage."""
        self._storage[key] = data

    def load(self, key: str) -> Optional[dict]:
        """Load data from in-memory storage."""
        return self._storage.get(key)

    def delete(self, key: str) -> None:
        """Delete data from in-memory storage."""
        self._storage.pop(key, None)


class BookRepository:
    """
    Repository for managing book operations.

    This class demonstrates:
    - Dependency injection (storage backend)
    - Single Responsibility Principle
    - Interface segregation
    - Clean method naming
    - Proper error handling

    Example:
        >>> storage = InMemoryStorage()
        >>> repo = BookRepository(storage)
        >>> book = Book(
        ...     isbn="978-0-7475-3269-9",
        ...     title="Harry Potter",
        ...     author="J.K. Rowling",
        ...     publication_year=1997
        ... )
        >>> repo.add_book(book)
        >>> found_book = repo.get_book_by_isbn(book.isbn)
        >>> found_book.title == "Harry Potter"
        True
    """

    def __init__(self, storage: Optional[StorageBackend] = None) -> None:
        """
        Initialize the repository with a storage backend.

        Args:
            storage: Implementation of StorageBackend protocol
                    If None, uses InMemoryStorage
        """
        self._storage = storage or InMemoryStorage()

    def add_book(self, book: Book) -> None:
        """
        Add a book to the repository.

        Args:
            book: The book to add

        Raises:
            DuplicateBookError: If a book with the same ISBN already exists
        """
        if self.get_book_by_isbn(book.isbn) is not None:
            raise DuplicateBookError(book.isbn)

        self._storage.save(book.isbn, self._book_to_dict(book))

    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Retrieve a book by its ISBN.

        Args:
            isbn: The ISBN to look up

        Returns:
            The book if found, None otherwise
        """
        data = self._storage.load(isbn)
        return self._dict_to_book(data) if data else None

    def delete_book(self, isbn: str) -> None:
        """
        Delete a book from the repository.

        Args:
            isbn: The ISBN of the book to delete
        """
        self._storage.delete(isbn)

    def import_book_csv(self, csv_file: TextIO) -> None:
        """Stores a list of books for a given CSV as books.
        
        Args:
            csv_file: The CSV file text content of the books CSV.

        Raises:
            InvalidCSVError: If the CSV cannot be parsed for any reason
            BooksCSVEmpty: If the CSV does not contain any books to import
            InvalidCSVHeader: If the CSV header is missing or does not contain an ISBN
        """
        books_dict = None
        books_csv_header = None
        try:
            books_df = pd.read_csv(csv_file)
            books_csv_header = books_df.columns
            books_df.columns = map(str.lower, books_csv_header)
            books_dict = books_df.T.to_dict()
        except:
            raise InvalidCSV(csv_file)
        if len(books_dict) == 0:
            raise BooksCSVEmpty()
        for key in books_dict:
            book = BookRepository._dict_to_book(books_dict[key])
            if book.isbn == None:
                raise InvalidCSVHeader(books_csv_header)
            self.add_book(book)

    @staticmethod
    def _book_to_dict(book: Book) -> dict:
        """Convert a Book object to a dictionary."""
        return {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "publication_year": book.publication_year,
            "description": book.description,
            "added_at": book.added_at.isoformat(),
        }
    
    @staticmethod
    def _dict_to_book(data: dict) -> Book:
        """Convert a dictionary to a Book object."""
        return Book(
            isbn=data["isbn"],
            title=data["title"],
            author=data["author"],
            publication_year=data["publication_year"],
            description=data["description"],
            added_at=datetime.fromisoformat(data["added_at"]),
        )
