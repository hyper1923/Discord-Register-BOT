import discord
from discord import Intents
from discord.ext import commands
from hcfg import *
import os
from config import *


##INTENTS
intents = discord.Intents.default()
intents.members = True

##CLIENT
client = commands.Bot(command_prefix='.',intents=intents)
client.remove_command('help')
client.load_extension('cogs.ready')
client.load_extension('cogs.register')
client.load_extension('cogs.error_handling')





client.run(token)