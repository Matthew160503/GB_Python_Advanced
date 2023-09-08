# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def csv_format(filename: str):
    with open(f'{filename}.json', 'r', encoding='utf-8') as f_input:
        data = json.load(f_input)
    rows = []
    for level, users in data.items():
        for our_id, name in users.items():
            rows.append({'level': level,
                        'name': name,
                        'id': our_id})

    with open(f'{filename}_3.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames=['level', 'name', 'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    csv_format('res_for_task2')

