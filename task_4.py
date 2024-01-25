# task 4

import csv
import string #для пароля(заглавные строчные буквы алфавита)
import random


def create_initials(s: string): #строчка с ФИО
    '''
    Функция для создания логина ученика
    :param s: переменную типа строчка
    :return: созданный логин
    '''
    names = s.split() #split - делит массив на элементы по пробелу
    return f'{names[0]}_{names[1][0]}{names[2][0]}'#нули тут типо первая буква имени и первая отчества


def create_password():
    '''
    Функция для создания пароля ученика
    :return: сгенерированный пароль
    '''
    characters = string.ascii_letters + string.digits #создаем строчку из рандомных букв и цифр
    password = ''.join(random.choice(characters) for _ in range(8)) #создаем пароль из рандомных символов строчки выше
    return password

students_with_password = []
with open('students.csv', encoding = 'utf-8') as file: #тут utf - это кодировка
    reader = list(csv.DictReader(file, delimiter = ',', quotechar='"')) # reader - позволяет читать наш файл в виде списка,
    #каждым элементов списка будет являться каждая строчка списка - это DictReader делает
    # delimiter - разделитель строчек это запятая, quotechar по умолчанию ставится такой
    for row in reader:
        row['login'] = create_initials(row['Name'])
        row['password'] = create_password()
        students_with_password.append(row)

with open('students_new.csv', 'w', newline = '',encoding = 'utf-8') as file:
    #'w' - файл создается на запись,newline - для правильного переноса
    w = csv.DictWriter(file, fieldnames = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    #DictWriter - запись в новый файл столбцов
    w.writeheader() #создание заголовков
    w.writerows(students_with_password) #запись самих строк с инфой
