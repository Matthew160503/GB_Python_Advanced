def duplicate_elems(our_list):
    """Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно
    быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
    """
    res = []
    for el in our_list:
        if our_list.count(el) > 1 and el not in res:
            res.append(el)
    return  res