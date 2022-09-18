from aiogram.fsm.state import StatesGroup, State


class AcceptStates(StatesGroup):
    CHOICE = State()
    FROM = State()
    URL = State()
    WHY = State()
