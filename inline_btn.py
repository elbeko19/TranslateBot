from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def translate_langs_btn():
    btn = InlineKeyboardMarkup(row_width=2)

    btn.add(
        InlineKeyboardButton(
            text="RU🇷🇺", callback_data='lang:ru'
        ),
        InlineKeyboardButton(
            text="UZ🇺🇿", callback_data='lang:uz'
        ),
        InlineKeyboardButton(
            text="EN🇺🇸", callback_data='lang:en'
        ),
        InlineKeyboardButton(
            text="DE🇩🇪", callback_data='lang:de'
        ),
        InlineKeyboardButton(
            text="FR🇫🇷", callback_data='lang:fr'
        ),
        InlineKeyboardButton(
            text="IT🇮🇹", callback_data='lang:it'
        ),
    )
    return btn
