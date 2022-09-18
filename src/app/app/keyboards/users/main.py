from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


politics_buttons: list[list[InlineKeyboardButton]] = [
    [
        InlineKeyboardButton(text='Принимаю', callback_data='accept'),
        InlineKeyboardButton(text='Не приминаю', callback_data='failure')
    ]
]
politics_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=politics_buttons)


from_buttons: list[list[InlineKeyboardButton]] = [
    [
        InlineKeyboardButton(text='Тема на форуме lolz', callback_data='lolz'),
        InlineKeyboardButton(text='Реклама', callback_data='advertisement'),
        InlineKeyboardButton(text='От друга', callback_data='friend'),
        InlineKeyboardButton(text='Другое', callback_data='other'),
     ]
]
from_keyboard = InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=from_buttons)
