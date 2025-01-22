import os
import json
import csv
import pickle

def get_directory_info(directory):
    """
    Функция для рекурсивного обхода директории и сбора информации о файлах и папках.
    """
    directory_info = []

    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = get_directory_size(dir_path)
            directory_info.append({
                'name': dir_name,
                'type': 'directory',
                'parent': root,
                'size': dir_size
            })

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            directory_info.append({
                'name': file_name,
                'type': 'file',
                'parent': root,
                'size': file_size
            })

    return directory_info

def get_directory_size(directory):
    """
    Функция для вычисления общего размера всех файлов в директории.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def save_as_json(data, filename):
    """Сохраняет данные в файл JSON."""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_as_csv(data, filename):
    """Сохраняет данные в файл CSV."""
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['name', 'type', 'parent', 'size'])
        writer.writeheader()
        writer.writerows(data)

def save_as_pickle(data, filename):
    """Сохраняет данные в файл Pickle."""
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
