from aiogram.fsm.state import StatesGroup, State


class FindTyresFortochki(StatesGroup):
    tyre_data = State()
    mask_data = State()
