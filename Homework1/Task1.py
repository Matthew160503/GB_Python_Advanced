def process():
    a = int(input("Введите длину 1-ой стороны треугольника: "))
    b = int(input("Введите длину 2-ой стороны треугольника: "))
    c = int(input("Введите длину 3-ой стороны треугольника: "))

    if a + b <= c or a + c <= b or b + c <= a and a > 0 and b > 0 and c > 0:
        print(f"Треугольника со сторонами {a}, {b}, {c} не существует")
    else:
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")