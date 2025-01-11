import requests

# API-ключ
api_key = 'LUPEQPM1JU3NIALZSDFLKBJQ2ANXDV1ZIX5EWX3HR4POKVNO'  

# URL для запроса
url = 'https://api.foursquare.com/v3/places/search?query=coffee&near=Moscow&limit=10'

# Заголовки с авторизацией
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Выполнение GET-запроса
response = requests.get(url, headers=headers)

# Проверка успешности запроса
if response.status_code == 200:
    data = response.json()
    for venue in data['results']:
        print(venue['name'], venue['location']['address'])
else:
    print(f"Ошибка: {response.status_code}")
