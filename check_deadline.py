# Импортируем модуль datetime из стандартной библиотеки Python
from datetime import datetime

# Выводим текущую дату в формате "день-месяц-год"
now = datetime.now()
formatted = now.strftime("%d-%m-%Y")
print("Текущая дата:", formatted)

# Используем цикл while с условиями
while True:
    try:
        # Запрашиваем дату дедлайна у пользователя
        issue_date = input("Введите дату дедлайна (в формате день-месяц-год, например 20-01-2025): ")

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
