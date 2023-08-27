# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv


def _is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def valid_day(date: str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))
        if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
            days_in_month = [31, 28 + _is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return day <= days_in_month[month - 1]
        else:
            return False
    except ValueError:
        return False


if __name__ == '__main__':
    check_date = argv[1:2]
    print(valid_day(check_date[0]))