from citybot.data import load_cities as ls


already_been = []
cities = ls('cities-russia.txt')


def greet_user(update, context):
    update.message.reply_text('Привет, пользователь!\n Сыграем в города?')


def find_last_char(user_city):
    user_city = user_city[::-1]
    index = 0
    last_char = user_city[index]
    while last_char in ['ы', 'ь', 'ъ', 'й']:
        index += 1
        last_char = user_city[index]
    return last_char


def check_city(user_city):
    if user_city in already_been:
        return 1 
    elif user_city not in cities[user_city[0].lower()]:
        return 2
    return 3


def check_responce(user_city):
    if len(already_been) > 1:
        last_city = already_been[-1]
        if user_city[0].lower() != find_last_char(last_city.lower()):
            return 4
    return 5

def find_city(last_char):
    for city in cities[last_char]:
        if city not in already_been:
            return city 
    return None # конец игры

            
def user_city_message_received(update, context):
    user_city = update.message.text
    check = check_city(user_city.capitalize())
    if check == 1:
        update.message.reply_text(f'Город {user_city} уже был!')
    elif check == 2:
        update.message.reply_text('Таких городов в нашей необьятной не имеется!')
    elif check == 3:
        check = check_responce(user_city)
        if check == 4:
            update.message.reply_text(f'Не та буква. Последний город: {already_been[-1]}')
        elif check == 5:
            city = find_city(find_last_char(user_city.lower()))
            already_been.append(user_city)
            if city:
                update.message.reply_text(f'{city}! Тебе на {find_last_char(city.lower())}')
                already_been.append(city)
            else:
                update.message.reply_text('Конец')
                
