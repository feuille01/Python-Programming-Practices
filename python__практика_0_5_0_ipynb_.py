# -*- coding: utf-8 -*-
"""Python  "Практика 0.5.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i7istAIvSqa1cHOZCwgkCP8n4EgtaVJb

**ФИО: Цепелев Кирилл Сергеевич**
"""

print("Цепелев Кирилл Сергеевич")

"""# **Задание 1**

Дан словарь, содержащий имена и возраст людей, напишите программу выводящую возраст человека по имени

Дано:

```
{"Alice": 25, "Bob": 30, "Charlie": 35}
```

Вввод:


```
Alice
```

Вывод:


```
Alice 25
```
"""

dict_={"Alice": 25, "Bob": 30, "Charlie": 35}
n = input("Введите имя: ")

print(n, dict_[n])

"""# **Задание 2**

Дан список, состоящий из целых чисел, необходимо написать функцию считающую сумму всех положительных четных чисел списка

Ввод:

```
1, 2, 3, 4, 5, 6, 7, 8, 9
```

Вывод:


```
20
```

***Запрещено:***

*   Использование готовых функций для суммирования чисел
"""

def func (list_nums):

    for x in list_nums:
        if x%2==0:
            g.append(x)

    return g[0] + g[1] + g[2] + g[3]

g = []
list_nums = map(int,input("Введите числа: ").split(","))
func(list_nums)

"""# **Задание 3**

Дан словарь, содержащий название фрукта и его цвет, выведите список всех желтых фруктов


Дано:

```
fruits_and_colors = {
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}
```

Вывод:


```
Yellow fruits:
banana
mango
lemon
```
"""

dict_={
    "apple": "red",
    "banana": "yellow",
    "mango": "yellow",
    "orange": "orange",
    "lemon": "yellow",
    "grape": "purple"
}

print("Yellow fruits:")

for k,v in dict_.items():
    if v == "yellow":
        print(k)

"""# **Задание 4**

Дан словарь, необходимо написать функцию меняющую ключ и значение местами

Дано:


```
{"a": 1, "b": 2, "c": 3}
```

Вывод:

```
{1: 'a', 2: 'b', 3: 'c'}
```
"""

dict_ = {"a": 1, "b": 2, "c": 3}

dict2 = {v:k for k,v in dict_.items()}

print(dict2)

"""# **Задание 5**

Дан список слов, неограниченной длинны, сформируйте словарь, где в качестве ключа будет слово, а в качестве значения количество слов

**Критерии**


*   Словарь необходимо отсортировать по убыванию количества элементов в списке.
*   Подсчет элементов должен быть реализован в отдельной функции
*   Сортировка пары `ключ:значение` должна быть реализована также в виде отдельной функции




Дано:
```
['apple','banana','orange','apple','apple','banana']
```


Вывод:
```
{'apple':3, 'banana': 2, 'orange': 1}
```

***Запрещено:***

*   Использование готовых функций для сортировки
*   Использование готовых функций для подсчета элементов
"""

def count_words(sentence):
    words = sentence
    uniq = {} #словарь

    for word in words:
        if word in uniq:      #если слово в списке слов
            uniq[word] += 1 #если слова есть
        else:
            uniq[word] = 1 #если слово нет
    # print(uniq)
    return uniq


def find_max(uniq):
    max_v=0
    max_k=0

    for k,v in uniq.items():
        if v>max_v:
            max_v=v
            max_k=k
    return [max_k, max_v]


def sorting(uniq):
    sorted_dict = {} #созд пустой словарь

    while uniq != { }:
        el  = find_max(uniq) #элемент равен значению, которое вернула функция
        max_k = el[0] #элемент равен по индексу 0 ключу max_k из функц find_max
        max_v = el[1] #элемент равен по индексу 1 ключу max_v из функц find_max
        del uniq[max_k] #удаляем из списка лишние фрукты
        sorted_dict[max_k] = max_v
    return sorted_dict


sentence = ['apple','banana','orange','apple','apple','banana']
rez = count_words(sentence) #выполнили подсчёт количества слов
# print(rez)
sorted_dict = sorting(rez) #вызываем функцию сортировки с вернувшимся значением подсчёта слов
print(sorted_dict)

