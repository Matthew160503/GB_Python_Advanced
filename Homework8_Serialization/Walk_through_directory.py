# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
# обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
# директорий.
import csv
import json
import os
import pickle


def get_size(our_path: str) -> int:
    size = 0
    for adress, dirs, names in os.walk(our_path):
        for file in names:
            size += os.path.getsize(os.path.join(adress, file))
    return size


def directory_description(dir_name: str):
    res = []
    for adress, dirs, files in os.walk(dir_name):
        for name in files:
            full_path = os.path.join(adress, name)
            res.append({'name': name,
                        'parent': adress,
                        'type': 'file',
                        'size': os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(adress, name)
            res.append({'name': name,
                        'parent': adress,
                        'type': 'directory',
                        'size': get_size(full_path)})

    with open('task1_json_file.json', 'w', encoding='utf-8') as f_json:
        json.dump(res, f_json, indent=4)

    with open('task1_csv_file.csv', 'w', encoding='utf-8', newline='') as f_csv:
        csv_write = csv.DictWriter(f_csv, fieldnames=['name', 'parent',
                                                      'type', 'size'])
        csv_write.writeheader()
        csv_write.writerows(res)

    with open('task1_pickle_file.pickle', 'wb') as f_pickle:
        pickle.dump(res, f_pickle)


if __name__ == '__main__':
    directory_description('example_to_walk_dir')
