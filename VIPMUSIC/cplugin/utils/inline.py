from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝐂ʟᴏsᴇ ♡", callback_data="close")]]
)
