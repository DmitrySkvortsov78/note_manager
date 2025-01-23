from datetime import datetime

print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")

# Выводим текущую дату в формате "день-месяц-год"
now = datetime.now()
formatted = now.strftime("%d-%m-%Y")
print("Текущая дата:", formatted)

def create_note():
  name = input("Введите имя пользователя: ")
  title = input("Введите заголовок заметки: ")
  content = input("Введите описание заметки: ")
  status = input("Введите статус заметки: ")
  created_date = input('Дата создания заметки в формате "день-месяц-год", например "20-01-2025": ')

  # Используем цикл while с условиями
  while True:
      try:
          # Запрашиваем дату дедлайна у пользователя
          issue_date = input("Введите дату дедлайна (в формате день-месяц-год, например 25-01-2025): ")

          # Преобразуем строку с датой в объект datetime
          deadline = datetime.strptime(issue_date, "%d-%m-%Y")
          formatted2 = deadline.strftime("%d-%m-%Y")

          # Вычисляем разницу между дедлайном и текущей датой
          time_difference = deadline - now
          days_difference = time_difference.days

          # Проверяем статус дедлайна и выводим соответствующее сообщение
          if days_difference < 0:
              print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
          elif days_difference == 0:
              print("Дедлайн сегодня!")
          else:
              print(f"До дедлайна осталось {days_difference:02d} дней.")
          break
      except ValueError:
          print("Произошла ошибка! Пожалуйста, введите дату в формате (день-месяц-год).")

  return {
      "Имя": name,
      "Заголовок": title,
      "Описание": content,
      "Статус": status,
      "Дата создания": created_date,
      "Дедлайн": deadline
  }

def my_notes(notes):
  if not notes:
      print("Нет сохраненных заметок.")
      return

  for i, note in enumerate(notes):
    print(f"Заметка #{i + 1}")
    for key, value in note.items():
      print(f"  {key}: {value}")

def main():
  notes = []
  while True:
    command = input("Введите 'создать' для добавления заметки или 'стоп' для завершения: ").lower()

    if command == "создать":
      new_note = create_note()
      notes.append(new_note)
      print("Заметка добавлена.")
    elif command == "стоп":
      break
    else:
       print("Неверная команда, попробуйте еще раз.")

  my_notes(notes)

if __name__ == "__main__":
  main()
