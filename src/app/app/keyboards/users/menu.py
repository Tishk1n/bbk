from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

menu_buttons: list[list[KeyboardButton]] = [
    [
        KeyboardButton(text='👨‍🔧 Профиль')
    ],
    [
        KeyboardButton(text='🗳 Сервисы'),
        KeyboardButton(text='📝 О проекте')
    ]
]
menu_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=menu_buttons, resize_keyboard=True)


profile_buttons: list[list[InlineKeyboardButton]] = [
    [
        InlineKeyboardButton(text='Выплаты', callback_data='withoute')
    ],
    [
        InlineKeyboardButton(text='Карты мамонтов', callback_data='cards_people'),
        InlineKeyboardButton(text='Настройки', callback_data='settings')
     ],
    [
        InlineKeyboardButton(text='Реф.система', callback_data='referrals')
    ]
]
profile_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=profile_buttons)


service_buttons: list[list[InlineKeyboardButton]] = [
    [
        InlineKeyboardButton(text='СОЗДАТЬ', callback_data='create'),
        InlineKeyboardButton(text='ПОСМОТРЕТЬ', callback_data='show')
    ]
]
service_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=service_buttons)
