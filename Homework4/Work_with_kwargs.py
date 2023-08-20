# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ —
# значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление. Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if type(value) == list or set or dict or bytearray:
            result_dict[str(value)] = key
        else:
            result_dict[value] = key
    return result_dict


print(create_dict(res=12, reverse=[1, 2, 3]))