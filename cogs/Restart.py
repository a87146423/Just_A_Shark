import os
import requests
from disnake.ext import commands

class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='restart', description='Restart this bot.')
    @commands.has_permissions(ban_members=True)
    async def _restart(self, inter):
        await inter.response.send_message(f"Bot restarted.")
        TOKEN = os.environ.get("DC_TOKEN")
        await self.bot.close()
        await self.bot.start(TOKEN, reconnect=True)

def setup(bot):
    bot.add_cog(Restart(bot))