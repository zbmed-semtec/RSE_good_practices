# Bookstore Package

A demonstration package for teaching Python best practices. This package implements a simple book management system to illustrate:

- Clean code principles
- Proper package structure
- Good naming conventions
- Comprehensive documentation
- Type hints
- Testing practices

## Project Structure

```
bookstore/
├── src/
│   └── bookstore/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── book.py
│       ├── repositories/
│       │   ├── __init__.py
│       │   └── book_repository.py
│       └── exceptions/
│           ├── __init__.py
│           └── book_exceptions.py
└── tests/
    └── test_book.py
```

## Installation

For development:
```bash
pip install -e ".[dev]"
```

## Usage Example

```python
from bookstore.models.book import Book
from bookstore.repositories.book_repository import BookRepository

# Create a new book
book = Book(
    isbn="978-0-7475-3269-9",
    title="Harry Potter and the Philosopher's Stone",
    author="J.K. Rowling",
    publication_year=1997
)

# Store the book
repository = BookRepository()
repository.add_book(book)

# Retrieve a book
found_book = repository.get_book_by_isbn("978-0-7475-3269-9")
```

## Development Practices Demonstrated

1. **Clear Module Structure**: Separation of concerns between models, repositories, and exceptions
2. **Type Hints**: All functions include proper type annotations
3. **Documentation**: Google-style docstrings with examples
4. **Error Handling**: Custom exceptions and proper error messages
5. **Testing**: Comprehensive unit tests with pytest
6. **Clean Code**: Short, focused methods with clear responsibilities

## Contributing

This is an educational project. Feel free to fork and experiment! 