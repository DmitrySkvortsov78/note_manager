status = "Статус вашей заметки: В процессе"
print(status)

print("Выберите новый статус вашей заметки:")
print("1. Выполнено")
print("2. В процессе")
print("3. Отложено")

# Создаём бесконечный цикл с условиями
while True:
   update_status = int(input("Введите новый статус: "))
   if update_status == 1:
      print("Статус вашей заметки обновлен на: Выполнено")
      break
   elif update_status == 2:
      print("Статус вашей заметки обновлен на: В процессе")
      break
   elif update_status == 3:
      print("Статус вашей заметки обновлен на: Отложено")
      break
   else:
      print("Некорректный ввод, выберите 1, 2 или 3")

status = update_status
