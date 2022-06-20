'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


def my_func(arg1: int or float, arg2: int or float, arg3: int or float):
    a = [arg1, arg2, arg3]
    a.sort()
    return a[1]+a[2]


print(my_func(2, 0.3, 16.99))
