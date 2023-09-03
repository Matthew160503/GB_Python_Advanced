# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих
#   файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os


def changing_group_name(wanted_name: str,
                        count_nums: int,
                        extension_old: str,
                        extension_new: str,
                        diapazon: list[int],
                        our_path: str = '.') -> None:
    count = 1

    for filename in os.listdir(our_path):
        if filename.endswith(extension_old):
            last_name = os.path.splitext(filename)[0]
            last_name = last_name[diapazon[0]:diapazon[1] + 1] if diapazon else ''
            new_name = f'{last_name}{wanted_name}{str(count).zfill(count_nums)}{extension_new}'
            count += 1
            os.rename(os.path.join(our_path, filename), os.path.join(our_path, new_name))


if __name__ == '__main__':
    changing_group_name('task', 3, '.txt', '.md', [1, 3])