import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 29755489))

    API_HASH = os.environ.get("API_HASH", "05e0d957751c827aa03494f503ab54fe")
