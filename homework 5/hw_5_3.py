'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''


with open('hw_3.txt', 'w') as f:
    while True:
        s = input()
        if s != '':
            f.write(s + '\n')
        else:
            break

with open('hw_3.txt', 'r') as f:
    file_strings = f.readlines()
    #print(file_strings)
    salary_summ = 0
    for i in range(len(file_strings)):
        s = file_strings[i].split()
        if int(s[1]) < 20000:
            print(s[0])
        salary_summ += int(s[1])
        mean_salary = salary_summ / len(file_strings)
    print(mean_salary)
