import Task1

Task1.process()

number = int(input("Введите число от 0 до 100 тысяч: "))
MIN_VALUE = 0
MAX_VALUE = 100000
if number < MIN_VALUE or number > MAX_VALUE:
    print("Ввели число, которое выходит за диапазон")
else:
    if number == 1 or number == 0:
        print(f"Число {number} является ни составным, ни простым")
        exit()
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            print(f"Число {number} является составным")
            break
    if flag:
        print(f"Число {number} является простым")