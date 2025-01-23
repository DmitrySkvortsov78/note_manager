# Создаём пустой список
titles = []

# Создаём бесконечный цикл запросов о введении заголовка заметки с условиями
while True:
    user_input = input("Введите заголовок заметки (или оставьте пустым для завершения) и нажмите ввод: ")
    if user_input == '':
        print(f"Заголовки заметки: ", titles)
        break
    elif user_input in titles:
        print("Такой заголовок уже введен")
    else:
        titles.append(user_input)






