"""Импорт функции получения случайных чисел"""

from random import randint
import sys

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
sys.stdout.write(f'Угадай число от 1 до 100\n------------------------\n')


def check_number():
    """Проверяет число"""

    flag = False

    # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        sys.stdout.write('Число меньше загаданного.\n\n')
    elif guess > number:
        # ...выводим сообщение.
        sys.stdout.write('Число больше загаданного.\n\n')
    elif guess == number:
        flag = True

    return flag


while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input('Твоё число: '))

    if check_number():
        break

sys.stdout.write('\nОтлично! Ты угадал число :)')
