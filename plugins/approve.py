from pyrogram import Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Script import script
from info import PICS
from utils import temp
import random


@Client.on_chat_join_request()
async def accept_request(client, r):

    buttons = [
        [
            InlineKeyboardButton('➕ 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ➕', url=f"http://t.me/{temp.U_NAME}?startgroup=true")
        ],[
            InlineKeyboardButton('🛡 𝖮𝗐𝗇𝖾𝗋', callback_data="owner_info"),
            InlineKeyboardButton('🧩 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉', url=f"https://t.me/{SUPPORT_CHAT}")
        ],[
            InlineKeyboardButton('ℹ️ 𝖧𝖾𝗅𝗉', callback_data='help'),
            InlineKeyboardButton('😊 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
        ],[
            InlineKeyboardButton('🔎 𝖨𝗇𝗅𝗂𝗇𝖾 𝖲𝖾𝖺𝗋𝖼𝗁', switch_inline_query_current_chat='')
        ]]
    
    await client.send_photo(
        r.from_user.id,
        random.choice(PICS),
        script.START_TXT.format(r.from_user.mention, temp.U_NAME, temp.B_NAME),
        enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(buttons))

    await r.approve()
