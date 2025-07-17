import hmac
import time
import base64
import hashlib
import telebot
import env


def generate_totp(secret: str) -> str:
    code = ''
    char = '23456789BCDFGHJKMNPQRTVWXY'

    hex_time = ('%016x' % (int(time.time()) // 30))
    byte_time = bytes.fromhex(hex_time)

    digest = hmac.new(base64.b64decode(secret),
                      byte_time, hashlib.sha1).digest()
    begin = ord(digest[19:20]) & 0xF
    c_int = int.from_bytes((digest[begin:begin + 4]), "big") & 0x7fffffff

    for r in range(5):
        code += char[int(c_int) % len(char)]
        c_int /= len(char)
    return code


class IsUser(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_user'

    @staticmethod
    def check(message: telebot.types.Message):
        return f'{message.from_user.id}' in env.USERS


bot = telebot.TeleBot(env.BOT_TOKEN)
bot.add_custom_filter(IsUser())


@bot.message_handler(is_user=False)
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Go away, it`s not for you, I`m a private bot")


@bot.message_handler(commands=['start', 'help'], is_user=True)
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to our cozy secret bot")


@bot.message_handler(commands=['steam'], is_user=True)
def send_totp(message):
    result = '\n'.join(
        list(f'{key}: {generate_totp(value)}' for key, value in env.STEAM_SECRETS.items()))
    bot.reply_to(message, result)


bot.infinity_polling()
