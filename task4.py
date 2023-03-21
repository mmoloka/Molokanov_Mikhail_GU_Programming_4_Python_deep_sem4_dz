''' Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список:
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег '''

WITHDRAWAL_INTEREST = 0.015
ACCRUED_INTEREST = 0.03
LOWER_BOUND, UPPER_BOUND = 30, 600
MAX_SUM = 5_000_000
WEALTH_TAX_INTEREST = 0.1
MULTIPLE = 50

sum_ = 0
operations_count = 0
operations_sum_list = []
exit_flag = False

def withdraw_cash(amount_cash: int) -> bool:
    global sum_
    global operations_count
    global operations_sum_list
    withdrawal_interest = amount_cash * WITHDRAWAL_INTEREST 

    if amount_cash > sum_:
        print('Недостаточно средств.')
    elif amount_cash % MULTIPLE == 0:
        if sum_ >= MAX_SUM:
            sum_ -= amount_cash * WEALTH_TAX_INTEREST
        operations_count += 1
        if multiple_3(operations_count):
            sum_ += amount_cash * ACCRUED_INTEREST
        if withdrawal_interest < 30:
            sum_ -= amount_cash + 30
        elif 30 <= withdrawal_interest <= 600:
            sum_ -= amount_cash + withdrawal_interest
        else:
            sum_ -= amount_cash + 600
        operations_sum_list.append(sum_)            
    else:
        print('Сумма должна быть кратна 50!')    
    return operations_sum_list 

def put_cash(amount_cash: int) -> list[float]:
    global sum_
    global operations_count
    global operations_sum_list
    initial_amount = amount_cash 

    if amount_cash % MULTIPLE == 0:
        if sum_ >= MAX_SUM:
            amount_cash *= (1 - WEALTH_TAX_INTEREST)
        sum_ += amount_cash
        operations_count += 1
        if multiple_3(operations_count):
            sum_ += initial_amount * ACCRUED_INTEREST
        operations_sum_list.append(sum_)
    else:
        print('Сумма должна быть кратна 50!')    
    return operations_sum_list    

def multiple_3(value: int) -> bool:
    if value % 3 == 0:
        return True
    else:
        return False       
            
def exit_() -> None:
    global exit_flag
    exit_flag = True

while not exit_flag:
    command = int(input('Нажмите: 1 - снять наличные \
                                  2 - внести наличные \
                                  3 - выйти'))
    match command:
        case 1:
            amount_cash = int(input('Введите сумму: '))
            withdraw_cash(amount_cash)
        case 2:
            amount_cash = int(input('Введите сумму: '))
            put_cash(amount_cash)
        case 3:
            exit_()        
print(operations_sum_list)
