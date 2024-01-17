import logging
from aiogram import Bot, Dispatcher, executor, types
from inline_btn import *
from database import *
from utils import translate_text

BOT_TOKEN = '6690583551:AAH6z-iD8dMJ8qycyzrh8BKVLRibRhdRElU'
ADMINS = [848376593]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot)


async def command_menu(dp: Dispatcher):
    await create_tables()
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'start to translate'),
            types.BotCommand('stats', 'users\' statistics'),
            types.BotCommand('id', 'get your telegram-id'),
        ]
    )


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer(f"Hello, @{message.from_user.username}. Welcome to translator bot")


@dp.message_handler(commands=['stats'])
async def get_user_stats_handler(message: types.Message):
    if message.from_user.id in ADMINS:
        count = await get_all_users()
        await message.answer(f"Bot users number: {count}")


@dp.message_handler(commands=['id'])
async def get_id_handler(message: types.Message):
    await message.answer(f"{message.from_user.id}")


@dp.message_handler(content_types=['text'])
async def get_user_text_handler(message: types.Message):
    btn = await translate_langs_btn()
    await message.answer(text=message.text, reply_markup=btn)


@dp.callback_query_handler(text_contains='lang')
async def selected_lang_callback(call: types.CallbackQuery):
    lang = call.data.split(':')[-1]
    text = call.message.text
    result_text = await translate_text(text=text, lang=lang)
    btn = await translate_langs_btn()
    await call.message.edit_text(text=result_text, reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=command_menu)
    print("End")
