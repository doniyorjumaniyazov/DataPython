import requests
from datetime import date

# Ваши актуальные CLIENT_ID и CLIENT_SECRET для Foursquare API V3
CLIENT_ID = ''
CLIENT_SECRET = ''

# Новый эндпоинт для API V3 (замените URL на актуальный)
BASE_URL = "https://api.foursquare.com/v3/places/search"

# Получаем текущую дату для версии API
current_date = date.today().strftime('%Y%m%d')

def search_venues(category="cinema", location="Москва", limit=5):
    # Проверим правильность параметров
    print("Параметры запроса:")
    print(f"Client ID: {CLIENT_ID}")
    print(f"Client Secret: {CLIENT_SECRET}")
    print(f"Версия API: {current_date}")
    print(f"Категория: {category}")
    print(f"Местоположение: {location}")
    print(f"Лимит: {limit}")
    
    # Параметры запроса
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'near': location,   # Местоположение
        'query': category,  # Категория или ключевое слово
        'limit': limit,     # Лимит на количество результатов
    }

    headers = {
        'Authorization': f'Bearer {CLIENT_SECRET}'  # В случае использования нового формата авторизации
    }

    # Отправка GET-запроса
    response = requests.get(BASE_URL, params=params, headers=headers)

    # Проверка на ошибку 400
    if response.status_code == 400:
        print("Ошибка 400: Некорректный запрос.")
        print(f"Ответ от API: {response.text}")
        return

    if response.status_code == 200:
        data = response.json()
        venues = data['response']['venues']

        if not venues:
            print("Заведения не найдены.")
            return

        for venue in venues:
            name = venue['name']
            address = venue['location'].get('address', 'Адрес не указан')
            rating = venue.get('rating', 'Не оценено')

            print(f"Название: {name}")
            print(f"Адрес: {address}")
            print(f"Рейтинг: {rating}")
            print("-" * 40)
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
        print(f"Ответ от API: {response.text}")

# Пример поиска музеев
search_venues("cinema", location="Moscow")
