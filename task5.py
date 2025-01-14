# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_path(file_path):
    # Извлекаем путь к файлу, имя файла и расширение
    directory = os.path.dirname(file_path)  # Путь к файлу
    filename = os.path.basename(file_path)  # Имя файла с расширением
    name, extension = os.path.splitext(filename)  # Разделяем имя и расширение
    
    return (directory, name, extension)

# Пример использования
file_path = "/home/user/documents/file.txt"
print(split_path(file_path))


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем 
# словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка 
# умноженная на процент премии

names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 2000]
bonuses = ["10%", "15%", "20%"]

bonus_dict = {name: rate * (float(bonus.strip('%')) / 100) for name, rate, bonus in zip(names, rates, bonuses)}

print(bonus_dict)

# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
gen = fibonacci_generator()
for _ in range(10):  # Выведем первые 10 чисел Фибоначчи
    print(next(gen))


# или

def fibonacci_list(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

# Пример использования
n = 10  # Число чисел Фибоначчи, которые нужно вывести
print(fibonacci_list(n))
