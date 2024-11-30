# -*- coding: utf-8 -*-
"""Python  "Практика 0.4.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s2rqhKV7TFjujGPoJ8Ayg_iHvE5-_OI3

Введите ваше ФИО:
"""

print("Цепелев Кирилл Сергеевич")

"""***Дисклеймер***

В данной практике запрещено использования функций:


*   sum()
*   min()
*   max()
*   average()
*   reversed()
*   sorted()
*   готовые функции или библиотеки

**Задача 1:**



Интернет-магазин предлагает следующие условия скидок:

*   Для заказов больше 1000 единиц, клиент получает скидку 5%. Если клиент использует промокод SUPERDISCOUNT, он получает скидку 10% (вместо 5%).
*  Для заказов более 5000 единиц, клиент получает скидку 15%, а использование промокода SUPERDISCOUNT увеличивает скидку до 20% (вместо 15%).

Этап 1:
Ввод:
```
Введите стоимость единицы товара: 5
Введите количество товара: 1001
Введите промокод: GiVEMEDISCONT
```

Вывод:

```
Ваша скидка: 5%
Итоговая сумма: 4754.75
```
Этап 2:

Оформите ваш код в виде функции
"""

def skidIsum (cost, k, skid):
    if k > 1000 and k <= 5000:
        if pr == 'superdiscount':
            skid = 10
            print(f'Ваша скидка {skid}%')
        else:
            skid = 5
            print(f'Ваша скидка {skid}%')
    elif k > 5000:
        if pr == 'superdiscount':
            skid = 20
            print(f'Ваша скидка {skid}%')
        else:
            skid = 15
            print(f'Ваша скидка {skid}%')
    else:
        print('Скидка отсутсвует ')

    return ((cost*k)-(cost*k/100*skid))


cost = int(input('Введите стоимость единицы товара: '))
k = int(input('Введите количество товара: '))
pr = input('Введите промокод: ')
pr = pr.lower()

skidIsum (cost, k, skid)

"""**Задача 2:**

Этап 1:
Напишите программу способную отфильтровать список и вывести только положительные элементы


Ввод:
```
-1 5 1 2 -3
```

Вывод:

```
5 1 2
```

Этап 2:

Оформите ваш код в виде функции
"""

def filtr(numlist):
    for i in [i for i in numlist if i > 0]:
        rez.append(i)
    return rez
nums = (input("Введите числа через пробел: ").split())
numlist = list(map(int, nums))
rez = []

output=filtr(numlist)

# print(output)
print(" ".join(map(str,output)))

"""**Задача 3:**

Этап 1:
Напишите программу реализующую Алгоритм Евклида


> Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.



Ввод:
```
30 18
```

Вывод:

```
6
```

Этап 2:
Оформите ваш код в виде функции

"""

def nod(x,y):
    while x != y and y != x:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x
nums = (input().split())
numlist = list(map(int, nums))

nod(numlist[0],numlist[1])

"""**Задача 4:**

Этап 1:
Напишите функцию программу, которая принимает строку и возвращает список слов и количество их упомнинаний в предложении

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
apple banana apple
```

Вывод:

```
apple: 2,
banana: 1
```
"""

def count_words(sentence):
    words = sentence.lower().split()
    unique_words = [] #список для хран уник слов
    word_counts = []  #список для хранения количества повтор каждого слова

    for word in words:
        if word in unique_words:      #если слово в списке слов
            # Находим по индексу слово и увеличиваем счётчик
            index = unique_words.index(word)
            word_counts[index] += 1
        else:
        # Если слова нет в списке, добавляем его в список уникальных слов
            unique_words.append(word)
        # Добавляем 1 в список количества, так как это первое упоминание слова
            word_counts.append(1)
    # Создаём список для результата
    result = []

    for i in range(len(unique_words)):
        result.append([unique_words[i], word_counts[i]])
    return result

