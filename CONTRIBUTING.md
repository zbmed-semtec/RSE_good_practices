# Contributing to Bookstore Package

Thank you for your interest in contributing to the Bookstore Package! This document provides guidelines and instructions for contributing.

## Getting Started

If you are internal contributor of ZBMED, you can start by cloning the repository to your local machine:

```bash
git clone https://github.com/ZBMED/bookstore.git
```

If you are an external contributor of ZBMED, you can start by forking the repository and then cloning it to your local machine:

1. Fork the repository

2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/bookstore.git
   cd bookstore
   ```
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```


## Development Workflow

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes:
   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. Commit your changes:

   ```bash
   git add .
   git commit -m "✨ Add book categories"
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request

## Branch Naming Convention

- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent fixes
- `refactor/*` - Code improvements
- `docs/*` - Documentation changes
- `test/*` - Test additions

## Commit Message Convention

We use the gitmoji convention for commit messages. You can find a list of emojis and their meaning here: https://gitmoji.dev/.

```
<emoji> <description>
```

Types:
- ✨ Add new feature
- 🐛 Fix bug
- 📝 Update documentation
- 🎨 Improve code structure/format
- ⚡️ Improve performance
- ✅ Add, update or pass tests
and many more.

Examples:
```
✨ Add book categories
🐛 Fix duplicate ISBN error
📝 Update README with new features
⚡️ Improve performance of book search
✅ Add, update or pass tests for book categories
```

## Code Style Guidelines

1. **Python Version**: Use Python 3.8 or higher

2. **Type Hints**:
   ```python
   def add_book(self, book: Book) -> None:
       """Add a book to the repository."""
       pass
   ```

3. **Docstrings**: Use Google style
   ```python
   def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
       """
       Retrieve a book by its ISBN.
       
       Args:
           isbn: The ISBN to look up
           
       Returns:
           The book if found, None otherwise
       """
       pass
   ```

4. **Testing**:
   - Write unit tests for all new functionality
   - Maintain test coverage above 90%
   - Use pytest fixtures for test setup

## Pull Request Process

Be sure to follow the PR best practices:

1. Update the README.md with details of changes if needed
2. Add or update tests as needed
3. Update documentation
4. Ensure all tests pass
5. Get review from at least one maintainer

## Code Review Process

1. **Review Checklist**:
   - [ ] Code follows style guidelines
   - [ ] Tests are added and passing
   - [ ] Documentation is updated
   - [ ] Commit messages follow convention
   - [ ] Changes are focused and logical

2. **Feedback**:
   - Be constructive and helpful
   - Explain your reasoning
   - Suggest improvements

## Getting Help

If you need help, you can:
1. Open an issue with your question
2. Comment on the relevant issue or PR
3. Reach out to the maintainers

Thank you for contributing! 