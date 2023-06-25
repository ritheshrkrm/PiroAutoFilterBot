from pyrogram import Client, enums, filters
from pyrogram.types import Message, User, ChatJoinRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Script import script
from info import REQ_PICS
from utils import temp
import random


@Client.on_chat_join_request()
async def accept_request(client, r):
    chat=message.chat 
    user=message.from_user 

    buttons = [
        [
            InlineKeyboardButton('❤️‍🔥 𝖡𝖫𝖠𝖲𝖳𝖤𝖱 𝖧𝖴𝖡 ❤️‍🔥', url="https://https://t.me/blaster_hub"),
            InlineKeyboardButton('⚡𝖴𝗉𝖽𝖺𝗍𝖾𝗌 ⚡', url="https://t.me/piroxbots")
        ]]
    
    await client.send_photo(
        r.from_user.id,
        random.choice(REQ_PICS),
        script.REQ_TXT.format(r.from_user.mention, chat.title),
        enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(buttons))

    await r.approve()
