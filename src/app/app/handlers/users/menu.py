import datetime

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.models import User
from app.keyboards.users.menu import menu_buttons, profile_keyboard, service_keyboard

router = Router()


@router.message(text=menu_buttons[0][0].text)
async def btn_profile(message: Message, state: FSMContext) -> None:
    await state.clear()
    user = await User.get(id_tg=message.from_user.id).prefetch_related('advertisements', 'success')
    last_profit = user.last_profit if user.last_profit else 'Нет'
    await message.answer(f"""👨‍🔧 ВАШ ПРОФИЛЬ

🆔 Ваш ID: {message.from_user.id}
🤑 Баланс: {user.balance} RUB
📌 Ставка: оплата - 75% / возврат - 70%

🧾 Активных объявлений: {await user.advertisements.all().count()}
✂️ Успешных профитов: {await user.success.all().count()}
🐲 Ваш последний профит: {last_profit}

🌚 Вы с нами уже: {(datetime.datetime.today() - user.created_at).strftime('%d дней: %H часов %m')}
""", reply_markup=profile_keyboard)


@router.message(text=menu_buttons[0][1].text)
async def btn_service(message: Message, state: FSMContext) -> None:
    await message.answer('🗳 ВЫБЕРИТЕ ДЕЙСТВИЕ', reply_markup=service_keyboard)


@router.message(text=menu_buttons[1][0].text)
async def btn_about(message: Message, state: FSMContext) -> None:
    await message.answer(f""" 📝 ИНФОРМАЦИЯ О ПРОЕКТЕ

🕓 Дата открытия:  10.10.2020
👥  Воркеров:  {await User.all().count()}
💵  Выплаты:  Оплата - 75% | Возврат - 70%

СДЕЛАТЬ ССЫЛКИ НА ЧАТЫ""")
