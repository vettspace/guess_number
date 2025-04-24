"""Угадай число"""
from random import randint
import sys


def check_number(number, guess):
    """Проверяет число"""
    flag = False

    # Если число меньше загаданного...
    if guess < number:
        # ...выводим сообщение.
        sys.stdout.write('Число меньше загаданного.\n')
    elif guess > number:
        # ...выводим сообщение.
        sys.stdout.write('Число больше загаданного.\n')
    elif guess == number:
        flag = True

    return flag


def main():
    """Основная функция"""

    number = randint(1, 100)
    sys.stdout.write('Угадай число от 1 до 100:\n\n')

    while True:
        # Получаем число от пользователя
        guess = int(input('Твоё число: '))

        if check_number(number, guess):
            break

    sys.stdout.write('\nОтлично! Ты угадал число ⭐️')


if __name__ == "__main__":
    main()