"""# **Задание 6**

Дан словарь, содержащий информацию о людях, необходимо:



*   Вывести всех людей старше 30 лет
*   Вывести список городов и количество людей из словаря проживающих в них
*   Вывести список профессий и список людей для каждой профессии

**Критерии**

Каждый из пунктов необходимо реализовать в виде функции
"""

people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}

# Вывести всех людей старше 30 лет
def sort_age(people_info):
    people=[ ]

    for k,v in people_info.items():
        if v["age"]>30:
            people.append(k)

    print("Люди, которые старше 30 лет:")
    print(f"{', '.join(people)}\n")


# Вывести список городов и количество людей из словаря проживающих в них
def count_cities(people_info):
    c_cities = { }

    for k,v in people_info.items():
        city=v['city']
        if city in c_cities.keys():
            c_cities[city] += 1
            k = c_cities[city] + 1
        else:
            k = c_cities[city] = 1
    k = str(k)
    print("Cписок городов и количество людей из словаря проживающих в них:")
    # print(c_cities,"\n")
    print(f"{c_cities}: {', '.join(k)}\n")


# Вывести список профессий и список людей для каждой профессии
def group_by_occupation(people_info):
    occupation_dict = { }

    for name, info in people_info.items():
        occupation = info["occupation"]
        if occupation in occupation_dict:
            occupation_dict[occupation].append(name)
        else:
            occupation_dict[occupation] = [name]

    # print("Cписок профессий и список людей для каждой профессии:")
    for occupation, people in occupation_dict.items():
        print(f"{occupation}: {', '.join(people)}")


people_info = {
    "Alice": {"age": 25, "city": "New York", "occupation": "Engineer"},
    "Bob": {"age": 30, "city": "Los Angeles", "occupation": "Designer"},
    "Charlie": {"age": 35, "city": "Chicago", "occupation": "Teacher"},
    "Diana": {"age": 28, "city": "Miami", "occupation": "Doctor"},
    "Ethan": {"age": 40, "city": "Seattle", "occupation": "Chef"},
    "Frank": {"age": 32, "city": "Atlanta", "occupation": "Lawyer"},
    "Gabriella": {"age": 29, "city": "San Francisco", "occupation": "Software Engineer"},
    "Harrison": {"age": 38, "city": "Denver", "occupation": "Architect"},
    "Isabella": {"age": 26, "city": "Washington D.C.", "occupation": "Journalist"},
    "Julian": {"age": 42, "city": "Miami", "occupation": "Musician"},
    "Kate": {"age": 31, "city": "Philadelphia", "occupation": "Nurse"},
    "Lucas": {"age": 36, "city": "Nashville", "occupation": "Businessman"},
    "Mia": {"age": 27, "city": "Atlanta", "occupation": "Artist"},
    "Natalie": {"age": 39, "city": "Portland", "occupation": "Writer"},
    "Oliver": {"age": 44, "city": "Minneapolis", "occupation": "Professor"},
    "Penelope": {"age": 33, "city": "San Diego", "occupation": "Marketing Manager"},
    "Quincy": {"age": 41, "city": "Nashville", "occupation": "Singer"},
    "Rachel": {"age": 34, "city": "Cleveland", "occupation": "Teacher"},
    "Sophia": {"age": 29, "city": "Nashville", "occupation": "Engineer"},
    "Tessa": {"age": 37, "city": "Miami", "occupation": "Lawyer"}
}

sort_age(people_info)
count_cities(people_info)
group_by_occupation(people_info)

