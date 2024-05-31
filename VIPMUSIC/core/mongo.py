from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "𝐍ᴏ 𝐌ONGO 𝐃B 𝐔RL 𝐅ᴏᴜɴᴅ.. 𝐘ᴏᴜʀ 𝐁ᴏᴛ 𝐖ɪʟʟ 𝐖ᴏʀᴋ 𝐎ɴ 𝐒𝐎𝐇𝐈𝐍𝐈 𝐌𝐔𝐒𝐈𝐂 𝐃ᴀᴛᴀʙᴀsᴇ"
    )
    temp_client = Client(
        "VIPMUSIC",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    pymongodb = _mongo_sync_.Anon
