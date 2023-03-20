# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def get_profit_loss(companies: dict[str:list[int]]) -> dict[str:int] and bool:
    result_dict = {}
    profit = True
    for i in companies:
        companie_profit = sum(companies[i])
        result_dict[i] = companie_profit
        if companie_profit < 0:
            profit = False
    return result_dict, profit        

companies_dict = {'Mercedes':[20, -3, 4, -10, 8], 'BMW':[25, -14, 6, 4, 2], 'Audi':[18, -4, -9, 1, -10]}
print(get_profit_loss(companies_dict))