sentence = input()
rez = count_words(sentence)
print(" ".join(map(str,rez)))

"""**Задача 5:**

Этап 1:
Детектор анаграмм Напишите программу на Python, которая принимает в качестве входных данных две строки и проверяет, являются ли они анаграммами друг друга

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
listen silent
```

Вывод:

```
True
```
"""

CHARS = 256


def areAnagram(str1, str2):
    count1 = [0] * CHARS
    count2 = [0] * CHARS

    for i in str1:
      count1[ord(i)] += 1

    for i in str2:
      count2[ord(i)] += 1

    if len(str1) != len(str2):
      return 0

    # сравнение
    for i in range(CHARS):
      if count1[i] != count2[i]:
        return 0

    return 1


str1, str2 = (input().split())

# str1 = "listen"
# str2 = "silent"

if areAnagram(str1, str2):
	print ("True")
else:
	print ("False")

"""**Задача 6:**

Шифр ​​Цезаря

Напишите программу на Python, которая реализует шифр Цезаря, простой метод шифрования, который заменяет каждую букву буквой на фиксированное количество позиций вниз по алфавиту. Программа должна запрашивать у пользователя сообщение и значение сдвига, а затем шифровать и расшифровывать сообщение.

Этап 1:

Напишите код для реализации данной задачи

Этап 2:

Оформите код в виде нескольких функций:

* Зашифровывает сообщение
* Расшифровывает сообщение
"""

#Зашифровка сообщения
def shifr(mes):
    mes = input("Сообщение для шифровки: ").lower()
    lang = input('Выберите язык ru/en: ')
    lang = lang.lower()
    res = ''

    if lang == 'ru':
        for i in mes:
            mesto = l_alf_ru.find(i)
            new_mesto = mesto + sdvig
            if i in l_alf_ru:
                res += l_alf_ru[new_mesto]
            else:
                res += i
    elif lang == 'en':
        for i in mes:
            mesto = l_alf_en.find(i)
            new_mesto = mesto + sdvig
            if i in l_alf_en:
                res += l_alf_en[new_mesto]
            else:
                res += i
    else:
        print("Ошибка выбора языка")

    return res


#Расшифровка сообщения
def deshifr(mes):
    mes = input("Сообщение для расшифровки: ").lower()
    lang = input('Выберите язык ru/en: ')
    lang = lang.lower()
    res = ''

    if lang == 'ru':
        for i in mes:
            mesto = l_alf_ru.find(i)
            new_mesto = mesto - sdvig
            if i in l_alf_ru:
                res += l_alf_ru[new_mesto]
            else:
                res += i
    elif lang == 'en':
        for i in mes:
            mesto = l_alf_en.find(i)
            new_mesto = mesto - sdvig
            if i in l_alf_en:
                res += l_alf_en[new_mesto]
            else:
                res += i
    else:
        print("Ошибка выбора языка")

    return res


# Англ и русский алфавит
l_alf_en = ''.join(map(chr, range(ord('a'), ord('z') + 1)))
l_alf_ru = ''.join(map(chr, range(ord('а'), ord('я') + 1)))
mes = ''

print("Выберите действие: \n 1. Зашифровать сообщение.\n 2. Расшифровать сообщение\n")
a = (int(input()))

if a == 1:
    sdvig = int(input('Шаг шифровки: '))
    print(shifr(mes))
elif a == 2:
    sdvig = int(input('Шаг шифровки: '))
    print(deshifr(mes))
else:
    print("Ошибка выбора действия! Перезапустите программу.")

