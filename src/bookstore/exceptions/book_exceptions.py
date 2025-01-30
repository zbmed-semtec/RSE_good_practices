"""Custom exceptions for the bookstore package."""

from typing import TextIO


class BookstoreError(Exception):
    """Base exception class for all bookstore-related errors."""


class BookNotFoundError(BookstoreError):
    """Raised when a book cannot be found in the repository."""

    def __init__(self, isbn: str) -> None:
        """
        Initialize the exception.

        Args:
            isbn: The ISBN that was not found
        """
        super().__init__(f"Book with ISBN {isbn} not found")


class DuplicateBookError(BookstoreError):
    """Raised when attempting to add a book that already exists."""

    def __init__(self, isbn: str) -> None:
        """
        Initialize the exception.

        Args:
            isbn: The duplicate ISBN
        """
        super().__init__(f"Book with ISBN {isbn} already exists")


class InvalidISBNError(BookstoreError):
    """Raised when an invalid ISBN is provided."""

    def __init__(self, isbn: str, reason: str) -> None:
        """
        Initialize the exception.

        Args:
            isbn: The invalid ISBN
            reason: The reason why the ISBN is invalid
        """
        super().__init__(f"Invalid ISBN {isbn}: {reason}")


class InvalidPublicationYearError(BookstoreError):
    """Raised when an invalid publication year is provided."""

    def __init__(self, year: int, reason: str) -> None:
        """
        Initialize the exception.

        Args:
            year: The invalid publication year
            reason: The reason why the year is invalid
        """
        super().__init__(f"Invalid publication year {year}: {reason}")


class BooksCSVEmpty(BookstoreError):
    """Raised when the imported books csv is empty."""

    def __init__(self) -> None:
        """
        Initialize the exception.
        """
        super().__init__(f"The imported books CSV is empty")


class InvalidCSVHeader(BookstoreError):
    """Raised when CSV header does not correspond to any book property labels"""

    def __init__(self, header: list[str]) -> None:
        """
        Initialize the exception.

        Args:
            header: The invalid header content
        """
        super().__init__(
            f"The CSV header of { header } is not corresponding to any book properties"
        )


class InvalidCSV(BookstoreError):
    """Raised when the CSV content is invalid and can't be parsed"""

    def __init__(self, csv: TextIO) -> None:
        """
        Initialize the exception.

        Args:
            csv: CSV TextIO content
        """
        super().__init__(f"The CSV content is invalid: {csv}")
