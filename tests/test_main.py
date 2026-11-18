import sys
from pathlib import Path
import unittest

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from models import Task
from utils import get_task_status


class TestTask(unittest.TestCase):

    def test_create_task(self):
        task = Task("Тестовая задача")

        self.assertEqual(task.title, "Тестовая задача")
        self.assertFalse(task.completed)

    def test_complete_task(self):
        task = Task("Тестовая задача")
        task.complete()

        self.assertTrue(task.completed)

    def test_task_status(self):
        task = Task("Тестовая задача")

        self.assertEqual(
            get_task_status(task),
            "Не выполнена"
        )

        task.complete()

        self.assertEqual(
            get_task_status(task),
            "Выполнена"
        )


if __name__ == "__main__":
    unittest.main()
