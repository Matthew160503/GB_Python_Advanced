__all_stock_cost = {}


def calculate_portfolio_value(stock: dict, price: dict) -> float:
    """
    Расчет общей стоимости портфеля акций:
    """
    total_share_price = 0
    for key1, value1 in stock.items():
        for key2, value2 in price.items():
            if key1 == key2:
                __all_stock_cost[key1] = value1 * value2
                total_share_price += value1 * value2
    return total_share_price


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    """
    Расчет доходности портфеля
    """
    return (current_value/initial_value - 1) * 100


def get_most_profitable_stock(stock: dict, price: dict) -> str:
    """
    Определение наиболее прибыльной акции
    """
    temp = {}
    for key1, value1 in stock.items():
        for key2, value2 in price.items():
            if key1 == key2:
                current_cost = value1 * value2
                temp[key1] = current_cost - __all_stock_cost[key1]

    for key, value in temp.items():
        if value == max(temp.values()):
            return key


if __name__ == "__main__":
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    print(calculate_portfolio_value(stocks, prices))
    i_val = 20000
    c_val = 15000
    print(calculate_portfolio_return(i_val, c_val))
    stocks2 = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    print(get_most_profitable_stock(stocks2, prices2))