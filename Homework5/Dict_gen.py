# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем
# в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

import decimal


def premium_calculation(names: list[str], rates: list[int], premiums: list[str]) -> dict[str, decimal]:
    return {name: salary * (decimal.Decimal(premium.strip("%")) / 100)
            for name, salary, premium in zip(names, rates, premiums)}


employee = ['Matthew', 'Andrew', 'Kate']
rate = [4500, 900, 1500]
bonus = ['70.79', '50.83', '65.39']

print(premium_calculation(employee, rate, bonus))