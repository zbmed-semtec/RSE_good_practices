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

# Contributing

This is an educational project. Feel free to fork and experiment, but we have some tasks for you to complete.

## Tasks 1
Add Book Categories/Genres
Branch name: feature/book-categories
Scope:
- Add category field to Book class
- Add category validation
- Update repository to search by category
PR Learning Points:
- Single responsibility principle
- Database schema changes
- Test coverage for new field

## Tasks 2
Book Search Functionality
Branch name: feature/search-books
Scope:
- Add search by title/author
- Implement fuzzy matching
- Add search result pagination
PR Learning Points:
- Algorithm implementation
- Performance considerations
- Documentation of search parameters

## Tasks 3
Branch name: feature/book-ratings
Scope:
- Add Rating class
- Implement rating statistics
- Add rating constraints (1-5 stars)
PR Learning Points:
- Relationship between models
- Data validation
- Statistical calculations

## Tasks 4
Add Book Import/Export
Branch name: feature/import-export
Scope:
- CSV import/export
- JSON serialization
- Data validation
PR Learning Points:
- File handling
- Data formats
- Error handling

## Branch handling
It is important to know how to hadle and operate with branches.

### Naming Convention
- feature/   - For new features
- bugfix/    - For bug fixes
- hotfix/    - For urgent fixes
- refactor/  - For code improvements
- docs/      - For documentation changes
- test/      - For test additions

### Workflow
You can start the workflow by forking the repository and then cloning it to your local machine, but it depends on the access you have to the repository.

1. Create a new branch
```bash
git checkout -b feature/book-categories
```

2. Make changes

3. Commit changes

For commit messages remember to start with a git emoji and then a short description of the changes. You can find a list of emojis here: https://gitmoji.dev/.

Remember to always start with a verb and then the changes.

```bash
git commit -m "✨ Add book categories"
```

4. Push changes
```bash
git push origin feature/book-categories
```

5. Create a pull request
6. Merge pull request

## PR Best Practices
- Keep changes focused and small
- Write clear commit messages (using conventional commits)
- Include tests for new functionality
- Update documentation
- Respond to review comments promptly
- Squash commits before merging if needed
