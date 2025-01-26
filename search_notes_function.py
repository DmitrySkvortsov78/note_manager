def search_notes(notes, keyword=None, status=None):
    fields_for_search = ["title", "content", "username"]
    found_notes = []

    for note in notes:
        keyword_creteria = True
        status_creteria = True

        if keyword is not None:
            for field in fields_for_search:
                if keyword in note[field]:
                    keyword_creteria = True
                    break
                else:
                    keyword_creteria = False
        if status is not None:
            if note["status"] == status:
                status_creteria = True
            else:
                status_creteria = False

        if keyword_creteria == True and status_creteria == True:
            found_notes.append(note)

    return found_notes

if __name__ == '__main__':
    notes = [
        {'username': 'Дмитрий', 'title': 'Обучение', 'content': 'Доделать этап 3', 'status': 'в процессе',
         'created_date': '20-01-2025', 'issue_date': '25-01-2025'},
        {'username': 'Мария', 'title': 'ДР Алёны', 'content': 'Купить подарок', 'status': 'выполнено',
         'created_date': '20-01-2025', 'issue_date': '22-01-2025'},
        {'username': 'Дарья', 'title': 'Выступление', 'content': 'Выучить танец', 'status': 'в процессе',
         'created_date': '20-01-2025', 'issue_date': '30-01-2025'}
    ]
    found_notes = search_notes(notes, keyword="Обучение", status=None)
    print(found_notes)

    # found_notes = search_notes(notes, keyword=None, status="Выполнено")
    # print(found_notes)

    # found_notes = search_notes(notes, keyword="подарок", status="выполнено")
    # print(found_notes)

    # found_notes = search_notes(notes)
    # search_notes(notes, keyword='Обучение', status=None)
    # search_notes(notes, keyword=None, status='выполнено')
    # print(found_notes)

