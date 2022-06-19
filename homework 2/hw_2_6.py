'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена,
количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
'''
db = []
i = 1
while input('Хотите внести данные? (Да/Нет)\n').lower() == 'да':
    line = input('Введите через пробел слежующие параметры:'
                 '1. Название 2. Цена 3. Количествво 4. Единицы измерения\n').split()
    dict_line = {'название': line[0], 'цена': int(line[1]), 'количество': int(line[2]), 'eд': line[3]}
    tuple_line = (i, dict_line)
    db.append(tuple_line)
    i += 1
    for el in range(len(db)):
        print(db[el])


'''
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''
names = []
costs = []
count = []
units = []
for row in db:
    for k, v in row[1].items():
        if k == 'название':
            names.append(v)
        elif k == 'цена':
            costs.append(v)
        elif k == 'количество':
            count.append(v)
        elif k == 'eд':
            units.append(v)

analisys_dict = {
                    'название': names,
                    'цена': costs,
                    'количество': count,
                    'ед': units
                }

for key, value in analisys_dict.items():
    print(key, ':', value)