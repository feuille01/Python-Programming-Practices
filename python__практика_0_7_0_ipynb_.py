# -*- coding: utf-8 -*-
"""Python  "Практика 0.7.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yKtNS-_3KZsDuRxvC1A83_LrWPjdcjSi

Ссылка на материалы:  [пдф тут](https://drive.google.com/file/d/16Cm2tgrpuDH8eIdxdSYyOsfDPqnJ3byd/view?usp=sharing)

ФИО:
"""



"""## Задание 1. HTTP-запросы, ответы и погода

Описание:

Напишите HTTP-запрос для получения информации о погоде в введенном городе из API.

Можно использовать API: https://open-meteo.com/. Используйте метод GET.


Ввод
```
56.50, 60.35
```

Вывод
```
Сегодня (1.11) погода 20 ◦С, нет осадков, туман
```
"""

import requests
from datetime import datetime


# функция отправки запроса
def send_request(url):
    response = requests.get(url)

    status_code = response.status_code
    if status_code == 200:
        return response.json()
    return None

# функция очистки данных
def clear_data(data):
    # получение текущей даты
    current_date = datetime.today().date()
    current_date = f'{current_date.day}.{current_date.month}'

    # получение температуры
    temperature = data['current']['temperature_2m']
    temperature_format = data['current_units']['temperature_2m']

    # получение кода температуры
    weather_code = data['current']['weather_code']

    # определение погоды по коду
    if weather_code in [0, 1]:
        weather = 'нет осадков, ясно'
    elif weather_code == 45:
        weather = 'нет осадков, туман'
    elif weather_code in [61, 63, 65 ,71 ,73, 75]:
        weather = 'осадки, нет тумана'
    else:
        weather = 'выгляни в окно и посмотри сам'

    # формирование сообщения
    message = f'Сегодня ({current_date}) погода {temperature} {temperature_format}, {weather}'

    return message


# основная функция
def main():
    coordinates = input('Введите ваши координаты').split(', ')
    url = f'https://api.open-meteo.com/v1/forecast?latitude={coordinates[0]}&longitude={coordinates[1]}&current=temperature_2m,weather_code&forecast_days=1'
    data = send_request(url)
    message = clear_data(data)
    print(message)


main()

"""## Задание 2. HTTP-запросы, ответы и покемоны

**Описание:**


Создайте код программы, которая будет взаимодействовать с API, со следующим функионалом:

1. Используя метод GET, отправьте запрос на endpoint /pokemon, чтобы получить список первых 20 покемонов

2. Извлеките имена покемонов из ответа и выведите их списком

3. Введите с помощью input() название одного из покемонов


```
Имя покемона: clefairy
```



4. Отправьте GET-запрос, чтобы получить полную информацию о выбранном покемоне

5. Извлеките и выведите следующие данные о введенном покемоне:

     • Имя

     • Тип

     • Вес

     • Рост

     • Способности

Используйте PokéAPI (https://pokeapi.co/), который предоставляет информацию о покемонах, их характеристиках, типах и другую информацию.
"""

import requests

url = "https://pokeapi.co/api/v2"


# GET-запрос для получения первых 20 покемонов
def get_pokemon_list(limit=20):
    response = requests.get(f"{url}/pokemon?limit={limit}")
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_names = [pokemon["name"] for pokemon in pokemon_data["results"]]
        print("Список первых 20 покемонов:")
        for name in pokemon_names:
            print(name)
    else:
        print("Не удалось получить список покемонов.")


# Получение информации о выбранном покемоне
def get_pokemon_info(pokemon_name):
    response = requests.get(f"{url}/pokemon/{pokemon_name}")
    if response.status_code == 200:
        pokemon_info = response.json()

        # Извлечение и вывод данных по условию
        name = pokemon_info["name"]
        types = [type_info["type"]["name"] for type_info in pokemon_info["types"]]
        weight = pokemon_info["weight"]
        height = pokemon_info["height"]
        abilities = [ability["ability"]["name"] for ability in pokemon_info["abilities"]]

        print(f"\nИнформация о покемоне:")
        print(f"Имя: {name}")
        print(f"Тип: {', '.join(types)}")
        print(f"Вес: {weight}")
        print(f"Рост: {height}")
        print(f"Способности: {', '.join(abilities)}")
    else:
        print("Не удалось получить информацию о покемоне.")

# Основной код
if __name__ == "__main__":
    # Вывод списка первых 20 покемонов
    get_pokemon_list()

    # Ввод имени покемона
    pokemon_name = input("\nВведите название покемона для получения информации: ").strip().lower()
    get_pokemon_info(pokemon_name)

