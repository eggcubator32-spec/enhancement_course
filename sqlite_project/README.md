# SQLite3 Python Project

A comprehensive Python project demonstrating SQLite3 database operations with full CRUD functionality.

## Overview

This project provides a complete example of building a Python application with SQLite3, featuring:

- **Database Management**: Connection pooling, transaction handling, and resource management
- **CRUD Operations**: Full Create, Read, Update, Delete functionality for Users and Tasks
- **Data Models**: Object-oriented data representation with dataclasses
- **Error Handling**: Comprehensive logging and exception handling
- **Type Hints**: Full type annotations for better code clarity

## Project Structure

```
sqlite_project/
├── main.py          # Main application with example usage
├── database.py      # Database connection and management
├── models.py        # Data models (User, Task)
├── crud.py          # CRUD operations (UserCRUD, TaskCRUD)
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## Features

✅ **Context Managers** - Proper resource cleanup with context managers  
✅ **Foreign Keys** - Relational data with cascade delete  
✅ **Error Handling** - Try-catch blocks and logging throughout  
✅ **Type Safety** - Full type hints for IDE support  
✅ **Logging** - Detailed operation tracking  
✅ **Modular Design** - Separation of concerns across modules  

## Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd sqlite_project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start

Run the example application:

```bash
python main.py
```

This will demonstrate all CRUD operations with sample data.

### Using in Your Code

```python
from database import Database
from crud import UserCRUD, TaskCRUD

# Initialize database
db = Database('tasks.db')
db.initialize()

# Create CRUD instances
user_crud = UserCRUD(db)
task_crud = TaskCRUD(db)

# Create a user
user_id = user_crud.create('John Doe', 'john@example.com')

# Create a task for the user
task_id = task_crud.create(
    title='Complete project',
    description='Finish the quarterly project',
    user_id=user_id
)

# Read all tasks for user
tasks = task_crud.read_by_user(user_id)

# Update task status
task_crud.update_status(task_id, 'in_progress')

# Clean up
db.close()
```

## Database Schema

### Users Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tasks Table

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    user_id INTEGER NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

## API Reference

### Database Class

- `__init__(db_path)` - Initialize database connection
- `connect()` - Establish connection
- `initialize()` - Create tables
- `execute(query, params)` - Execute SELECT query
- `execute_one(query, params)` - Execute and return single result
- `execute_update(query, params)` - Execute INSERT/UPDATE/DELETE
- `get_cursor()` - Context manager for cursor
- `close()` - Close connection

### UserCRUD Class

- `create(name, email)` - Create new user
- `read(user_id)` - Get user by ID
- `read_all()` - Get all users
- `update(user_id, name, email)` - Update user
- `delete(user_id)` - Delete user

### TaskCRUD Class

- `create(title, description, user_id)` - Create new task
- `read(task_id)` - Get task by ID
- `read_all()` - Get all tasks
- `read_by_user(user_id)` - Get tasks for specific user
- `update_status(task_id, status)` - Update task status
- `delete(task_id)` - Delete task

## Example Output

```
=== Creating Users ===
Created user: 1
Created user: 2
Created user: 3

=== Reading Users ===
Retrieved user: {'id': 1, 'name': 'Alice Johnson', 'email': 'alice@example.com', ...}
Total users: 3

=== Creating Tasks ===
Created task: 1
Created task: 2
Created task: 3

=== Reading Tasks ===
Total tasks: 3
  - Complete project proposal: pending
  - Review code: pending
  - Update documentation: pending

=== Final Summary ===
Total users: 3
Total tasks: 2
```

## Best Practices

1. **Always close connections**: Use `db.close()` or context managers
2. **Enable foreign keys**: Foreign key constraints are enabled by default
3. **Use parameterized queries**: Prevents SQL injection
4. **Check return values**: Verify success of create/update/delete operations
5. **Handle exceptions**: Wrap operations in try-catch blocks

## Logging

The project uses Python's built-in logging module. Configure logging level in main:

```python
logging.basicConfig(
    level=logging.INFO,  # or DEBUG for more detail
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Requirements

- Python 3.7+
- sqlite3 (included with Python)

## License

This project is provided as an educational example.

## Support

For issues or questions, refer to:
- [SQLite3 Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)
