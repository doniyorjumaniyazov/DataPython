# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

 def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)
input_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
result = find_duplicates(input_list)
print(result)

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку

import string
from collections import Counter

def get_most_common_words(text, top_n=10):
    # Приводим текст к нижнему регистру
    text = text.lower()
    
    # Убираем знаки препинания
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Разбиваем текст на слова
    words = text.split()
    
    # Подсчитываем частоту каждого слова
    word_counts = Counter(words)
    
    # Возвращаем топ N самых частых слов
    return word_counts.most_common(top_n)

# Пример текста из статьи на Википедии о Python
text = """
Python — это высокоуровневый язык программирования общего назначения. 
Он был создан в конце 1980-х годов Гвидо ван Россумом и выпущен в 1991 году. 
Python имеет динамическую типизацию и автоматическое управление памятью. 
Его философия включает в себя такие принципы, как простота и читаемость кода.
"""

# Получаем 10 самых частых слов
top_words = get_most_common_words(text, top_n=10)

# Выводим результат
print(top_words)

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

import itertools

# Словарь с вещами и их массой
things = {
    "палатка": 2.5,
    "спальный мешок": 1.5,
    "фляга": 1.0,
    "картография": 0.2,
    "питьевая вода": 3.0,
    "кастрюля": 1.2,
    "фонарь": 0.5
}

def find_combinations(things, max_weight):
    # Все возможные комбинации вещей
    possible_combinations = []
    
    # Перебираем все возможные размеры комбинаций (от 1 до количества всех вещей)
    for r in range(1, len(things) + 1):
        for combination in itertools.combinations(things.items(), r):
            total_weight = sum(item[1] for item in combination)
            
            # Если комбинация влезает в рюкзак, добавляем её
            if total_weight <= max_weight:
                possible_combinations.append(combination)
    
    return possible_combinations

# Максимальная грузоподъёмность рюкзака
max_weight = 5.0

# Получаем все возможные варианты комплектации рюкзака
combinations = find_combinations(things, max_weight)

# Выводим все возможные варианты
for combination in combinations:
    items = [item[0] for item in combination]
    total_weight = sum(item[1] for item in combination)
    print(f"Вещи: {items}, Общий вес: {total_weight} кг")

