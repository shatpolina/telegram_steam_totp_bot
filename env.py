from dotenv import load_dotenv
import os
import json

load_dotenv('.env')


def require_env_var(name, parser=None):
    value = os.getenv(name)
    if not value:
        print(f"Missing {name} in .env")
        quit()
    if parser:
        try:
            return parser(value)
        except Exception:
            print(f"{name} in .env is invalid")
            quit()
    return value


BOT_TOKEN: str = require_env_var("BOT_TOKEN")
STEAM_SECRETS: dict = require_env_var("STEAM_SECRETS", json.loads)
USERS: list = require_env_var("USERS")
