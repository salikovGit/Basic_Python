'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''


translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []

with open('hw_4.txt', 'r') as f:
    for line in f.readlines():
        new_line = line.split()
        new_line[0] = translation.get(new_line[0])
        new_text.append(new_line)


with open('hw_4_translated.txt', 'w') as file:
    for line in new_text:
        file.write(' '.join(line) + '\n')
