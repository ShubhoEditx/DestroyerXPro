import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat, add_served_chat
from VIPMUSIC.utils.database import get_assistant


photo = [
    "https://telegra.ph/file/57d5705756c589e14a1a3.jpg",
    "https://telegra.ph/file/ea3c012fdde82812a5a73.jpg",
    "https://telegra.ph/file/f86bac9f1576697c69669.jpg",
    "https://telegra.ph/file/a13a059b486d096cbc7ba.jpg",
    "https://telegra.ph/file/95281ac786e89c37d3edd.jpg",
]

from strings.__init__ import LOGGERS


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** {message.chat.id}\n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"😍𝐀ᴅᴅᴇᴅ 𝐁ʏ😍",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await add_served_chat(message.chat.id)
                await userbot.join_chat(f"{username}")
                oks = await userbot.send_message(LOGGERS, f"/start")
                Ok = await userbot.send_message(
                    LOGGERS, f"#{app.username}\n@{app.username}"
                )
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()

    except Exception as e:
        print(f"Error: {e}")
