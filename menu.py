from colorama import init, Fore, Style

from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from search_notes_function import search_notes

# Инициализация библиотеки
init(autoreset=True)

def delete_note(notes):
    # Создаём перечень заметок
    notes = [
        {
            'id': 1,
            'username': 'Дмитрий',
            'title': 'Обучение',
            'content': 'Доделать этап 3',
            'status': 'в процессе',
            'created_date': '20-01-2025',
            'issue_date': '25-01-2025'
        },
        {
            'id': 2,
            'username': 'Мария',
            'title': 'ДР Алёны',
            'content': 'Купить подарок',
            'status': 'выполнено',
            'created_date': '20-01-2025',
            'issue_date': '22-01-2025'
        },
        {
            'id': 3,
            'username': 'Дарья',
            'title': 'Выступление',
            'content': 'Выучить танец',
            'status': 'в процессе',
            'created_date': '20-01-2025',
            'issue_date': '30-01-2025'
        }
    ]

    # Предлагаем ознакомиться со списком заметок
    print('Выберите заметку для удаления')
    print('Для выбора используйте имя пользователя или заголовок заметки:')
    for note in notes:
        print(f"{note['id']}. Имя: {note['username']}")
        print(f"   Заголовок: {note['title']}")
        print(f"   Описание: {note['content']}")
        print(f"   Статус: {note['status']}")
        print(f"   Дата создания: {note['created_date']}")
        print(f"   Дедлайн: {note['issue_date']}\n")

    # Запрос критерия для удаления
    search_term = input("Введите имя пользователя или заголовок для удаления заметки: ")

    # Проверка, что ввод не пустой
    if not search_term:
        print("Ошибка: критерий поиска не может быть пустым.")
    else:
        # Создаем новый список для хранения заметок, которые нужно оставить
        notes_to_keep = []
        notes_to_delete = []

        # Поиск заметок для удаления
        for note in notes:
            if note['username'] == search_term or note['title'] == search_term:
                notes_to_delete.append(note)
            else:
                notes_to_keep.append(note)

        # Проверка, найдены ли заметки для удаления
        if not notes_to_delete:
            print("Заметок с таким именем пользователя или заголовком не найдено.")
        else:
            # Вывод заметок, которые будут удалены
            print("\nСледующие заметки будут удалены:")
            for note in notes_to_delete:
                print(f"{note['id']}. Имя: {note['username']}")
                print(f"   Заголовок: {note['title']}")
                print(f"   Описание: {note['content']}")
                print(f"   Статус: {note['status']}")
                print(f"   Дата создания: {note['created_date']}")
                print(f"   Дедлайн: {note['issue_date']}\n")

            # Запрос подтверждения удаления
            confirm = input("Вы уверены, что хотите удалить эти заметки? (да/нет): ")

            if confirm == 'да':
                # Обновление списка заметок
                notes = notes_to_keep

                # Обновление ID заметок
                for i, note in enumerate(notes, 1):
                    note['id'] = i

                # Вывод результата
                print("\nЗаметки успешно удалены.")
                if notes:
                    print("\nОстались следующие заметки:")
                    for note in notes:
                        print(f"{note['id']}. Имя: {note['username']}")
                        print(f"   Заголовок: {note['title']}")
                        print(f"   Описание: {note['content']}")
                        print(f"   Статус: {note['status']}")
                        print(f"   Дата создания: {note['created_date']}")
                        print(f"   Дедлайн: {note['issue_date']}\n")
                else:
                    print("Список заметок пуст.")
            else:
                print("\nУдаление отменено.")
    return notes

def display_menu(notes):
    while True:
        # Отображаем меню
        print(f"{Style.BRIGHT+Fore.GREEN}\nМеню действий:")
        print(f"{Fore.RED}1. Создать новую заметку")
        print(f"{Fore.YELLOW}2. Показать все заметки")
        print(f"{Fore.BLUE}3. Обновить заметку")
        print(f"{Fore.CYAN}4. Удалить заметку")
        print(f"{Fore.MAGENTA}5. Найти заметки")
        print(f"{Fore.GREEN}6. Выйти из программы")

        try:
            choice = input("Ваш выбор: ")
            if choice == "1":
                note = create_note()
                notes.append(note)
            elif choice == "2":
                display_notes(notes)
            elif choice == "3":
                if notes:
                    display_notes(notes)
                    index = int(input("Введите номер заметки для обновления: ")) - 1
                    if 0 <= index < len(notes):
                        notes[index] = update_note(notes[index])
                    else:
                        print("Неверный номер заметки.")
                else:
                    print("Список заметок пуст.")
            elif choice == "4":
                # Реализуем функцию удаления заметки
                notes = delete_note(notes)
            elif choice == "5":
                keyword = input("Введите ключевое слово для поиска: ")
                status = input("Введите статус для поиска (или оставьте пустым): ")
                found_notes = search_notes(notes, keyword, status)
                display_notes(found_notes)
            elif choice == "6":
                print("Программа завершена. Спасибо за использование!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число от 1 до 6.")

# Запускаем меню
if __name__ == "__main__":
    notes = [
        {'username': 'Дмитрий', 'title': 'Обучение', 'content': 'Доделать этап 3', 'status': 'в процессе',
         'created_date': '20-01-2025', 'issue_date': '25-01-2025'},
        {'username': 'Мария', 'title': 'ДР Алёны', 'content': 'Купить подарок', 'status': 'выполнено',
         'created_date': '20-01-2025', 'issue_date': '22-01-2025'},
        {'username': 'Дарья', 'title': 'Выступление', 'content': 'Выучить танец', 'status': 'в процессе',
         'created_date': '20-01-2025', 'issue_date': '30-01-2025'}
    ]
    display_menu(notes)
