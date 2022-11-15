import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBD1bz4x0zqW4D7FtgA_v-f5BZwvzCebbE1k4j_nF7ewZazQSlzkdvz2HPhqEkzoftNAmz1Cx1P5SJZun2vawxdQlOV3ohcx7hecJvIr8whyz3P5n5X4iWlkpFADI-Md3Jq8N1mHHHeO4bmMF3C6MK-2zNqp-5nquMihRLqZ0Cb2R2UK4QgKa-h9TuMFy2sTP2HQv3reBGIkKYoavhyFNTYVmg3Q2VwyaPCenyLXpHdLhmADgcY-aH7BQ5HF8cuk-vqu_7PpPJZNl7AEzLIIIlvddtXVwHM1ST0CJAIrB_Gjy_W9E5riCCMrbnIJnvEYo5GPuaDVKly_i7Z_UHKe0vvAAAAAVas6LwA")
BOT_TOKEN = getenv("BOT_TOKEN", "5634980934:AAErWBn1rmbh_klCYM5jsDHIZI-PjELVMCQ")
BOT_NAME = getenv("BOT_NAME", "NOT MUSIC")
API_ID = int(getenv("API_ID", "20763469")
API_HASH = getenv("API_HASH", "8f351d3e0c92bcdee35e5b94d411af01")
OWNER_NAME = getenv("OWNER_NAME", "amer")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "NottMusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "NotMussic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EvvEE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vvEE")
SUDO_USERS = getenv("SUDO_USERS", "1355557215")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8aeb92cd7cfb176a403e0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/67b2184e9ab3dbd8c3b27.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/0999c47b06173cf040137.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/017c27e00f1484491072f.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/27be9a2b467e5a91ac818.jpg")
