"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def count_even_odd(n, even=0, odd=0):
    if n != 0:
        if (n % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_even_odd((n // 10), even, odd)
    print(f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})')

try:
    n = int(input('Введите число: '))
except ValueError:
    print('Вы ввели не натуральное число! Исправтесь!')
    exit(1)

count_even_odd(n)

# n = 3451
# count_even_odd(3451, 0, 0)
# count_even_odd(345, 0, 1) -> 1
# count_even_odd(34, 0, 2) -> 5
# count_even_odd(3, 1, 2) -> 4
# count_even_odd(0, 1, 3) -> 3
# Срабатывает базовое условие n != 0-> Количество четных и нечетных цифр в числе равно: (1, 3)
