# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка

def get_sum_between_indexes(array: list[int], index_1: int, index_2: int) ->int:
    
    sum_between = 0

    if index_1 > len(array):
        index_1 = len(array)
    elif -len(array) <= index_1 < 0:
        index_1 += len(array)   
    elif index_1 < -len(array):
        index_1 = 0
        sum_between += array[0]
 
    if index_2 > len(array):
        index_2 = len(array)
    elif -len(array) <= index_2 < 0:
        index_2 += len(array)        
    elif index_2 < -len(array):
        index_2 = 0
        sum_between += array[0]

    if index_1 == index_2:
        return sum_between
    else:
        if index_1 < index_2:
            for i in range(index_1 + 1, index_2):
                sum_between += array[i]
            return sum_between
        elif index_1 > index_2:
            for i in range(index_2 + 1, index_1):
                sum_between += array[i]
            return sum_between
            
array = [1, 2, 3, 4, 5, 6, 7]               
print(get_sum_between_indexes(array, 5, -5))
