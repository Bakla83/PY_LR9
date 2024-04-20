import csv
from dateparser import parse

# Загружаем данные из CSV-файла
with open("2 - 1.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Пропускаем заголовок
    next(reader, None)

    target_date = parse("01 Янв 2024")  # Заданная дата
    pedagogy_scores = []  # Список для хранения баллов по Педагогике
    psychology_scores = []  # Список для хранения баллов по Психологии
    passed_tests = []  # Список для хранения информации о пройденных тестах
    all_tests = []  # Список для хранения информации о всех тестах

    for row in reader:
        # Получаем информацию из строки
        last_name, first_name, _, _, _, _, test_started, _, _, score, _, _, _, _, _, b4, b5, b6, b7, *_ = row

        # Парсим дату начала теста
        start_date = parse(test_started)

        # Добавляем информацию о всех тестах
        all_tests.append((last_name, first_name, test_started, score))

        # Проверяем, что тест был выполнен до заданной даты
        if start_date is not None and start_date <= target_date:
            if score != '-':
                score = float(score.replace(',', '.'))

                if b4 != '-' and b5 != '-':
                    pedagogy_scores.append((float(b4.replace(',', '.')), float(b5.replace(',', '.'))))
                if b6 != '-' and b7 != '-':
                    psychology_scores.append((float(b6.replace(',', '.')), float(b7.replace(',', '.'))))

                if score >= 60:
                    passed_tests.append((last_name, first_name, test_started, score))

    pedagogy_average = sum(sum(scores) / 2 for scores in pedagogy_scores) / len(pedagogy_scores) if pedagogy_scores else 0
    psychology_average = sum(sum(scores) / 2 for scores in psychology_scores) / len(psychology_scores) if psychology_scores else 0

    print(f"Средний балл по теме 'Педагогика': {pedagogy_average:.2f}")
    print(f"Средний балл по теме 'Психология': {psychology_average:.2f}")

    print("\nСписок всех пройденных тестов:")
    for test in passed_tests:
        print(f"{test[0]} {test[1]} - {test[2]}: {test[3]}")

    print("\nСписок всех тестов, которые могут удовлетворять условию:")
    for test in all_tests:
        print(f"{test[0]} {test[1]} - {test[2]}: {test[3]}")
