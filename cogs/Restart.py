import os
import requests
from disnake.ext import commands

class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='restart', description='Restart this bot.')
    @commands.has_permissions(ban_members=True)
    async def _restart(self, inter):
        TOKEN = os.environ.get("DC_TOKEN")
        await self.bot.close()
        await self.bot.start(TOKEN, reconnect=True)

    @commands.slash_command(name='xratelimit', description='Check x-RateLimit.')
    @commands.has_permissions(ban_members=True)
    async def _check_x_ratelimit(self, inter):
        r = requests.head(url="https://discord.com/api/v1")
        try:
            await inter.response.send_message(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left", ephemeral=True)
        except:
            await inter.response.send_message(f"No rate limit, Remaining: {int(r.headers['X-RateLimit-Remaining']) / 60}", ephemeral=True)

def setup(bot):
    bot.add_cog(Restart(bot))