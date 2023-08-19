# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX_DICT = {10: 'A', 11: 'B', 12:  'C', 13: 'D', 14: 'E', 15: 'F'}
HEX_NUM = 16

num = 18990
check_num = num
res = ''

while num > 0:
    temp = num % HEX_NUM
    if temp > 9:
        res += HEX_DICT[temp]
    else:
        res += str(num % HEX_NUM)
    num //= HEX_NUM

res = res[::-1]
print(res, hex(check_num))
