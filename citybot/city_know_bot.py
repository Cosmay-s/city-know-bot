from citybot.data import load_cities as ls
import random 
import logging


logger = logging.getLogger(__name__)
cities = ls('cities-russia.txt')


def greet_user(update, context, user_id):
    update.message.reply_text('Привет, пользователь!\nИграем в города\nНачинай!')
    logger.info(f'Пользователь {user_id}: Начал игру')


def get_user_cities(context):
    if 'already_been' not in context.user_data:
        context.user_data['already_been'] = []
    return context.user_data['already_been']


def set_user_cities(context, cities_list):
    context.user_data['already_been'] = cities_list


def find_last_char(user_city):
    user_city = user_city[::-1]
    index = 0
    last_char = user_city[index]
    while last_char in ['ы', 'ь', 'ъ', 'й']:
        index += 1
        last_char = user_city[index]
    return last_char


def check_city(user_city, context):
    already_been = get_user_cities(context)
    if user_city in already_been:
        return 1 
    elif user_city not in cities[user_city[0].lower()]:
        return 2
    return 3


def check_responce(user_city, context):
    already_been = get_user_cities(context)
    if len(already_been) > 1:
        last_city = already_been[-1]
        if user_city[0].lower() != find_last_char(last_city.lower()):
            return 4
    return 5


def find_city(last_char, context, user_id):
    already_been = get_user_cities(context)
    city = random.choice(cities[last_char])
    if city not in already_been:
        return city
    while city in cities[last_char]:
        city_cash = []
        city_cash.append(city)
        logger.info(f'Пользователь {user_id}: Повторный поиск города для ответа вариант: {city}')
        if city not in already_been:
            return city
        
        if len(set(cities[last_char])) == len(set(city_cash)):
            logger.info(f'Пользователь {user_id}: кончились города')
            logger.info(f'{cities[last_char]}')
            logger.info(f'{city_cash}')
            return None
        city = random.choice(cities[last_char])



def check_user_responce(update, context, user_city, user_id, already_been):
    check = check_responce(user_city, context)
    if check == 4:
        update.message.reply_text(f'Не та буква. Последний город: {already_been[-1]}')
        logger.info(f'Пользователь {user_id}: Не та буква. Последний город: {already_been[-1]}')
    elif check == 5:
        city = find_city(find_last_char(user_city.lower()), context, user_id)
        already_been.append(user_city)
        logger.info(f'Пользователь {user_id}: Ответил город {user_city}')
        finish_check(update, context, city, already_been, user_id)

    set_user_cities(context, already_been)
    logger.info(f'Пользователь {user_id}: Обновленный список городов:\n {already_been}\n Городов в списке: {len(already_been)}')


def finish_check(update, context, city, already_been, user_id):
    if city:
        update.message.reply_text(f'{city}!\nТебе на {find_last_char(city.lower()).upper()}!')
        already_been.append(city)
        logger.info(f'Пользователь {user_id}: Получил в ответ {city}')
      
    else:
        update.message.reply_text('Конец')
        logger.info(f'Пользователь {user_id}: Конец игры')
            
def user_city_message_received(update, context):
    user_city = update.message.text
    user_id = update.message.from_user.id
    already_been = get_user_cities(context)

    check = check_city(user_city.capitalize(), context)
    if check == 1:
        update.message.reply_text(f'Город {user_city} уже был!')
        logger.info(f'Пользователь {user_id}: Город {user_city} уже был')
        return
    if check == 2:
        update.message.reply_text('Таких городов в нашей необьятной не имеется!')
        logger.warning(f'Пользователь {user_id}: Город {user_city} не найден в списке')
        return
    if check == 3:
        check_user_responce(update, context, user_city, user_id, already_been)
        