# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def delete_last_s_():
    vars_dict = {}
    for i in filter(lambda x: x.endswith('s'), globals().keys()):
        if len(i) > 1:
            vars_dict[i[:len(i) - 1]] = globals()[i]
            globals()[i] = None
    for j in vars_dict:
        globals().setdefault(j, vars_dict[j])   
    
names = 1
s = 5
args = [1, 2, 3]

delete_last_s_()
print(globals())


