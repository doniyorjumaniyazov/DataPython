import os

def rename_files(directory, final_name, num_digits, input_extension, output_extension, name_range):
    """
    Функция для группового переименования файлов в указанном каталоге.
    """
    try:
        # Проверяем, существует ли каталог
        if not os.path.exists(directory):
            raise ValueError(f"Каталог {directory} не существует.")
        
        # Получаем список файлов в каталоге
        files = os.listdir(directory)
        if not files:
            raise ValueError(f"В каталоге {directory} нет файлов.")
        
        # Отфильтровываем файлы с нужным расширением
        files_to_rename = [f for f in files if f.endswith(input_extension)]
        if not files_to_rename:
            raise ValueError(f"Нет файлов с расширением {input_extension} в каталоге {directory}.")
        
        # Переименовываем каждый файл
        for idx, filename in enumerate(files_to_rename, 1):
            # Получаем часть имени согласно диапазону
            base_name = filename.split('.')[0]  # Берем имя файла без расширения
            name_part = base_name[name_range[0]-1:name_range[1]]  # Индексы начинаются с 1, поэтому -1
            
            # Формируем новое имя с учетом счетчика и расширения
            new_filename = f"{name_part}{final_name}{str(idx).zfill(num_digits)}.{output_extension}"
            
            # Путь к старому и новому файлу
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Переименовываем файл
            os.rename(old_file_path, new_file_path)
            print(f"Переименован файл: {filename} -> {new_filename}")
    
    except Exception as e:
        print(f"Ошибка: {e}")

# Пример вызова функции
rename_files(
    directory='./my_folder',   # Путь к каталогу с файлами
    final_name='_last',       # Желаемое окончательное имя файлов
    num_digits=2,              # Количество цифр в порядковом номере
    input_extension='txt',     # Расширение исходных файлов
    output_extension='md',    # Расширение конечных файлов
    name_range=[3, 6]          # Диапазон индексов для части имени файла
)

