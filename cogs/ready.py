from operator import imod
from os import times
import discord
from discord import mentions
from discord.abc import User
from discord.client import Client
from discord.ext import *
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from time import *
from config import *

class Ready(commands.Cog):

    def __init__(self,client):
        self.client : Client = client
        self.guild = None
        self.channel = None
        self.trustedTime = 1577880000

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.client.user.name} has ready.")
        self.guild = self.client.get_guild(serverGuildId)
        self.channel = self.client.get_channel(registerChannelId)


    async def TryTrusted(self,timeStamp):
        if(timeStamp >= self.trustedTime):
            return ">>>   **❎ Güvenilir değil**"
        else:
            return ">>>   **✅ Güvenilir**"


    @commands.Cog.listener()
    async def on_member_join(self,member): 
        timestamp = member.created_at.timestamp()
        time = member.created_at.strftime(r'%d/%m/%y')

        text = await self.TryTrusted(timestamp)
        embed = discord.Embed()
        embed.set_author(icon_url=self.guild.icon_url,name=f"Bir ışık belirdi, 👋 {member.name}")
        embed.description = f"""
        **🥳 Sunucumuza hoş geldin** {member.mention}!\n
        **🎉 Seninle beraber {len(self.guild.members)} kişiyiz!**\n
        **✅ Kayıt olmak için yetkilileri beklemen yeterlidir.**\n

        {text}
        **📡 Hesabın oluşturulma tarihi: {time}**
        """ 
        embed.set_thumbnail(url=member.avatar_url)
        embed.color = discord.Colour.random()
        embed.set_footer(icon_url=self.guild.icon_url,text=f"{self.guild.name} Kayıt Sistemi")
        await self.channel.send(f"> {member.mention}", embed=embed)



        

def setup(client):
    client.add_cog(Ready(client))