"""**Задача 7**

Задача: «Банковская система»

Создайте программу Python, которая имитирует базовую банковскую систему. Система должна иметь следующие функции:

Требования
*   Система должна позволять клиентам создавать счета и хранить их балансы.
*   Система должна позволять клиентам вносить и снимать деньги со своих счетов.
*   Система должна позволять клиентам проверять свой текущий баланс.
*   Система должна позволять клиентам переводить деньги между счетами.
*   Система должна отслеживать транзакции (депозиты, снятия и переводы) и иметь возможность печатать детали транзакций.


Задачи
1. Реализуйте банковскую систему, используя только базовые конструкции Python, такие как def, lists, if, elif и else, без классов или словарей.
Определите функции для создания счетов, внесения и снятия денег, получения балансов счетов, перевода денег между счетами, а также создания и печати транзакций.
2. Напишите основную функцию, которая демонстрирует использование банковской системы путем создания счетов, внесения и снятия денег и перевода денег между счетами.
3. Бонусное задание
Реализуйте способ хранения и печати истории транзакций для каждого счета.

Ограничения
Не используйте классы или словари.
Используйте только базовые конструкции Python, такие как def, lists, if, elif и else.

"""

def create_account(accounts, balances, transactions):
    account_number = len(accounts)
    accounts.append(account_number)
    balances.append(0)
    transactions.append([])
    return account_number


def deposit(accounts, balances, transactions, account_number, amount):
    if account_number in accounts and amount > 0:
        balances[account_number] += amount
        transactions[account_number].append(f"Депозит: +{amount}")
        return True
    return False


def withdraw(accounts, balances, transactions, account_number, amount):
    if account_number in accounts and 0 < amount <= balances[account_number]:
        balances[account_number] -= amount
        transactions[account_number].append(f"Снятие: -{amount}")
        return True
    return False


def check_balance(balances, account_number):
    if account_number in range(len(balances)):
        return balances[account_number]
    return None


def transfer(accounts, balances, transactions, from_account, to_account, amount):
    if (from_account in accounts and
        to_account in accounts and
        from_account != to_account and
        0 < amount <= balances[from_account]):
        balances[from_account] -= amount
        balances[to_account] += amount
        transactions[from_account].append(f"Перевод: -{amount} на счет {to_account}")
        transactions[to_account].append(f"Перевод: +{amount} со счета {from_account}")
        return True
    return False


def print_transactions(transactions, account_number):
    if account_number in range(len(transactions)):
        for transaction in transactions[account_number]:
            print(transaction)
    else:
        print("Неверный номер счета.")

def main():
    accounts = []
    balances = []
    transactions = []

    while True:
        print("\n1: Создать счет")
        print("2: Внести депозит")
        print("3: Снять деньги")
        print("4: Проверить баланс")
        print("5: Перевод денег")
        print("6: История транзакций")
        print("7: Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            account_number = create_account(accounts, balances, transactions)
            print(f"Счет создан. Номер счета: {account_number}")

        elif choice == '2':
            account_number = int(input("Введите номер счета: "))
            amount = float(input("Введите сумму депозита: "))
            if deposit(accounts, balances, transactions, account_number, amount):
                print("Депозит успешно внесен.")
            else:
                print("Ошибка внесения депозита.")

        elif choice == '3':
            account_number = int(input("Введите номер счета: "))
            amount = float(input("Введите сумму для снятия: "))
            if withdraw(accounts, balances, transactions, account_number, amount):
                print("Средства успешно сняты.")
            else:
                print("Ошибка снятия.")

        elif choice == '4':
            account_number = int(input("Введите номер счета: "))
            balance = check_balance(balances, account_number)
            if balance is not None:
                print(f"Баланс счета {account_number}: {balance}")
            else:
                print("Неверный номер счета.")

        elif choice == '5':
            from_account = int(input("Введите номер вашего счета: "))
            to_account = int(input("Введите номер счета получателя: "))
            amount = float(input("Введите сумму перевода: "))
            if transfer(accounts, balances, transactions, from_account, to_account, amount):
                print("Перевод выполнен успешно.")
            else:
                print("Ошибка перевода.")

        elif choice == '6':
            account_number = int(input("Введите номер счета: "))
            print_transactions(transactions, account_number)

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Повторите попытку.")

if __name__ == "__main__":
    main()