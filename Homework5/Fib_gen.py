# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*fibonacci(10))
