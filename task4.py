# Напишите функцию для транспонирования матрицы

def transpone(matrix):
    transpone_matrix = []
    
    for i in range(len(matrix[0])): # по столбцам
        row = []
        for j in range(len(matrix)): # по строкам
            row.append(matrix[j][i])
        transpone_matrix.append(row)  # обратный матрица
            
    return transpone_matrix
    
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]   

new_matrix = transpone(matrix)
print(new_matrix) 
            
            
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.  

def create_dict(**kwargs):
    result = {}
    
    for key, value in kwargs.items():
        try:
            # Попробуем получить хешируемость значения
            result[hash(value)] = key
        except TypeError:
            # Если значение не хешируемо, используем строковое представление
            result[str(value)] = key
    
    return result

# Пример использования функции:
new_dict = create_dict(a=5, b=[1, 2], c="Hello")
print(new_dict)


# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
             

# Глобальная переменная для хранения текущего баланса
current_balance = 0
# Список для хранения истории операций
operation_history = []

# Функция пополнения счета
def deposit_balance(amount):
    global current_balance
    current_balance += amount
    operation_history.append(f"Пополнение: {amount} рублей")
    print(f"Баланс  пополненно: {amount} рублей")
    print(f"Баланс после пополнения: {current_balance} рублей")

# Функция снятия средств
def withdraw_balance(amount):
    global current_balance
    if amount > current_balance:
        print("Недостаточно средств!")
    else:
        current_balance -= amount
        operation_history.append(f"Снятие: {amount} рублей")
        print(f"Cнятия cредств: {amount} рублей")
        print(f"Баланс после снятия: {current_balance} рублей")

# Функция проверки баланса
def checking_balance():
    print(f"Текущий баланс: {current_balance} рублей")

# Функция для вывода истории операций
def history_balance():
    print("История операций:")
    if not operation_history:
        print("История пуста.")
    else:
        for operation in operation_history:
            print(operation)

# Пример работы с банкоматом
deposit_balance(500)      # Пополнение на 500
withdraw_balance(200)     # Снятие 200
checking_balance()        # Проверка баланса
history_balance()         # Вывод истории
withdraw_balance(1000)    # Попытка снять больше, чем на счете

    
        
    
    