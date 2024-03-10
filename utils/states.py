from aiogram.fsm.state import StatesGroup, State


class FindTyresFortochki(StatesGroup):
    tyre_data = State()
