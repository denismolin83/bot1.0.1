# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
# from utils.states import FindTyresFortochki
#
# router = Router()
#
#
# # @router.message(F.text.lower() == "найти шины в форточках")
# # async def get_tyres_fortochki(message: Message, state: FSMContext):
# #     await state.set_state(FindTyresFortochki.tyre_data)
# #     await message.answer("Введи строку в формате: 205 55 16 зима шип")