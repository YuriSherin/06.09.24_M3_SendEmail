# Задача "Рассылка писем"

def check_string(s):
    """Функция проверяет наличие в строке '@', а также, что строка оканчивается на '.ru', '.com', '.net'"""
    result = False      # Результат работы функции. Изначально примем как False
    i = s.rfind('.')    # Находим индекс '.' в строке. Поиск символа начинаем справа
    if i < 0:           # Символ '.' в строке не найден
        return result   # Выходим из функции с result = False
    s1 = s[i:]          # Получаем подстроку от индекса до конца строки
    if '@' in s and (s1 == '.ru' or s1 == '.com' or s1 == '.net'):  # Если условие выполняется
        result = True   # Результат True
    return result

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    """Функция отправляет <message> от <sender> к <recipient> и выводит сообщение в консоль"""
    f1 = check_string(recipient)    # Проверим состояние адреса получателя
    f2 = check_string(sender)       # Проверим состояние адреса отправителя
    if not f1 or not f2:            # Если с адресами что-то не так
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')    # Выводим сообщение
    elif recipient.lower() == sender.lower():   # Если адрес отправителя равен адресу получателя
        print('Нельзя отправить письмо самому себе!')   # Выводим сообщение
    elif sender.lower() == 'university.help@gmail.com'.lower(): # Если адрес отправителя по умолчанию
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.') # Выводим сообщение
    else:   # Если предыдущие условия не сработали, выводим сообщение
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# ================== Правильные тестовые выводы сообщений в консоль =======================
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!
