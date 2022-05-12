from disnake.ext import commands

class Misc(commands.Cog):
    """Misc slash commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ping', description='Ping! Pong!')
    async def _ping(self, inter):
        await inter.response.send_message(f'{round(self.bot.latency*1000)}ms')

    @commands.slash_command(name='repeat', description='Repeat what you said.')
    async def _repeat(self, inter, text:str):
        await inter.response.send_message(text)

def setup(bot):
    bot.add_cog(Misc(bot))
