from api import discord_key
import discord
from discord import app_commands
from discord.ext import commands
import os
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync() 
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')


list_id = 1289151239120097365
channel_id = 1288962369564708966


def generate_idnex():
    chair_idx = random.randint(0, 5)
    scribe_idx = random.randint(0, 5)

    if chair_idx == scribe_idx:
        raise ValueError
    
    return (chair_idx, scribe_idx)

@bot.tree.command(name="roles", description="Choose a chair and a scribe")
async def hello(interaction: discord.Interaction):

    channel = bot.get_channel(channel_id)

    if channel == None:
        print("Channel not found")

    list = await channel.fetch_message(list_id)
    members = list.content
    members = members.split(',')

    try:
        chair_idx, scribe_idx = generate_idnex()
    except ValueError:
        chair_idx, scribe_idx = generate_idnex()

    await interaction.response.send_message(f'Today chair is {members[chair_idx]} and scribe is {members[scribe_idx]}')

try:
    temp = os.getenv('heroku')
    if temp == 1:
        discord_key = os.getenv('discord_key')
except:
    pass


bot.run(discord_key)