from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import FindTyresFortochki
from keyboards.reply import exit_kb, main_kb
from data.get_find_tyre_fortochki import get_find_tyre_fortochki

router = Router()


@router.message(F.text.lower() == "найти шины в форточках")
async def get_tyres_fortochki(message: Message, state: FSMContext):
    await state.set_state(FindTyresFortochki.tyre_data)
    await message.answer("Введи строку в формате: 205 55 16 зима шип", reply_markup=exit_kb)


@router.message(FindTyresFortochki.tyre_data)
async def find_tyres(message: Message, state: FSMContext):
    await state.update_data(find_tyres=message.text)

    if message.text.lower() == "exit":
        await state.clear()
        await message.answer("Выходим", reply_markup=main_kb)
    else:
        data_tyre = message.text.lower().strip()
        data_tyre = " ".join(data_tyre.split())
        tyre_param_all = data_tyre.split()
        diametr_tyre = tyre_param_all[2]
        width_tyre = tyre_param_all[0]
        height_tyre = tyre_param_all[1]
        thorn_tyre = False

        if 'лет' in tyre_param_all[3]:
            season_tyre = ['s', 'u']
        else:
            season_tyre = ['w']

        if len(tyre_param_all) > 4 and 'шип' in tyre_param_all[4]:
            thorn_tyre = True

        await message.reply(
            f"Ширина: {width_tyre}\n"
            f"Высота: {height_tyre}\n"
            f"Диаметр: {diametr_tyre}\n"
            f"Сезон: {season_tyre}\n"
            f"Шип: {thorn_tyre}\n"
        )

        list_of_tyres = get_find_tyre_fortochki(diameter=int(diametr_tyre), height=int(height_tyre),
                                                season=season_tyre, width=int(width_tyre), thorn=thorn_tyre)
        list_of_tyres = "\n".join(list_of_tyres)
        await message.answer(list_of_tyres, reply_markup=exit_kb)
