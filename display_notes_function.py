def display_page(notes, page):
    start_index = 0 + page * 3
    end_index = 3 + page * 3
                                # notes[0:3] - первая страница
                                # notes[3:6] - вторая страница
    for index, note in enumerate(notes[start_index:end_index], start=1):  # f строки
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        Описание: {note["content"]}
        Статус: {note["status"]}
        Дата создания: {note["created_date"]}
        Дедлайн: {note["issue_date"]}
        """)
        print("_" * 50)  # str * int

def display_notes(notes, page_number=0):
    if len(notes) == 0:
        print("Список заметок пуст")
    else:
        display_page(notes, page_number)

if __name__ == '__main__':
    notes = [
        {"username": "Дмитрий", "title": "Обучение", "content": "Доделать этап 3", "status": "в процессе",
         "created_date": "20-01-2025", "issue_date": "25-01-2025"},
        {"username": "Мария", "title": "ДР Алёны", "content": "Купить подарок", "status": "выполнено",
         "created_date": "20-01-2025", "issue_date": "22-01-2025"},
        {"username": "Дарья", "title": "Выступление", "content": "Выучить танец", "status": "в процессе",
         "created_date": "20-01-2025", "issue_date": "30-01-2025"}
    ]
    display_notes(notes=notes, page_number=0)

