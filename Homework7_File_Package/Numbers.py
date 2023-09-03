# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1001


def file_adding(file_name: str, count_line: int) -> None:
    with open(f'{file_name}.txt', 'a',  encoding='utf-8') as f:
        for _ in range(count_line + 1):
            f.write(str(randint(MIN_NUM, MAX_NUM)) + '|' + str(uniform(MIN_NUM, MAX_NUM)) + '\n')


if __name__ == '__main__':
    file_adding('task1.txt', 5)