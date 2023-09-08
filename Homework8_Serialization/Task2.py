# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json


def is_uniq(data: dict, our_id: str) -> bool:
    for item in data.values():
        if our_id in item.keys():
            return False
    return True


def person_identification(input_file: str) -> None:
    while True:
        name = input('Введите имя: ')
        input_id = (input('Введите id: '))
        level_access = (input('Введите уровень доступа: '))

        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                read_dict: dict = json.load(f)
        except FileNotFoundError:
            read_dict: dict = {str(i): {} for i in range(1, 8)}

        if is_uniq(read_dict, input_id):
            read_dict[level_access].update({id: name})
        else:
            continue

        with open(input_file, 'w', encoding='utf-8') as res:
            json.dump(read_dict, res, indent=4)


if __name__ == '__main__':
    person_identification('res_for_task2.json')