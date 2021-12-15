import os
import disnake

from disnake.ext import commands

def get_prifex(bot, msg):
    if msg.author != bot.user:
        return ['a!', 'A!']

intents = disnake.Intents().all()
bot = commands.Bot(command_prefix=get_prifex, case_insensitive=True, intents=intents, sync_commands_debug=True, sync_permissions=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="蝦蝦✅"))
    print(f"Logged in as: {bot.user.name} - {bot.user.id} / Version: {disnake.__version__}")


if __name__ == "__main__":
    for Filename in os.listdir('private_cogs'):
        try:
            bot.load_extension(f"{'private_cogs'}.{Filename[:-3]}")
        except Exception as e:
            print(e)
        else:
            print(f"{'private_cogs'}.{Filename[:-3]} is loaded.")

    for Filename in os.listdir('cogs'):
        try:
            bot.load_extension(f"{'cogs'}.{Filename[:-3]}")
        except Exception as e:
            print(e)
        else:
            print(f"{'cogs'}.{Filename[:-3]} is loaded.")

    TOKEN = os.environ.get("DC_TOKEN")
    bot.run(TOKEN)
