'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
#from itertools import count

with open('hw_2.txt', 'r') as f:
    s = f.readlines()
    print(len(s))
    for i in range(len(s)):
        print(f'В строке №{i+1} {len(s[i])} символов')
