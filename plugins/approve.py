from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Script import script
from info import REQ_PICS
from utils import temp
import random


@Client.on_chat_join_request()
async def accept_request(client, r):
buttons = [[
    InlineKeyboardButton("❤️‍🔥 𝖡𝖫𝖠𝖲𝖳𝖤𝖱 𝖧𝖴𝖡 ❤️‍🔥", url=f"https://https://t.me/blaster_hub"),
    InlineKeyboardButton("⚡𝖴𝗉𝖽𝖺𝗍𝖾𝗌 ⚡", url=f"https://t.me/piroxbots")
]]
    
    await client.send_photo(
        r.from_user.id,
        random.choice(REQ_PICS),
        script.REQ_TXT.format(r.from_user.mention, temp.U_NAME, temp.B_NAME),
        enums.ParseMode.HTML,
        reply_markup = InlineKeyboardMarkup(buttons))

    await r.approve()
