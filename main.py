import traceback
import os

import disnake
from disnake.ext import commands

def fancy_traceback(exc: Exception) -> str:
    """May not fit the message content limit"""
    text = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    return f"```py\n{text[-4086:]}\n```"

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='a!',
            help_command=None,
            intents=disnake.Intents().all(),
            sync_commands_debug=True,
            sync_permissions=True
        )

    def load_all_extensions(self, folder: str) -> None:
        for filename in os.listdir(folder):
            try:
                self.load_extension(f"{folder}.{filename[:-3]}")
            except Exception as e:
                print(e)
            else:
                print(f"{folder}.{filename[:-3]} loaded.")

bot = Bot()
bot.load_all_extensions('private_cogs')
bot.load_all_extensions('cogs')
bot.run(os.environ.get("DC_TOKEN"))

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="蝦蝦✅"))
    print(f"Logged in as: {bot.user.name} - {bot.user.id} / Version: {disnake.__version__}")

