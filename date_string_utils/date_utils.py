from datetime import datetime


def get_current_date():
    return datetime.now().strftime("%d.%m.%Y")


def format_date(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.strftime("%d.%m.%Y")


def get_year(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    return date.year
