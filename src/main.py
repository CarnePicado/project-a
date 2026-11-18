from datetime import datetime

from models import Task
from utils import get_task_status
from date_string_utils import get_current_date, format_date


def main():
    task = Task("Изучить Git", "Выполнить лабораторную работу")

    print(f"Задача: {task.title}")
    print(f"Описание: {task.description}")
    print(f"Статус: {get_task_status(task)}")

    task.complete()

    print(f"Статус после выполнения: {get_task_status(task)}")
    print(f"Текущая дата: {get_current_date()}")

    date_string = datetime.now().strftime("%Y-%m-%d")
    print(f"Дата в формате ДД.ММ.ГГГГ: {format_date(date_string)}")


if __name__ == "__main__":
    main()
