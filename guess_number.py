"""Импорт функции получения случайных чисел"""

from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадай число от 1 до 100')


def check_number():
    """Проверяет число"""

    flag = False

    # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        print('Число меньше загаданного.')
    elif guess > number:
        # ...выводим сообщение.
        print('Число больше загаданного.')
    elif guess == number:
        flag = True

    return flag


while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input('Твоё число: '))

    if check_number():
        break

# ...выводим сообщение.
print('Отличная интуиция! Ты угадал число :)')
