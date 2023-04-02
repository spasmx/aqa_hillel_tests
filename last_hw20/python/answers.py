import json
import os
import platform

#4
# створити Dict такого вигляду:
# {'one': '1', 'two': '2', 'three': '3'}
# та максимально коротким записом в коді поміняти місцями ключі та значення.

hw_dict = {'one': '1', 'two': '2', 'three': '3'}
new_hw_dict = {v: k for k, v in hw_dict.items()}

#5
# У файлі answers.py створити функцію, яка запише результат виконання коду з п.4 у новий файл anwsers.txt


def write_dict_in_file(data_dict: dict):
    with open('answers.txt', 'w') as f:
        json.dump(data_dict, f)
    return f

#write_dict_in_file(new_hw_dict)

#6
# Створити файл test.txt; у файлі answers.py створити функцію, яка перейменує файл test.txt в залежності від того,
# яка у вас операційна система


def rename_file_os():
    with open('test.txt', 'w') as f:
        f.write('It\'s test file')
    system = platform.uname().system
    new_name = ''
    if system == 'Windows':
        new_name = 'windows.txt'
    elif system == 'Linux':
        new_name = 'linux.txt'
    elif system == 'Darwin':
        new_name = 'mac.txt'
    else:
        print('Unknown OS')
    os.rename(f.name, new_name)

#rename_file_os()

# 7
# Створити генератор, який буде інкрементувати число з кроком 1, починаючи з числа, яке передається як перший аргумент.
# Зупиняти своє виконання у випадку, якщо буде досягнуто значення, передане другим аргументом, незалежно від знаку


def numeric_generator(start: int, end: int):
    if start > end:
        for i in range(start, end - 1, -1):
            yield i
    for i in range(start, end + 1, 1):
        yield i

# x = numeric_generator(1, -5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

#8
# Створти 3 класи: A, B, C. Клас B віднаслідувати від A; C - від B.
# В кожному з класів має бути поле name з унікальним для цього класу значенням. Наприклад 'A', 'B' або 'C'.
# * При зверненні до полів класу (не творюючи екземпляр), має друкуватись відповідний name
# * При створенні екземпляру класу C, має бути надруковано в консоль значення поля name з класу A. Використовувати super.


class A:
    name = 'name_A'

    def __init__(self):
        self.name = A.name


class B(A):
    name = 'name_B'

    def __init__(self):
        super().__init__()


class C(B):
    name = 'name_C'

    def __init__(self):
        super().__init__()



# print(A.name)
# print(B.name)
# print(C.name)
# c = C()
# print(c.name)



#9
# показати приклади використання args та kwargs
# args

def my_func_args(*args):
    for arg in args:
        print(arg)


# print(my_func_args(1, 2, 3))
# print(my_func_args('a', 'b', 'c', 'd'))
# print(my_func_args(1, 2, 3, 'a', 'b', 'c', 'd'))

#kwargs

def my_func_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')


# print(my_func_kwargs(a=1, b=2, c=3))
# print(my_func_kwargs(a=1, b=2, c=3, name='Bob', country='Ukraine'))

# args+kwargs

def my_func_combo(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


#print(my_func_combo(1, 2, 'a', name='Bob', country='Ukraine'))


#10
# написати функцію, яка буде відкривати json файл та змінювати в ньому обране поле (значення)

def update_json(file: str, field_name: str, new_value):
    with open(file) as f:
        data_json = json.load(f)

    data_json[field_name] = new_value

    with open(file, 'w') as f:
        json.dump(data_json, f, indent=4)


#update_json('json_for_example.json', 'age', 20)
