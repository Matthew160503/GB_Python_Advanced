# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint


def give_aliases() -> str:
    name: str = ''
    for _ in range(randint(4,7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def file_adding(file_name: str, count_line: int) -> None:
    with open(f'{file_name}.txt', 'a',  encoding='utf-8') as f:
        for _ in range(count_line + 1):
            f.write(f'{give_aliases()}\n')


if __name__ == '__main__':
    file_adding('task2.txt', 5)