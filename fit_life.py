# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
CONVERT_TO_LITER = 1000

user_name = str(input("Здраствуйте, Как вас зовут? "))
while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        break
    except Exception:
        print("Введите возраст числом!")

while True:
    try:
        user_weight = float(input("Сколько вы вестите? "))
        break
    except Exception:
        print("Введите вес используя разделитель точка.")

while True:
    try:
        user_height = float(
            input("Какой у вас рост метрах (например 1.75)? "))
        break
    except Exception:
        print("Введите рост, используя раздеитель точка.")

# Формула ИМТ: вес разделить на (рост в квадрате)
if user_height > 0:
    bmi = round(user_weight / (user_height ** 2), 1)
else:
    bmi = 0

# Подсчет воды: вес * 30 мл
water_needed = round(user_weight * WATER_PER_KG / CONVERT_TO_LITER, 2)

print(f"Отчет для пользоватля: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.2f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
