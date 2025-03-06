
from data import cities
from city_parser import load_cities


def greet_user(update, context):
    update.message.reply_text('Привет, пользователь!\n Сыграем в города?')


already_been = []
cities = list(cities)


def already_been_check(update, user_city):
    if user_city in already_been:
        update.message.reply_text(f'Город {user_city} уже был!')
        return False
    elif user_city not in cities:
        update.message.reply_text('Я про такие города не слышал!')
        return False
    elif already_been:
        last_city = already_been[-1]
        if user_city[0].lower() != find_last_char(last_city.lower()):
            update.message.reply_text(f'Не та буква. Последний город: {last_city}')
            return False

    already_been.append(user_city)
    return True


def find_city(last_char):
    for city in cities:
        if city not in already_been and city[0].lower() == last_char:
            already_been.append(city)
            return city
    return False

def find_last_char(user_city):
    user_city = user_city[::-1]
    index = 0
    last_char = user_city[index]
    while last_char in ['ы', 'ь', 'ъ']:
        index += 1
        last_char = user_city[index]
    return last_char
            

def play_city_game(update, context):
    user_city = update.message.text
    if already_been_check(update, user_city.capitalize()):
            last_char = find_last_char(already_been[-1].lower())
            answer_city = find_city(last_char)           
            if answer_city:
                update.message.reply_text(f'{answer_city}! Тебе на {find_last_char(answer_city.lower())}!')
            else:
                update.message.reply_text('Конец парам пам')

