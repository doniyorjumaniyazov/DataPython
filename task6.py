# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# import sys
# from datetime import datetime

# def validate_date(str_data):
#     try:
#         data_obj = datetime.strptime(str_data, '%Y-%m-%d')
#         print(f"дата {str_data} валиданно!")
#     except:
#         print(f"неверный формат {str_data}")
        
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("исползовай: например <дата>")
#         sys.exit(1)
        
#     input_data = sys.argv[1]
#     validate_date(input_data)  
    

#  Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, 
#  решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, 
#  чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
#  есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, 
#  каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.  

# def is_safe(queens_positions):
#     # Списки для отслеживания горизонталей, вертикалей и диагоналей
#     rows = set()
#     cols = set()
#     main_diagonals = set()  # x - y
#     anti_diagonals = set()  # x + y
    
#     for x, y in queens_positions:
#         # Проверяем горизонталь (строку)
#         if x in rows:
#             return False
#         rows.add(x)
        
#         # Проверяем вертикаль (столбец)
#         if y in cols:
#             return False
#         cols.add(y)
        
#         # Проверяем главную диагональ (x - y)
#         if (x - y) in main_diagonals:
#             return False
#         main_diagonals.add(x - y)
        
#         # Проверяем побочную диагональ (x + y)
#         if (x + y) in anti_diagonals:
#             return False
#         anti_diagonals.add(x + y)
    
#     return True


# # Вводим координаты 8 ферзей
# queens_positions = []
# for _ in range(8):
#     x, y = map(int, input("Введите координаты ферзя (x, y): ").split())
#     queens_positions.append((x, y))

# # Проверяем, бьют ли ферзи друг друга
# if is_safe(queens_positions):
#     print("Истина: Ферзи не бьют друг друга.")
# else:
#     print("Ложь: Ферзи бьют друг друга.")
    
    
# Напишите функцию в шахматный модуль. Используйте генератор случайных 
# чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные 
# варианты и выведите 4 успешных расстановки.

import random

def is_safe(queens_positions):
    # Списки для отслеживания горизонталей, вертикалей и диагоналей
    rows = set()
    cols = set()
    main_diagonals = set()  # x - y
    anti_diagonals = set()  # x + y
    
    for x, y in queens_positions:
        # Проверяем горизонталь (строку)
        if x in rows:
            return False
        rows.add(x)
        
        # Проверяем вертикаль (столбец)
        if y in cols:
            return False
        cols.add(y)
        
        # Проверяем главную диагональ (x - y)
        if (x - y) in main_diagonals:
            return False
        main_diagonals.add(x - y)
        
        # Проверяем побочную диагональ (x + y)
        if (x + y) in anti_diagonals:
            return False
        anti_diagonals.add(x + y)
    
    return True

def generate_random_queens():
    # Генерируем случайную расстановку ферзей на доске 8x8
    return [(i+1, random.randint(1, 8)) for i in range(8)]

def find_successful_arrangements(num_successes=4):
    successful_arrangements = []
    while len(successful_arrangements) < num_successes:
        queens_positions = generate_random_queens()
        if is_safe(queens_positions):
            successful_arrangements.append(queens_positions)
    return successful_arrangements

# Находим 4 успешные расстановки ферзей
successful_arrangements = find_successful_arrangements()

# Выводим 4 успешные расстановки
for idx, arrangement in enumerate(successful_arrangements, start=1):
    print(f"Успешная расстановка {idx}: {arrangement}")
