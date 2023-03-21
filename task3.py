# ✔ Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def change_keys_values(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if str(type(value)) not in ["<class 'list'>", "<class 'dict'>", "<class 'set'>"]:
            result_dict[value] = key
        else:
            result_dict[str(value)] = key
    return result_dict

print(change_keys_values(понедельник=[10], вторник=8, среда=0, четверг=9))            
