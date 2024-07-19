from aiogram.fsm.context import FSMContext


async def check_time(state: FSMContext):
    time = await state.get_data()
    try:
        int(time["year"])
    except:
        return False
    try:
        int(time["month"])
    except:
        return False
    try:
        int(time["day"])
    except:
        return False
    try:
        int(time["hour"])
    except:
        return False
    try:
        int(time["minute"])
    except:
        return False
    return True
