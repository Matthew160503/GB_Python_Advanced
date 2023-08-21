# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из
# трёх элементов: путь, имя файла, расширение файла.
import os


def parse_path(file_name: str) -> tuple:
    path_file, extension = os.path.splitext(file_name)
    dirname, filename = os.path.split(path_file)
    return (dirname, filename, extension)


path_to_file = 'C:\Thecode\Media\статья.txt'

print(parse_path(path_to_file))