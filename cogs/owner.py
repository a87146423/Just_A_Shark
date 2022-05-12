import os

from disnake.ext import commands
from disnake import Permissions

class Restart(commands.Cog):
    """Slash command for restarting the bot."""
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='restart', description='Restart this bot.', default_member_permissions=Permissions(administrator=True))
    async def _restart(self, inter):
        await inter.response.send_message("Bot restarted.")
        token = os.environ.get("DC_TOKEN")
        await self.bot.close()
        await self.bot.start(token, reconnect=True)

def setup(bot):
    bot.add_cog(Restart(bot))
