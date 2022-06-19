'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def devision(a, b):
    if b != 0:
        return a/b
    else:
        return 'Division by Zero is not available'
x, y = input('Enter two numbers devided by spacebar\n').split()
print(devision(int(x), int(y)))
