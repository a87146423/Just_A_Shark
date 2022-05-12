import os

from disnake.ext import commands

class Restart(commands.Cog):
    """Slash command for restarting the bot."""
    def __init__(self, bot):
        self.bot = bot

    def check_if_owner(self, ctx):
        owner_id = int(os.environ.get("OWNER_ID"))
        return ctx.message.author.id == owner_id

    @commands.slash_command(name='restart', description='Restart this bot.')
    @commands.has_permissions(ban_members=True)
    @commands.check(check_if_owner)
    async def _restart(self, inter):
        await inter.response.send_message("Bot restarted.")
        token = os.environ.get("DC_TOKEN")
        await self.bot.close()
        await self.bot.start(token, reconnect=True)

def setup(bot):
    bot.add_cog(Restart(bot))