"""## Задание 3. HTTP-запросы, ответы и посты

**Описание:**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API, реализуя следующие функции:

1. Реализуйте функцию, которая выполняет GET-запрос к https://jsonplaceholder.typicode.com/posts и возвращает список постов в формате JSON

2. Реализуйте функцию, котороая получает вводимое ID поста, выполняет GET-запрос по ID и возвращает данные поста в формате JSON

3. Реализуйте функцию, которая выполняет обработку JSON из пункта 2 и выводит всю важную информацию в консоль
"""

import requests

url = "https://jsonplaceholder.typicode.com/posts"


# Получение списка постов
def get_all_posts():
    response = requests.get(f"{url}")
    if response.status_code == 200:
        return response.json()  # список постов в формате JSON
    else:
        print("Ошибка при получении списка постов.")
        return []


# Функция получения данных поста по его ID
def get_post_by_id(post_id):
    response = requests.get(f"{url}/{post_id}")
    if response.status_code == 200:
        return response.json()  # список постов в формате JSON
    else:
        print(f"Ошибка, пост с ID {post_id} не найден")
        return []

        #return None


# Обработка JSON из п. 2 и вывод важной инф-ии о посте
def display_post_info(post_data):
    if post_data:
        print("\nИнформация о посте:")
        print(f"ID: {post_data['id']}")
        print(f"Заголовок: {post_data['title']}")
        print(f"Текст: {post_data['body']}")
        print(f"ID пользователя: {post_data['userId']}")
    else:
        print("Нет данных для отображения.")


#Основной код
if __name__ == "__main__":
    all_posts = get_all_posts()
    if all_posts:
        print("Список первых 5 постов:")
        for post in all_posts[:5]: #Отображение первых 5 постов
            print(f"ID: {post['id']}, Заголовок: {post['title']}")

    # Ввод ID поста польз-ем
    try:
        post_id = int(input("\nВведите ID поста для получения данных поста: "))
        post_data = get_post_by_id(post_id)
        display_post_info(post_data)
    except ValueError:
        print("Ошибка. Недопустимое значение для ID")

"""## Задание 4. HTTP-запросы, ответы и работа с постами

**Описание**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API (из предыдущего задания), реализуя новые функции:

1. Реализуйте функцию, которая принимает заголовок, содержимое и ID пользователя (информация вводится с помощью input()), выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON


```
Заголовок: Новый пост
Содержимое поста: Тут должно находиться содержимое нового поста...
ID пользователя: 10
```



2. Реализуйте функцию, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON

3. Реализуйте функцию, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
"""

import requests

url = "https://jsonplaceholder.typicode.com"


# Функция для создания нового поста
def create_post(title, body, user_id):
    # Создаем данные для нового поста
    post_data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    # POST-запрос для создания нового поста
    response = requests.post(f"{url}/posts", json=post_data)

    # Проверка статуса ответа
    if response.status_code == 201:
        print("Пост успешно создан!")
        return response.json()  # Возврат информации о созданном посте
    else:
        print("Ошибка при создании поста.")
        return None


# Функция для обновления существующего поста
def update_post(post_id, new_title, new_body):
    update_data = {
        "title": new_title,
        "body": new_body
    }
    response = requests.put(f"{url}/posts/{post_id}", json=update_data)
    if response.status_code == 200:
        print("Пост обновлен!")
        return response.json()
    else:
        print(f"Ошибка при обновлении поста с ID {post_id}.")
        return None


# Функция для удаления поста по ID
def delete_post(post_id_to_delete):
    response = requests.delete(f"{url}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Пост с ID {post_id} удален.")
    else:
        print(f"Ошибка при удалении поста с ID {post_id}.")
    return response.status_code

# Основной код
if __name__ == "__main__":
    # Создание поста
    title = input("Введите заголовок поста: ")
    body = input("Введите содержимое поста: ")

    try:
        user_id = int(input("Введите ID пользователя: "))
        created_post = create_post(title, body, user_id)
        if created_post:
            print("\nИнформация о созданном посте:")
            print(f"ID: {created_post['id']}")
            print(f"Заголовок: {created_post['title']}")
            print(f"Содержимое: {created_post['body']}")
            print(f"ID пользователя: {created_post['userId']}")

        # Обновление поста
        post_id = int(input("\nВведите ID поста для обновления: "))
        new_title = input("Введите новый заголовок: ")
        new_body = input("Введите новое содержимое: ")
        updated_post = update_post(post_id, new_title, new_body)
        if updated_post:
            print("\nИнформация об обновленном посте:")
            print(f"ID: {updated_post['id']}")
            print(f"Заголовок: {updated_post['title']}")
            print(f"Содержимое: {updated_post['body']}")

        # Удаление поста
        post_id_to_delete = int(input("\nВведите ID поста для удаления: "))
        delete_status = delete_post(post_id_to_delete)
        print(f"Статус удаления: {delete_status}")

    except ValueError:
        print("Ошибка: Введите допустимое числовое значение для ID.")

