import math
import fractions

a = input("Введите дробь через /: ")
b = input("Введите вторую дробь через /: ")


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def fractions_summ(x, y):
    list_a = x.split('/')
    list_b = y.split('/')

    lcm_nums = lcm(int(list_a[1]), int(list_b[1]))

    summ = str(int(lcm_nums / int(list_a[1])) * int(list_a[0]) + int(lcm_nums /
               int(list_b[1])) * int(list_b[0])) + '/' + str(lcm_nums)

    list_summ = summ.split('/')

    temp = math.gcd(int(list_summ[0]), int(list_summ[1]))

    if temp != 1:
        list_summ[0] = str(int(int(list_summ[0]) / temp))
        list_summ[1] = str(int(int(list_summ[1]) / temp))
        summ = list_summ[0] + '/' + list_summ[1]

    return summ