"""# **Задание 7**

Задание: Разработка системы отзывов о предметах

Описание: Создать программу на Python для хранения и управления отзывами о предметах учебного курса. Программа должна позволять пользователям добавлять, просматривать и удалять отзывы, а также вычислять средний балл по заданному предмету.

**Функционал:**

*   Добавление отзыва и оценки:
   *   Пользователь может ввести название предмета, оценку (от 1 до 5) и текст отзыва.
   *   Отзывы должны храниться в структуре данных (например, словаре), где ключом будет название предмета, а значением - список отзывов (каждый отзыв может хранить оценку и комментарий).
*   Просмотр отзывов и оценок:
   *   Пользователь может запросить отзывы для указанного предмета.
   *   Если для указанного предмета есть отзывы, программа должна отобразить список всех отзывов и соответствующих оценок.
*   Удаление отзыва:
   *   Пользователь может удалить отзыв по индексу. Необходимо заранее уведомить пользователя о том, какие отзывы доступны для удаления.
   *   Программа должна обработать ситуацию, когда индекс введен неправильно.
*   Вычисление среднего балла по предмету:
   *   Пользователь может ввести название предмета, и программа должна вычислить и вывести средний балл по всем отзывам для этого предмета.
   *   Если отзывов нет, программа должна сообщить об этом.


**Критерии:**

*   Код должен быть оформлен в виде функций
*   Необходимо обрабатывать неправильный ввод пользователя
*   Должны быть комментарии к функциям
*   Присутсвует весь дополнительный функционал



**Опционально:**

Предлагаю вам добавить свои критерии оценки или вопросы, на которые должен ответить студент, чтобы оценить пару
"""

# Основной словарь для хранения отзывов по предметам
reviews = {}


# Функция доб-я отзыва и оценки указанного предмета
def add_review(subject, rating, comment):

    if subject not in reviews:
        reviews[subject] = []  # создание списка отзывов для нового предмета

    # Добавляем отзыв в список предмета
    reviews[subject].append({"rating": rating, "comment": comment})
    print(f"Отзыв для предмета '{subject}' успешно добавлен.")


# Функция для просмотра всех отзывов по указанному предмету
def view_reviews(subject):

    if subject in reviews and reviews[subject]:
        print(f"Отзывы для предмета '{subject}':")
        index = 1  # Счётчик
        for review in reviews[subject]:
            print(f"{index}. Оценка: {review['rating']}, Комментарий: {review['comment']}")
            index += 1
    else:
        print(f"Для предмета '{subject}' нет отзывов.")


# Функция для удаления отзыва
def delete_review(subject, index):

    if subject in reviews and 0 <= index < len(reviews[subject]):
        removed_review = reviews[subject][index]

        # Пересоздание списка отзывов без удалённого элемента
        reviews[subject] = reviews[subject][:index] + reviews[subject][index + 1:]

        print(f"Отзыв: «{removed_review['comment']}» с оценкой {removed_review['rating']} удален.")
    else:
        print("Неверный индекс или отзывов для указанного предмета нет.")


# Функция для вычисления среднего балла по всем отзывам для выбранного предмета
def calculate_average_rating(subject):

    if subject in reviews and reviews[subject]:
        total_rating = sum(review["rating"] for review in reviews[subject])
        average_rating = total_rating / len(reviews[subject])
        print(f"Средний балл по предмету '{subject}': {average_rating:.2f}")
    else:
        print(f"Для предмета '{subject}' нет отзывов.")


# Осн-я функция: отображение меню и обр-ка выбора
def main():

    while True:
        print("\nМеню:")
        print("1. Добавить отзыв")
        print("2. Просмотреть отзывы")
        print("3. Удалить отзыв")
        print("4. Вычислить средний балл")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            subject = input("Введите название предмета: ")
            try:
                rating = int(input("Введите оценку (от 1 до 5): "))
                if rating < 1 or rating > 5:
                    print("Ошибка: оценка должна быть от 1 до 5.")
                    continue
            except ValueError:
                print("Ошибка: оценка должна быть целым числом.")
                continue
            comment = input("Введите текст отзыва: ")
            add_review(subject, rating, comment)

        elif choice == "2":
            subject = input("Введите название предмета для просмотра отзывов: ")
            view_reviews(subject)

        elif choice == "3":
            subject = input("Введите название предмета для удаления отзыва: ")
            try:
                index = int(input("Введите номер отзыва для удаления: ")) - 1
            except ValueError:
                print("Ошибка: номер отзыва должен быть целым числом.")
                continue
            delete_review(subject, index)

        elif choice == "4":
            subject = input("Введите название предмета для вычисления среднего балла: ")
            calculate_average_rating(subject)

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")

main()