import json

# КРОК 1: Завантажуємо наші дані з попередньої роботи
with open('archive_metadata.json', 'r', encoding='utf-8') as file:
    digital_archive = json.load(file)

# КРОК 2: Створюємо базовий "скелет" нашої вебсторінки
# Ми додамо трохи стилів (CSS), щоб наші картки виглядали як справжні бібліотечні формуляри 
html_content = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Цифровий архів</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Колекція рідкісних видань</h1>
"""
# КРОК 3: Запускаємо цикл для генерації карток
# Проходимося по кожній книжці у нашому списку digital_archive
def format_year(year):
    if year and str(year).strip():
        return f"Видано у {year} р."
    else:
        return "Рік видання невідомий"
for book in digital_archive:
    
    # Використовуємо f-рядок для підстановки даних у HTML-теги
    # Зверніть увагу на фігурні дужки { } - саме туди Python вставить текст із JSON
    card_html = f"""
    <div class="card">
        <h2>{book['dc:title']}</h2>
        <p class="meta"><strong>Автор:</strong> {book['dc:creator']}</p>
        <p class="meta"><strong>Рік видання:</strong> {format_year(book.get('dc:date', ''))}</p
        <p class="meta"><strong>Місце видання:</strong> {book['dc:coverage']}</p>
        <p class="meta"><strong>Мова:</strong> {book['dc:language']}</p>
        
    </div>
    """
    
    # Доклеюємо щойно створену картку до загального коду сторінки
    # Символи += означають "додати до існуючого тексту"
    html_content += card_html

# КРОК 4: Закриваємо базові теги сторінки
html_content += """
</body>
</html>
"""

# КРОК 5: Зберігаємо весь згенерований текст у новий файл index.html
with open('index.html', 'w', encoding='utf-8') as output_file:
    output_file.write(html_content)

print("Магія відбулася! Файл index.html успішно згенеровано.")
