from datetime import datetime

import random
import pytz

from disnake import Embed
from disnake.ext import commands

from data import lots

LOTS = lots.LOTS

class DrawLots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='lots', description='抽籤！每日早上八點重置')
    async def _draw_lots(self, inter) -> None:
        seed = int(datetime.now().strftime('%Y%m%d')) + inter.author.id
        embed = self.embed_creator(inter, seed)
        await inter.response.send_message(content=f'{inter.author.mention}你今天的運勢是...',embed=embed)

    def embed_creator(self, inter, seed: int) -> Embed:
        """Creat and return a discord draw lots embed."""
        random.seed(seed)
        n = random.randint(0, 99)
        result = LOTS[n]

        now = datetime.utcnow().replace(tzinfo=pytz.timezone('UTC'))
        now_nst = now.astimezone(pytz.timezone('Asia/Taipei'))

        date = f"{now_nst.year} 年 {now_nst.month} 月 {now_nst.day} 日"
        desc = "**{}**\n".format(result["poem_line1"])
        desc+= "`{}`\n".format(result["poem_line1_explain"])
        desc+= "**{}**\n".format(result["poem_line2"])
        desc+= "`{}`\n".format(result["poem_line2_explain"])
        desc+= "**{}**\n".format(result["poem_line3"])
        desc+= "`{}`\n".format(result["poem_line3_explain"])
        desc+= "**{}**\n".format(result["poem_line4"])
        desc+= "`{}`\n".format(result["poem_line4_explain"])

        embed = Embed(title=f"{date}💮{result['title']}籤-{result['status']}",
         description=desc, color=inter.author.color, timestamp=datetime.now())
        
        payload = result['payload']
        for key in payload:
            embed.add_field(name=key, value=payload[key], inline=True)
        embed.set_footer(text=f"{inter.author.name}#{inter.author.discriminator}")
        return embed
   
def setup(bot):
    bot.add_cog(DrawLots(bot))
