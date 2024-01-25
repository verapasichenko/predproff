#task 5
#хэш таблица представляет из себя структуру данных в форматте
#ключ-значение, где значение-это сами данные, а ключ-значение хэша

import csv

def geenerate_hash(s: str):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l : i for i, l in enumerate(alphabet, 1)} #словарь,
    # в котором ключом является буква, а значение - это значение буквы начиная с 1(а=1)
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1 #p в нулевой будет единицей
    for c in s:
        hash_value = (hash_value + d[c]*p_pow) % m
        p_pow = (p_pow *p) % m
    return int(hash_value)

student_with_hash = []
with open('students.csv', encoding = 'utf-8') as file: #тут utf - это кодировка
    reader = list(csv.DictReader(file, delimiter = ',', quotechar='"')) # reader - позволяет читать наш файл в виде списка,
    #каждым элементов списка будет являться каждая строчка списка - это DictReader делает
    # delimiter - разделитель строчек это запятая, quotechar по умолчанию ставится такой
    for row in reader:
        row['id'] = geenerate_hash(row['Name'])
        student_with_hash.append(row)

with open('students_new.csv', 'w', newline = '',encoding = 'utf-8') as file:
    #'w' - файл создается на запись,newline - для правильного переноса
    w = csv.DictWriter(file, fieldnames = ['id', 'Name', 'titleProject_id', 'class', 'score'])
    #DictWriter - запись в новый файл столбцов
    w.writeheader() #создание заголовков
    w.writerows(student_with_hash) #запись самих строк с инфой