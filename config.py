import  os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

youtube_next_fetch = 0  # time in minute


@bot.on_message(Filters.command('start') & Filters.private)
async def start(bot, update):
    await update.reply(
        f"**Hi {update.chat.first_name} 👋**\n\n"
        "I am shortlink bot. Just send me link and get adsless short link. \n\nBot Created ❤️ 🇱🇰 by @im_KeKO")

EDIT_TIME = 5