import requests


def create_post(title, content, user_id, url):
    data = {
        "title": title,
        "body": content,
        "userId": user_id
    }

    response = requests.post(url, json=data)

    return response.json()


def update_post(post_id, new_title, new_content, url):
    data = {
        "title": new_title,
        "body": new_content
    }

    response = requests.put(f"{url}/{post_id}", data)

    return response.json()


def delete_post(post_id, url):
    response = requests.delete(f"{url}/{post_id}")

    return response.status_code


action = 0
url = "https://jsonplaceholder.typicode.com/posts"
while action != 4:
    print("Действия:\n"
          "1. Отправить POST запрос\n"
          "2. Отправить PUT запрос\n"
          "3. Отправить DELETE запрос\n")

    action = int(input("Введите число, обозначающее "
                       "действие в списке выше: "))
    if action == 1:
            # Создание нового поста
        title = input("Введите заголовок поста: ")
        content = input("Введите содержание поста: ")
        user_id = int(input("Введите ID пользователя: "))
        new_post = create_post(title, content, user_id, url)
        print("Созданный пост:", new_post)
    elif action == 2:
            # Обновление поста
        post_id_to_update = int(input("Введите ID поста для обновления: "))
        new_title = input("Введите новый заголовок поста: ")
        new_content = input("Введите новое содержание поста: ")
        updated_post = update_post(post_id_to_update, new_title, new_content, url)
        print("Обновлённый пост:", updated_post)
    elif action == 3:
            # Удаление поста
        post_id_to_delete = int(input("Введите ID поста для удаления: "))
        status_code = delete_post(post_id_to_delete, url)
        print("Статус удаления поста:", status_code)

    elif action == 4:
        break



"""## Задание 5. HTTP-запросы, ответы и пёсики

**Описание**

Создайте программу, которая будет взаимодействовать с Dog API, которая позволит получать список пород собак, вводить несколько пород и получать их фотогрфии.

Этапы:

1. Создайте функцию, которая использует метод GET и возвращает список всех пород собак в формате нумерованного списка

2. Реализуйте возможность ввода нескольких пород собак через запятую


```
african, chow, dingo
```



3. Создание функции, которая реализует запрос, возвращает и выводит изображениия собак, породы которых были введены до этого


Используйте Dog API (https://dog.ceo/dog-api/), который предоставляет информацию о породах собак и их изображения.

*Подсказка*



```
import requests
from PIL import Image
from IPython.display import display
import io

url = <____>
response = <____>
        
if response.<______> == <___>:
      image_url = response.json()['message']

res = requests.<__>(image_url)
img = Image.open(io.BytesIO(res.content))
display(img)
```
"""

import requests
from PIL import Image
from IPython.display import display
import io

url = "https://dog.ceo/api"


# Функция для получения списка всех пород собак
def get_breeds():
    response = requests.get(f"{url}/breeds/list/all")
    if response.status_code == 200:
        breeds = response.json()['message']
        breed_list = list(breeds.keys())

        # Выводим породы собак в нумерованном списке
        print("Список всех пород собак:")
        for i, breed in enumerate(breed_list, 1):
            print(f"{i}. {breed}")

        return breed_list
    else:
        print("Ошибка при получении списка пород.")
        return []

# Функция для получения и отображения изображений выбранных пород собак
def display_dog_images(breeds):
    for breed in breeds:
        response = requests.get(f"{url}/breed/{breed}/images/random")

        if response.status_code == 200:
            image_url = response.json()['message']
            res = requests.get(image_url)
            img = Image.open(io.BytesIO(res.content))
            print(f"\nИзображение породы {breed}:")
            display(img)
        else:
            print(f"Не удалось получить изображение для породы: {breed}")

# Основной код
if __name__ == "__main__":
    # Получение списка всех пород
    all_breeds = get_breeds()

    if all_breeds:
        # Запрос породы
        input_breeds = input("Введите названия пород через запятую: ")
        selected_breeds = [breed.strip().lower() for breed in input_breeds.split(",")]

        # Фильтр по доступным породам
        valid_breeds = [breed for breed in selected_breeds if breed in all_breeds]
        if valid_breeds:
            # Отображение изображения для выбранной породы
            display_dog_images(valid_breeds)
        else:
            print("Ни одна из введенных пород не найдена в списке.")