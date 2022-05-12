from random import choice

import os

from disnake.ext import commands, tasks
from disnake.utils import get

class TemporaryVoice(commands.Cog):
    Atlantis_ID = int(os.environ.get("Atlantis_ID"))
    """Temporary Voice Channel -> tvc"""
    def __init__(self, bot):
        self.bot = bot
        self.taskloop.start()

    @commands.Cog.listener('on_voice_state_update')
    async def _create_tvc(self, member, before, after):
        if after.channel is not None and after.channel.id == 973743539089457223:
            channel = get(member.guild.voice_channels, name=f'{member.name} 的頻道')
            if channel is None:
                category = get(member.guild.categories, id=973743537994752000)
                new_channel = await member.guild.create_voice_channel(name=f'{member.name} 的頻道', category=category, bitrate=64000, user_limit=0)
                await member.move_to(new_channel)
            else:
                await member.move_to(channel)
        elif before.channel.category_id == 973743537994752000 and before.channel.id != 973743539089457223 and before.channel.members is None:
            await before.channel.delete()

    async def tvc_helper(self) -> None:
        """
            Delete empty tvc.
            Transfer tvc owner.
        """
        guild = self.bot.get_guild(self.Atlantis_ID)
        for channel in self.bot.get_guild(self.Atlantis_ID).voice_channels:
            if channel.category_id == 973743537994752000 and channel.id != 973743539089457223:
                print(channel.members)
                if channel.members is None:
                    await channel.delete()
                else:
                    members_list = []
                    owner = get(guild.members, name=channel.name[:-4])
                    for member in channel.members:
                        if not member.bot:
                            members_list.append(member.id)
                    if not owner or owner.id not in members_list:
                        new_owner = get(guild.members, id=choice(members_list))
                        await channel.edit(name=f'{new_owner.name} 的頻道')
    
    async def creat_vc_cleaner(self) -> None:
        guild = self.bot.get_guild(self.Atlantis_ID)
        channel = get(guild.voice_channels, id=973743539089457223)
        for member in channel.members:
            channel = get(member.guild.voice_channels, name=f'{member.name} 的頻道')
            if channel is None:
                category = get(member.guild.categories, id=973743537994752000)
                new_channel = await member.guild.create_voice_channel(name=f'{member.name} 的頻道', category=category, bitrate=64000, user_limit=0)
                await member.move_to(new_channel)
            else:
                await member.move_to(channel)

    @tasks.loop(seconds=5.0)
    async def taskloop(self) -> None:
        try:
            await self.tvc_helper()
            await self.creat_vc_cleaner()
        except Exception as err:
            print(err)

    @taskloop.before_loop
    async def before_taskloop(self) -> None:
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(TemporaryVoice(bot))
