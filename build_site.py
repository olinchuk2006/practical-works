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
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }
        h1 { text-align: center; color: #333; }
        /* Дизайн нашої каталожної картки */
        .card { 
            background: white; 
            border-radius: 8px; 
            padding: 15px; 
            margin-bottom: 15px; 
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
            border-left: 5px solid #4CAF50; /* Зелена смужка зліва */
        }
        .card h2 { margin-top: 0; color: #2c3e50; }
        .meta { color: #555; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Колекція рідкісних видань</h1>
"""

# КРОК 3: Запускаємо цикл для генерації карток
# Проходимося по кожній книжці у нашому списку digital_archive
for book in digital_archive:
    
    # Використовуємо f-рядок для підстановки даних у HTML-теги
    # Зверніть увагу на фігурні дужки { } - саме туди Python вставить текст із JSON
    card_html = f"""
    <div class="card">
        <h2>{book['dc:title']}</h2>
        <p class="meta"><strong>Автор:</strong> {book['dc:creator']}</p>
        <p class="meta"><strong>Рік видання:</strong> {book['dc:date']}</p>
        <p class="meta"><strong>Місце видання:</strong> {book['dc:coverage']}</p>
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
