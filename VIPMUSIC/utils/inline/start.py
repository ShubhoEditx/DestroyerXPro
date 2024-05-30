from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="♡ 𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐍𝙴𝚆 𝐆𝚁𝙾𝚄𝙿𝚂 ♡",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆ʀᴏᴜᴘ ♡", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ ♡", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="🕊️𝐒ʜᴜʙʜᴏ❤️",
                url=f"https://t.me/about_shubho",
            ),
            InlineKeyboardButton(
                text="❤️𝐒ᴏʜɪɴɪ🕊️",
                url=f"https://t.me/About_Sohini",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐅ᴇᴀᴛᴜʀᴇs ♡", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
