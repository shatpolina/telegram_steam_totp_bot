# telegram steam-totp bot
Private bot with time-based one-time password algorithm for Steam 

## Security disclaimer and advice
Bot privacy based on check tg user id. 
Algorithm functions purely offline, secrets saves in .env file. Only __you and yourself are responsible__ for security of your keys.

## How to use
Add to .env:  
    BOT_TOKEN - your bot token  
    STEAM_SECRETS - dict, where {name: secret}  
    USERS - list with permitted users (telegram user.id number)
    
    python ./main.py
## Credits
Credit to [ran-sama](https://github.com/ran-sama) for the [steam_totp algorithm](https://github.com/ran-sama/python3-steam-authenticator)
