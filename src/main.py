from models import Task
from utils import get_task_status


def main():
    task = Task("Изучить Git", "Выполнить лабораторную работу")

    print(f"Задача: {task.title}")
    print(f"Описание: {task.description}")
    print(f"Статус: {get_task_status(task)}")

    task.complete()

    print(f"Статус после выполнения: {get_task_status(task)}")


if __name__ == "__main__":
    main()
