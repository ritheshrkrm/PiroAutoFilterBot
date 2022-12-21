# Separate channel to be created and bot to be added as admin. when the file forwarded to the this channel, then the file will be deleted from database. (This will help to eliminate time while delete file by forward file to bot and reply /delete command each time for each file)
import re
import logging
from pyrogram import Client, filters
from info import DELETE_CHANNELS
from database.ia_filterdb import Media, unpack_new_file_id

logger = logging.getLogger(__name__)

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(DELETE_CHANNELS) & media_filter)
async def deltemedia(bot, message):
    """Delete file from database"""
    reply = message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
        pass
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    file_id, file_ref = unpack_new_file_id(media.file_id)

    result = await Media.collection.delete_one({
        '_id': file_id,
    })
    if result.deleted_count:
        logger.info('File is successfully deleted from database')
    else:
        file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
        result = await Media.collection.delete_many({
            'file_name': file_name,
            'file_size': media.file_size,
            'mime_type': media.mime_type
            })
        if result.deleted_count:
            logger.info('File is successfully deleted from database')
        else:
            result = await Media.collection.delete_many({
                'file_name': media.file_name,
                'file_size': media.file_size,
                'mime_type': media.mime_type
            })
            if result.deleted_count:
                logger.info('File is successfully deleted from database')
            else:
                logger.info('File not found in database')
