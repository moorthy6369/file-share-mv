#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a >RAMU</a>\n○ Language : <code>Python3</code>\n○ Library : <a>Pyrogram asyncio {__version__}</a>\n○ Join min channel : <a href='https://t.me/+DOarPPh720NhOTY1'>MV TAMILAN NETWORK</a>\n○ Request Channel : <a href='https://t.me/+EjLPqrfAXldkODE1'>MV TAMILAN CHAT</a>\n○ Support Group : <a href='https://t.me/+o9eFUVmKC11mOTVl'>MV TAMILAN BACKUP</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton("🔒 Close", callback_data = "close") ]
                ]
            )
        )