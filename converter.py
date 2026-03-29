import json
# 1. Створюємо порожній список
digital_archive = []
# 2. Відкриваємо файл із даними для читання ('r' - read)
with open('books.txt', 'r', encoding='utf-8') as file:
    
    # Запускаємо конвеєр: беремо по одному рядку з файлу
    for line in file:
        
        # Очищаємо рядок від прихованих символів (наприклад, переносу 
        # рядка) і розбиваємо його на частини там, де стоїть кома
        parts = line.strip().split(',')
        
      # 3. Формуємо словник за стандартом Dublin Core
    # У програмуванні рахунок починається з нуля, тому перша частина
   # - це parts[0]
        metadata = {
            "dc:title": parts[0],      # Назва (Кобзар)
            "dc:creator": parts[1],    # Автор (Тарас Шевченко)
            "dc:date": parts[2],       # Рік (1840)
            "dc:coverage": parts[3],   # Місце (Київ)
            "dc:format": "application/pdf", # додаємо технічні метадані
            "dc:language": parts[4]
          
        }
        
               # Додаємо готову картку до списку
        digital_archive.append(metadata)
# 4. Зберігаємо результат у форматі JSON ('w' - write)
with open('archive_metadata.json', 'w', encoding='utf-8') as f:
    # Записуємо список у файл красиво (з відступами, indent=4) і зберігаючи кирилицю
    json.dump(digital_archive, f, ensure_ascii=False, indent=4)
print("Конвертація завершена! Перевірте файл archive_metadata.json")