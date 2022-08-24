import re

file1 = open('names.txt', 'w', encoding='UTF-8')
file2 = open('mails.txt', 'w', encoding='UTF-8')
file3 = open('files.txt', 'w', encoding='UTF-8')
file4 = open('colors.txt', 'w', encoding='UTF-8')
with open('MOCK_DATA.txt', 'r', encoding='UTF-8') as m_d:
    content = m_d.read()

def names_1():
    names_list = re.findall(r'\b[A-Z][a-zA-Z\'\-\. ]+[\s]+[a-zA-Z\'\-\. ]+\b', content)

    print(f'Количество имен: {len(names_list)}')


    for i in names_list:
        print(i)
        file1.write(f'\n{i}')






def mails_2():
    mails_list = re.findall(r'\w+@[a-z0-9._-]+\.[a-z]{2,}', content)
    print(f'Количество электроных адресов: {len(mails_list)}')


    for i in mails_list:
        print(i)
        file2.write(f'\n{i}')




def files_3():
    files_list = re.findall(r'\s[A-Z][a-zA-Z]+\.\w{3,}', content)
    print(f'Количество файлов: {len(files_list)}')
    for i in files_list:
        print(i)
        file3.write(f'\n{i}')
    # Я вводил этот код в Visual studio Code и там у меня было 1000 файлов, но тут почему то 996






def colors_4():
    colors_list = re.findall(r'#\w{6}', content)
    print(f'Количество цветов: {len(colors_list)}')
    for i in colors_list:
        print(i)
        file4.write(f'\n{i}')





def start():
    print('Выберите число от 1-5\n'
          '1 - имена\n'
          '2 - электроные адреса\n'
          '3 - файлы\n'
          '4 - цвета\n'
          '5 - выход из програмы')
    while True:

        a = int(input('Введите число: '))
        if a == 1:
            names_1()
        elif a == 2:
            mails_2()
        elif a == 3:
            files_3()
        elif a == 4:
            colors_4()
        elif a == 5:
            print('Программа завершена')
            break
        else:
            print('Вводите числа только от 1 до 5')
start()



