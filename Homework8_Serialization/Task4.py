# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import json


def csv_to_json(input_filename: str,
                output_filename: str) -> None:
    with open(f'{input_filename}.csv', 'r', newline='') as f_csv:
        data = f_csv.read().split('\n')

    res: list = []
    data.pop()

    for value in data[1:]:
        level, name, our_id = value[:-1].split(',')
        res.append({'id': f'{int(our_id):06}',
                    'level': level,
                    'name': name,
                    'hash': hash(our_id+name)})

    with open(f'{output_filename}.json', 'w', encoding='utf-8') as f_json:
        json.dump(res, f_json, indent=4)


if __name__ == "__main__":
    csv_to_json('res_for_task2_3', 'res_for_task4')