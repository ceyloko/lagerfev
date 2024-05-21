import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("27182917"))
    API_HASH = os.environ.get("e627c805adc5719f484d84fc829bc11b")
    BOT_TOKEN = os.environ.get("6817520332:AAFW4PCppQlrjaLo1Rhsic4Vz2lNwxsFpH4")
    BOT_USERNAME = os.environ.get("feverantaggerbot")
    BOT_NAME = os.environ.get("FeveranTaggerBot")
    BOT_ID = int(os.environ.get("6817520332"))
    SUDO_USERS = os.environ.get("1111099757").split()
    SUPPORT_CHAT = os.environ.get("https://t.me/feveranchat")
    OWNER_ID = int(os.environ.get("1111099757"))
    OWNER_USERNAME = os.environ.get("yusufuslu")
