import json
# КРОК 1: Завантаження даних із бази
with open('archive_metadata.json', 'r', encoding='utf-8') as file:
    digital_archive = json.load(file)

# КРОК 1.5
def format_year(year):
    if year and str(year).strip():
        return f"Видано у {year} р."
    else:
        return "Рік видання невідомий"

# Крок 1.6
def get_card_color(year):
    """
    Повертає CSS-колір для лівої смужки картки
    залежно від епохи книги.
    """
    try:
        year_int = int(year)
    except (ValueError, TypeError):
        return "#95a5a6"  # Сірий — якщо рік невідомий або не є числом

    if year_int < 1800:
        return "#8e44ad"  # Фіолетовий — XVIII ст. і раніше
    elif year_int < 1900:
        return "#e74c3c"  # Червоний — XIX ст.
    elif year_int < 2000:
        return "#e67e22"  # Помаранчевий — XX ст.
    else:
        return "#27ae60"  # Зелений — XXI ст.

###


###

# КРОК 2: Створення функції-шаблонізатора
def generate_html_card(book, index):
    """
    Генерує картку для головної сторінки каталогу.
    Тепер приймає також порядковий номер (index)
    для формування посилання на детальну сторінку.
    """
    year = book.get('dc:date', '')
    color = get_card_color(year)
    detail_page = f"book_{index + 1}.html"

    card_html = f"""
        <div class="card" style="border-left-color: {color};">
            <h2>{book.get('dc:title', 'Невідома назва')}</h2>
            <p><strong>Автор:</strong> {book.get('dc:creator', 'Невідомий автор')}</p>
            <p><strong>Рік:</strong> {format_year(year)}</p>
            <p><strong>Місце:</strong> {book.get('dc:coverage', 'Невідомо')}</p>
            <p><strong>Мова:</strong> {book.get('dc:language', 'Невідомо')}</p>
            <a href="{detail_page}">Детальніше →</a>
        </div>
    """

    return card_html

####

###

# КРОК 3: Підготовка базового каркаса сторінки (HTML+CSS)
html_start = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Цифровий архів</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Колекція рідкісних видань</h1>
    <div class="gallery">
"""
html_end = """
    </div>
</body>
</html>
"""


def generate_detail_page(book, index):
    """
    Генерує повну HTML-сторінку для однієї книги.
    """
    year = book.get('dc:date', '')
    color = get_card_color(year)

    # Умовна мітка антикваріату — перше самостійне застосування if
    if year.isdigit() and int(year) < 1900:
        antique_badge = '<span class="badge">[Антикваріат]</span>'
    else:
        antique_badge = ''

    page_html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{book.get('dc:title', 'Книга')}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <a href="index.html">← Повернутися до каталогу</a>
    <div class="detail-card" style="border-left-color: {color};">
        <h1>{book.get('dc:title', 'Невідома назва')} {antique_badge}</h1>
        <p><strong>Автор:</strong> {book.get('dc:creator', 'Невідомий автор')}</p>
        <p><strong>Рік видання:</strong> {year}</p>
        <p><strong>Місце видання:</strong> {book.get('dc:coverage', 'Невідомо')}</p>
        <p><strong>Мова:</strong> {book.get('dc:language', 'Невідомо')}</p>
        <p><strong>Формат:</strong> {book.get('dc:format', 'Невідомо')}</p>
    </div>
</body>
</html>"""

    return page_html


# ── КРОК 4: Генерація всіх сторінок ─────────────────────────────
all_cards_code = ""

for i, item in enumerate(digital_archive):

    # 4а. Генеруємо картку для головної сторінки
    all_cards_code += generate_html_card(item, i)

    # 4б. Генеруємо і одразу зберігаємо окрему детальну сторінку
    detail_html = generate_detail_page(item, i)
    detail_filename = f"book_{i + 1}.html"
    with open(detail_filename, 'w', encoding='utf-8') as detail_file:
        detail_file.write(detail_html)

print(f"Згенеровано {len(digital_archive)} детальних сторінок.")




# КРОК 5: Збирання та збереження фінального файлу
final_html = html_start + all_cards_code + html_end
with open('index.html', 'w', encoding='utf-8') as output_file:
    output_file.write(final_html)
print("Генерація успішна! Файл index.html оновлено.")
