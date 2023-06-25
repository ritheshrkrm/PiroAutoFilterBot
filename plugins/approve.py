from pyrogram import Client

@Client.on_chat_join_request()
async def accept_request(client, r):
    
    try:
        await client.send_message(r.from_user.id,
            f"Hello {r.from_user.mention}\nWelcome to {r.chat.title}\nYou Request Have Been Accepted...!!!")

    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")

    await r.approve()
