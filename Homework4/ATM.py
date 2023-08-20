# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

MODES = """Выберете действие:
1 - пополнить счет
2 - снять со счета
3 - вывести список операций
4 - выйти из программы"""
MAX_LIMIT = 5_000_000
QUALITY_NUM = 50
ADDITIONAL_PERCENT = 1.03
UNPROFITABLE_PERCENT = 0.015
LUXURY_PERCENT = 0.9
COUNT_FOR_BONUS = 3
MIN_OUTCOME = 30
MAX_OUTCOME = 600

balance = 0
count_of_process = 0
information_list = []

def choise_operation():
    return input(f'{MODES}:\n')


def compulsory_checks(money: int, count: int):
    if money > MAX_LIMIT:
        money = money * LUXURY_PERCENT
        print("Начислен налог на богатство")
        print(f'Ваш баланс составляет {money} y.e. на данный момент')

    if count % COUNT_FOR_BONUS == 0 and count >= COUNT_FOR_BONUS:
        money = money * ADDITIONAL_PERCENT
        print("Начислены проценты за количество операций.")
        print(f'Ваш баланс составляет {money} y.e. на данный момент')
    return money


def write_information(line: str, inf_list: list[str]):
    inf_list.append(line)


def calculating_comission(cash: int):
    bank_comission = cash * UNPROFITABLE_PERCENT
    if bank_comission >= MAX_OUTCOME:
        bank_comission = MAX_OUTCOME
    if bank_comission <= MIN_OUTCOME:
        bank_comission = MIN_OUTCOME
    return bank_comission


while True:

    choise = choise_operation()

    balance = compulsory_checks(balance, count_of_process)

    if choise == '1':
        income = int(input("Введите сумму пополнения: "))
        if income % QUALITY_NUM == 0:
            balance += income
            write_information(f'Поступило {income} средств на баланс', information_list)
        else:
            print("Сумма пополнения должна быть кратна 50. Попробуйте еще раз!")
        count_of_process += 1

    elif choise == '2':
        outcome = int(input("Введите сумму для снятия: "))
        if outcome % QUALITY_NUM == 0 and outcome <= balance:
            comission = calculating_comission(outcome)
            balance -= comission
            balance -= outcome
            write_information(f'Снято {income} средств с баланса', information_list)
        else:
            print("Сумма снятия должна быть кратна 50 или Вы хотите снять больше,Чем у Вас есть. Попробуйте еще раз!")
        count_of_process += 1
    elif choise == '3':
        print(f"{information_list}")
    elif choise == '4':
        print(f"Вы успешно вышли из программы.")
        break
    else:
        print('Введен номер несуществующей операции! Повторите еще раз!!!')
    print(f'Ваш баланс составляет {balance} y.e. на данный момент')
print(f'Ваш баланс составляет {balance} y.e. на данный момент')