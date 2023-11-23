import re
def format_phone_number(phone_number):
    # Удаляем все символы, кроме цифр
    cleaned_number = re.sub(r'\D', '', phone_number)
    # Проверяем на корректность введенного номера
    if len(cleaned_number) != 11:
        return "Некорректный номер телефона"
    # Форматируем номер в требуемом формате
    formatted_number = f"+7-{cleaned_number[1:4]}-{cleaned_number[4:7]}-{cleaned_number[7:9]}-{cleaned_number[9:11]}"
    return formatted_number




