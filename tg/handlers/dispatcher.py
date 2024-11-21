from utils import *
from tg.bot import dp, bot


@dp.message(Command("start"))
async def callback_start(message: Message, state: FSMContext):
    print(await bot.get_updates())
    user = message.from_user
    web_app_info = WebAppInfo(url="https://trueandre091.github.io/firsty.github.io/")
    markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Open Web App", web_app=web_app_info)]])
    await message.answer(f'Hello, {user.first_name}!', reply_markup=markup)

