#!/usr/bin/env python3
"""
Main application demonstrating SQLite3 CRUD operations.
"""

import logging
from database import Database
from crud import UserCRUD, TaskCRUD

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main application function."""
    # Initialize database
    db = Database('tasks.db')
    db.initialize()

    # Create CRUD instances
    user_crud = UserCRUD(db)
    task_crud = TaskCRUD(db)

    try:
        # Create users
        print("\n=== Creating Users ===")
        user1_id = user_crud.create('Alice Johnson', 'alice@example.com')
        print(f"Created user: {user1_id}")

        user2_id = user_crud.create('Bob Smith', 'bob@example.com')
        print(f"Created user: {user2_id}")

        user3_id = user_crud.create('Carol White', 'carol@example.com')
        print(f"Created user: {user3_id}")

        # Read users
        print("\n=== Reading Users ===")
        user = user_crud.read(user1_id)
        print(f"Retrieved user: {user}")

        all_users = user_crud.read_all()
        print(f"Total users: {len(all_users)}")
        for u in all_users:
            print(f"  - {u}")

        # Create tasks
        print("\n=== Creating Tasks ===")
        task1_id = task_crud.create(
            'Complete project proposal',
            'Finish the quarterly project proposal',
            user1_id
        )
        print(f"Created task: {task1_id}")

        task2_id = task_crud.create(
            'Review code',
            'Review pull requests from team members',
            user1_id
        )
        print(f"Created task: {task2_id}")

        task3_id = task_crud.create(
            'Update documentation',
            'Update API documentation',
            user2_id
        )
        print(f"Created task: {task3_id}")

        # Read tasks
        print("\n=== Reading Tasks ===")
        task = task_crud.read(task1_id)
        print(f"Retrieved task: {task}")

        all_tasks = task_crud.read_all()
        print(f"Total tasks: {len(all_tasks)}")
        for t in all_tasks:
            print(f"  - {t.title}: {t.status}")

        # Read tasks by user
        print(f"\n=== Tasks for User {user1_id} (Alice) ===")
        user_tasks = task_crud.read_by_user(user1_id)
        print(f"User has {len(user_tasks)} tasks:")
        for t in user_tasks:
            print(f"  - {t.title}: {t.status}")

        # Update task status
        print("\n=== Updating Task Status ===")
        task_crud.update_status(task1_id, 'in_progress')
        updated_task = task_crud.read(task1_id)
        print(f"Updated task: {updated_task}")

        # Update user
        print("\n=== Updating User ===")
        user_crud.update(user3_id, 'Carol Green', 'carol.green@example.com')
        updated_user = user_crud.read(user3_id)
        print(f"Updated user: {updated_user}")

        # Delete a task
        print("\n=== Deleting Task ===")
        task_crud.delete(task3_id)
        print(f"Deleted task {task3_id}")

        remaining_tasks = task_crud.read_all()
        print(f"Remaining tasks: {len(remaining_tasks)}")

        # Display final summary
        print("\n=== Final Summary ===")
        print(f"Total users: {len(user_crud.read_all())}")
        print(f"Total tasks: {len(task_crud.read_all())}")

    except Exception as e:
        logger.error(f"Application error: {e}")
    finally:
        db.close()
        print("\nApplication completed successfully!")


if __name__ == '__main__':
    main()
