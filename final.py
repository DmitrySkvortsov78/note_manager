username = input("Имя пользователя: ")
title = input("Заголовок заметки: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
created_date = input('Дата создания заметки в формате "день-месяц-год", например "10-11-2024": ')
issue_date = input('Дата истечения заметки (дедлайн) в формате "день-месяц-год", например "10-12-2024": ')
heading = input("Заголовок 1: ")
heading2 = input("Заголовок 2: ")
heading3 = input("Заголовок 3: ")
headings = [heading, heading2, heading3]
note = [username, title, content, status, created_date, issue_date, headings]
print("Имя пользователя:", note[0])
print("Заголовок заметки:", note[1])
print("Описание заметки:", note[2])
print("Статус заметки:", note[3])
print("Дата создания заметки:", note[4])
print("Дата истечения заметки:", note[5])
print("Заголовки 1, 2, 3:", note[6])