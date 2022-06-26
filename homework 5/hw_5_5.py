'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

numbers = '1 2 3 4 5'

with open('hw_5.txt', 'w') as file:
    file.write(numbers + '\n')

result = []

with open('hw_5.txt', 'r') as file:
    for line in file.readlines():
        result.extend((line.split()))

print(sum(list(map(int, result))))
