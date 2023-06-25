from pyrogram import Client


@Client.on_chat_join_request()
async def accept_request(_, r):
    await r.approve()
