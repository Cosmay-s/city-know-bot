cities = [
    'Москва', 'Санкт-Петербург', 'Алматы', 'Киев', 'Ташкент', 'Минск', 'Баку', 'Ереван', 'Тбилиси', 'Челябинск',
    'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань', 'Самара', 'Ростов-на-Дону', 'Уфа', 'Красноярск', 'Омск', 'Саратов',
    'Воронеж', 'Пермь', 'Волгоград', 'Краснодар', 'Тюмень', 'Ижевск', 'Барнаул', 'Ульяновск', 'Сургут', 'Владивосток',
    'Ярославль', 'Махачкала', 'Рязань', 'Тольятти', 'Кемерово', 'Набережные Челны', 'Астрахань', 'Ставрополь', 'Калуга', 'Кострома',
    'Владимир', 'Сочи', 'Тверь', 'Бийск', 'Арзамас', 'Петрозаводск', 'Иркутск', 'Мурманск', 'Псков', 'Липецк',
    'Томск', 'Тула', 'Калининград', 'Чита', 'Симферополь', 'Абакан', 'Новороссийск', 'Оренбург', 'Вологда',
    'Смоленск', 'Курск', 'Миасс', 'Нижневартовск', 'Грозный', 'Таганрог', 'Курган', 'Подольск', 'Димитровград', 'Орёл',
    'Саранск', 'Северодвинск', 'Элиста', 'Пятигорск', 'Великий Новгород', 'Шахты', 'Нижнекамск', 'Тихорецк', 'Жуковский',
    'Туапсе', 'Рубцовск', 'Зеленоград', 'Ленинск-Кузнецкий', 'Нальчик', 'Железногорск', 'Салават', 'Ангарск', 'Ленинградская',
    'Абакан', 'Кострома', 'Нижний Тагил', 'Балаково', 'Заречный', 'Дзержинск', 'Энгельс', 'Уссурийск', 'Армавир',
    'Кисловодск', 'Североморск', 'Кунгур', 'Рославль', 'Калуга', 'Благовещенск', 'Серпухов', 'Тамбов', 'Губкин', 'Северск',
    'Новокузнецк', 'Химки', 'Долгопрудный', 'Красногорск', 'Брянск', 'Анапа', 'Североморск', 'Кострома',
    'Каменск-Уральский', 'Королёв', 'Люберцы', 'Шахты', 'Петрозаводск', 'Артём', 'Краснотурьинск', 'Уфа', 'Тула', 'Тимашевск',
    'Гатчина', 'Павлово', 'Иваново', 'Ярославль', 'Арзамас', 'Киров', 'Суздаль', 'Златоуст', 'Братск', 'Кисловодск',
    'Тамбов', 'Смоленск', 'Новороссийск', 'Хабаровск', 'Сызрань', 'Воркута', 'Орел', 'Сергиев Посад', 'Таганрог',
    'Урай', 'Новошахтинск', 'Троицк', 'Старый Оскол', 'Уфа', 'Жуковский', 'Чебоксары', 'Долгопрудный', 'Краснодар', 'Шадринск',
    'Петропавловск-Камчатский', 'Курск', 'Абакан', 'Псков', 'Томск', 'Рязань', 'Тольятти', 'Астрахань', 'Ессентуки', 'Нальчик',
    'Ногинск', 'Омск', 'Тверь', 'Таганрог', 'Черкесск', 'Ставрополь', 'Тихвин', 'Подольск', 'Чебоксары', 'Арзамас',
    'Заречный', 'Южно-Сахалинск', 'Шахты', 'Сосновый Бор', 'Воронеж', 'Туапсе', 'Лобня', 'Рязань', 'Электросталь',
    'Старый Оскол', 'Калуга', 'Оренбург', 'Набережные Челны', 'Новокузнецк', 'Димитровград', 'Красногорск', 'Балаково', 'Калуга',
    'Усть-Кут', 'Череповец', 'Тверь', 'Кемерово', 'Мурманск', 'Владикавказ', 'Бердск', 'Лениногорск',
    'Петрозаводск', 'Севастополь', 'Смоленск', 'Черногорск', 'Тула', 'Муром', 'Псков', 'Красноярск', 'Новороссийск',
    'Грозный', 'Петропавловск-Камчатский', 'Армавир', 'Тимашевск', 'Владикавказ', 'Саранск', 'Таганрог', 'Калуга', 'Ростов-на-Дону',
    'Луганск', 'Донецк', 'Харьков', 'Запорожье', 'Одесса', 'Львов', 'Мариуполь', 'Кривой Рог', 'Николаев', 'Чернигов',
    'Полтава', 'Винница', 'Житомир', 'Сумы', 'Ровно', 'Кременчуг', 'Луцк', 'Мелитополь', 'Черкассы', 'Камец-Подольский',
    'Ивано-Франковск', 'Тернополь', 'Черновцы', 'Желтые Воды', 'Никополь', 'Бердянск', 'Каховка', 'Севастополь', 'Калуш',
    'Краматорск', 'Симферополь', 'Борисполь', 'Конотоп', 'Мелитополь', 'Кривой Рог', 'Славянск', 'Северодонецк', 'Дружковка',
    'Краматорск', 'Макеевка', 'Лисичанск', 'Мариуполь', 'Артёмовск', 'Рубежное', 'Алчевск', 'Луганск', 'Белгород', 'Рязань',
    'Самара', 'Саранск', 'Сыктывкар', 'Брянск', 'Сургут', 'Липецк', 'Кемерово', 'Ростов-на-Дону', 'Краснодар',
    'Волгоград', 'Пермь', 'Тула', 'Мурманск', 'Томск', 'Ижевск', 'Воронеж', 'Астрахань', 'Тольятти',
    'Винница', 'Гродно', 'Владикавказ', 'Железногорск', 'Тамбов', 'Калуга', 'Астрахань', 'Саратов',
    'Калуга', 'Махачкала', 'Тула', 'Уфа', 'Кемерово', 'Томск', 'Сочи', 'Калининград', 'Вологда',
    'Нижневартовск', 'Чита', 'Симферополь', 'Севастополь', 'Лобня', 'Ярославль', 'Ростов-на-Дону', 'Иркутск',
    'Благовещенск', 'Ульяновск', 'Симферополь', 'Таганрог', 'Липецк', 'Черкесск', 'Псков', 'Элиста', 'Заречный', 'Норильск'
]

