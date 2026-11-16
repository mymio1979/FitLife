# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
CONVERT_TO_LITER = 1000

# 1. Знакомство
user_name = str(input("Здраствуйте, Как вас зовут? "))
try:
    user_age = int(input("Сколько вам лет? "))
except Exception as error:
    raise AssertionError(
        "Введите возраст числом! "
        f"исключение: {type(error).__name__}: {error}`"
    )

# 2. Сбор данных
try:
    user_weight = float(input("Сколько вы вестите? "))
except Exception as error:
    raise AssertionError(
        "Введите вес используя разделитель точка. "
        f"исключение: {type(error).__name__}: {error}`"
    )

try:
    user_height = float(input("Какой у вас рост метрах (например 1.75)? "))
except Exception as error:
    raise AssertionError(
        "Введите рост, используя раздеитель точка."
        f"исключение: {type(error).__name__}: {error}`"
    )

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
if user_height > 0:
    bmi = round(user_weight / (user_height ** 2), 1)
else:
    bmi = 0

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_needed = round(water_ml / CONVERT_TO_LITER, 2)

# 4. Вывод красивого результата
print(f"Отчет для пользоватля: {user_name} ({user_age}.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.2f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
