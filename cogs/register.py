import discord
from discord.client import Client
from discord.ext import *
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from config import *
from hcfg import *



class Register(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.guild = None
        self.database = hcfgdb('./database/database.hcfg')


    @commands.Cog.listener()
    async def on_ready(self):
        print("Register module is ready.")
        self.guild = self.client.get_guild(serverGuildId)
        await self.client.change_presence(activity=discord.Game(name=f"{self.guild.name} ♥️ hyper"))
        

    

    async def assignRoles(self,member: discord.Member):
        for role in member.roles:
            try:
                await member.remove_roles(role)
            except:
                None
        
    async def addRole(self,member: discord.Member,roleId):
        role = self.guild.get_role(roleId)
        await member.add_roles(role)


    async def member_has_role(self,member,roleId):
        role = self.guild.get_role(roleId)
        if(role in member.roles):
            return True
        else:
            return False


    async def error(self,channel,msg):
        embed = discord.Embed()
        embed.title = "Hata ❎"
        embed.color = discord.Color.random()
        embed.description = f"**:face_with_monocle: {msg}.**"
        await channel.send(embed=embed,delete_after=5) 
        return

    async def success(self,channelId,msg,author):
        channel = self.guild.get_channel(channelId)
        embed = discord.Embed()
        embed.title = "Başarılı ✅"
        embed.set_author(name=f"{self.guild.name}",icon_url=self.guild.icon_url)
        embed.color = discord.Color.random()
        embed.description = f"**:face_with_monocle: {msg}**"
        embed.set_footer(text=f"{author} tarafından istendi.",icon_url=author.avatar_url)
        await channel.send(embed=embed) 
        return

    async def send_message(self,channelId: int, message):
        channel = self.guild.get_channel(channelId)
        await channel.send(message)
        return

    @commands.command()
    @commands.has_role(registerRoleId)
    async def e(self,ctx,member: discord.Member):
        if(member.top_role >= ctx.author.top_role):
            self.error(ctx.channel,"Kayıt etmek istediğin kişinin yetkisi senden büyük.")
            return

        await self.assignRoles(member)
        await self.addRole(member,maleRoleId)
        await self.success(registerLogChatId,f"{member.mention} Erkek rolüne atandı!",ctx.author)
        await self.send_message(generalChatId,f"{member.mention} **Aramıza katıldı, Hoş geldin!**")
        await ctx.message.add_reaction('✅')

    @commands.command()
    @commands.has_role(registerRoleId)
    async def k(self,ctx,member: discord.Member):
        if(member.top_role >= ctx.author.top_role):
            self.error(ctx.channel,"Kayıt etmek istediğin kişinin yetkisi senden büyük.")
            return
        await self.assignRoles(member)
        await self.addRole(member,femaleRoleId)
        await self.success(registerLogChatId,f"{member.mention} Kadın rolüne atandı!",ctx.author)
        await self.send_message(generalChatId,f"{member.mention} **Aramıza katıldı, Hoş geldin!**")
        await ctx.message.add_reaction('✅')

    
    @commands.command()
    @commands.has_role(registerRoleId)
    async def kayıtsız(self,ctx,member: discord.Member):
        if(member.top_role >= ctx.author.top_role):
            self.error(ctx.channel,"Kayıttan çıkarmak istediğin kişinin yetkisi senden büyük.")
            return
        await self.assignRoles(member)
        await self.addRole(member,unRegisteredRoleId)
        await self.success(registerLogChatId,f"{member.mention} Kayıtsız rolüne atandı!",ctx.author)
        


        


    


def setup(client):
    client.add_cog(Register(client))

