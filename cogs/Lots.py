import random

from datetime import datetime, timedelta
from disnake import Embed
from disnake.ext import commands
from data import lots

LOTS = lots.LOTS

class DrawLots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='lots', description='抽籤！每日早上八點重置')
    async def _draw_lots(self, inter):
        seed = int((datetime.now() + timedelta(hours=8)).strftime(f'%Y%m%d')) + inter.author.id
        embed = self.createEmbed(inter, seed)
        await inter.response.send_message(content=f'{inter.author.mention}你今天的運勢是...',embed=embed)

    def createEmbed(self, inter, seed):
        random.seed(seed)
        n = random.randint(0, 99)
        result = LOTS[n]

        date = (datetime.now() + timedelta(hours=8)).strftime(f'%Y年%m月%d日'.encode('unicode_escape').decode('utf8')).encode('utf-8').decode('unicode_escape')
        desc = "**{}**\n".format(result["poem_line1"])
        desc+= "`{}`\n".format(result["poem_line1_explain"])
        desc+= "**{}**\n".format(result["poem_line2"])
        desc+= "`{}`\n".format(result["poem_line2_explain"])
        desc+= "**{}**\n".format(result["poem_line3"])
        desc+= "`{}`\n".format(result["poem_line3_explain"])
        desc+= "**{}**\n".format(result["poem_line4"])
        desc+= "`{}`\n".format(result["poem_line4_explain"])
        embed = Embed(title=f"{date}💮{result['title']}籤-{result['status']}", description=desc, color=inter.author.color, timestamp=datetime.now())
        payload = result['payload']
        for key in payload:
            embed.add_field(name=key, value=payload[key], inline=True)
        embed.set_footer(text=f"{inter.author.name}#{inter.author.discriminator}")
        return embed

        
def setup(bot):
    bot.add_cog(DrawLots(bot))