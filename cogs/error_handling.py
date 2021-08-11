from discord.ext import commands
import discord



class ErrorHandling(commands.Cog):


    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            embed = discord.Embed()
            embed.title = "Hata ❎"
            embed.color = discord.Color.random()
            embed.description = "**:face_with_monocle: Bunu yapabilecek yetkin yok.**"
            await ctx.channel.send(embed=embed,delete_after=5) 
        if isinstance(error,commands.BotMissingPermissions):
            embed = discord.Embed()
            embed.title = "Hata ❎"
            embed.color = discord.Color.random()
            embed.description = "**:face_with_monocle: Benim bunu yapabilecek yetkim yok :(**"
            await ctx.channel.send(embed=embed,delete_after=5)
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed()
            embed.title = "Hata ❎"
            embed.color = discord.Color.random()
            embed.description = "**:face_with_monocle: Argümanın eksik veya yanlış.Argümanına dikkat et!**"
            await ctx.channel.send(embed=embed,delete_after=5)
        if isinstance(error,commands.MissingRole):
            embed = discord.Embed()
            embed.title = "Hata ❎"
            embed.color = discord.Color.random()
            embed.description = "**:face_with_monocle: Bunu yapabilecek yetkin yok.**"
            await ctx.channel.send(embed=embed,delete_after=5)
        if isinstance(error,commands.CommandOnCooldown):
            time = int(error.retry_after) 
            embed = discord.Embed()
            embed.title = "Hata ❎"
            embed.color = discord.Color.random()
            embed.description = f"**:face_with_monocle: Hızlı çocuk seni! {time} saniye sonra dene.**"
            await ctx.channel.send(embed=embed,delete_after=5)


def setup(client):
    client.add_cog(ErrorHandling(client))

    