from os import getenv

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.database.models import User
from app.errors.users.url_error import UrlError
from app.keyboards.users.main import politics_keyboard, from_keyboard
from app.keyboards.users.menu import menu_keyboard
from app.states.users.main import AcceptStates
from app.utils.serializer import convert_from_dict_to_str

router = Router()
channel_id = getenv('CHANNEL_ID')


@router.message(Command(commands='start'))
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    if await User.exists(id_tg=message.from_user.id):
        user = await User.get(id_tg=message.from_user.id)
        if user.active:
            await message.answer('🧾 Меню', reply_markup=menu_keyboard)
            return
        await message.answer('Ожидайте проверки администратора')
        return
    await message.answer(f"""
Добро пожаловать в 🔥 GARAGE TEAM BOT 🔥!

Ознакомьтесь с нашими правилами:

1️⃣ Запрещено медиа с некорректным содержанием (порно, насилие, убийства, призывы к экстремизму, реклама наркотиков).
2️⃣ Запрещен спам, флуд, пересылки с других каналов, ссылки на сторонние ресурсы.
3️⃣ Запрещено оскорбление воркеров/администраторов, неадекватное поведение.
4️⃣ Запрещено попрошайничество в беседе воркеров.
5️⃣ Отправка бтк чеков только в курилке.

Вы принимаете правила нашей команды?""", reply_markup=politics_keyboard)
    await state.set_state(AcceptStates.CHOICE)


@router.callback_query(AcceptStates.CHOICE, text='accept')
async def btn_accept(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer('❔ Как вы узнали о нашей команде?', reply_markup=from_keyboard)
    await state.set_state(AcceptStates.FROM)


@router.callback_query(AcceptStates.FROM)
async def btn_from(call: CallbackQuery, state: FSMContext) -> None:
    match call.data:
        case 'lolz':
            msg: str = 'Введите ссылку на обсуждение в lolz'
        case 'advertisement':
            msg: str = 'Введите ссылку на группу с рекламой'
        case 'friend':
            msg: str = 'Отправьте ссылку на вашего друга'
        case _:
            msg: str = 'Введите ссылку на источник, из которого вы узнали о нас'
    await state.update_data(source=call.data)
    await call.message.answer(msg)
    await state.set_state(AcceptStates.URL)


@router.message(AcceptStates.URL)
async def get_url(message: Message, state: FSMContext) -> None:
    msg: str = '🌋 Если вы находились/находитесь в данный момент в другой тиме, почему решили перейти в нашу команду?'
    if '@' in message.text or 'http' in message.text:
        await message.answer(msg)
        await state.update_data(url=message.text)
        await state.set_state(AcceptStates.WHY)
        return
    raise UrlError


@router.message(AcceptStates.WHY)
async def get_why(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(why=message.text)
    data: dict = await state.get_data()
    msg: str = 'Ваша заявка отправлена на рассмотрение'
    await User(id_tg=message.from_user.id).save()
    await message.answer(msg)
    await state.clear()
    await bot.send_message(channel_id, convert_from_dict_to_str(message.from_user.id, data))


@router.callback_query(text='failure')
async def btn_failure(call: CallbackQuery, state: FSMContext) -> None:
    msg: str = 'Для использования данного бота вам необходимо принять правила!'
    await call.message.answer(msg, reply_markup=politics_keyboard)
