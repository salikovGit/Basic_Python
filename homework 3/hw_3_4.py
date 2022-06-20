'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def power(x, y):
    if x < 0:
        return '"X" must be positive'
    elif y is not int and y >= 0:
        return '"Y" must integer and negative'
    else:
        return x ** y


def power_cycle(x, y):
    if x < 0:
        return '"X" must be positive'
    elif y is not int and y >= 0:
        return '"Y" must integer and negative'
    else:
        p = 1
        for i in range(0, abs(y)):
            p /= x
        return p


print(power(2, -3))
print((power_cycle(2, -3)))
