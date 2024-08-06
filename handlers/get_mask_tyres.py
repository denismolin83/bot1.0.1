from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import FindTyresFortochki
from keyboards.reply import exit_kb, main_kb
from data.get_find_tyre_fortochki import get_find_tyre_fortochki

router = Router()


@router.message(F.text.lower() == "найти шины по маскам")
async def get_mask_tyres_fortochki(message: Message, state: FSMContext):
    await state.set_state(FindTyresFortochki.mask_data)

    list_mask_tyres_dict = [
        {'width': 185, 'height': 65, 'diameter': 15, 'season': ['s', 'u'],
         'thorn': False, 'wrh_list': [1015], 'brand_list': ['']},
        {'width': 245, 'height': 45, 'diameter': 20, 'season': ['w'],
         'thorn': True, 'wrh_list': [1015], 'brand_list': ['']},
        {'width': 215, 'height': 55, 'diameter': 18, 'season': ['w'],
         'thorn': True, 'wrh_list': [1015], 'brand_list': ['']},
        {'width': 245, 'height': 55, 'diameter': 19, 'season': ['w'],
         'thorn': True, 'wrh_list': [1015], 'brand_list': ['']}
    ]

    for mask_tyre in list_mask_tyres_dict:
        # print(mask_tyre)
        await message.answer(f"{mask_tyre['width']}/{mask_tyre['height']} R{mask_tyre['diameter']} "
                             f"{mask_tyre['season']} ш: {mask_tyre['thorn']}")
        list_of_tyres = get_find_tyre_fortochki(diameter=mask_tyre['diameter'],
                                                height=mask_tyre['height'],
                                                season=mask_tyre['season'],
                                                width=mask_tyre['width'],
                                                thorn=mask_tyre['thorn'])
        if list_of_tyres:
            list_of_tyres_message = "\n".join(list_of_tyres)
            # print(list_of_tyres_message)
            await message.answer(list_of_tyres_message)

    await message.answer("---Поиск закончен---", reply_markup=exit_kb)


@router.message(F.text.lower() == "exit")
async def exit_mask_tyres(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выходим", reply_markup=main_kb)
