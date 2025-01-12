#  Напишите программу, которая получает целое число и возвращает его шестнадцатеричное 
#  строковое представление. Функцию hex используйте для проверки своего результата.

# простой вид

num = int(input("введите целое число: "))

res = hex(num)[2:]
print(res)

# 

def to_hex(n):
    str_hex = hex(n)[2:]
    return str_hex

n = int(input("введите целое число: "))

result = to_hex(n)

print(f'шестнадцатеричное вид: {result}')

print(f'проверка резултатов: {hex(n)[2:]}')

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions


from fractions import Fraction

def to_frac():
    # Ввод двух дробей
    frac1 = input("Введите первую дробь в формате a/b: ")
    frac2 = input("Введите вторую дробь в формате a/b: ")
    
    # Преобразуем строковые представления в объекты Fraction
    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)
    
    # Считаем сумму и произведение дробей
    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2
    
    return sum_result, product_result

# Вызов функции для получения суммы и произведения дробей
sum_result, product_result = to_frac()

# Выводим результаты
print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")



