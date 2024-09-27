from api import discord_key
import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()  # Sync the slash commands globally
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.tree.command(name="roles", description="Choose a chair and a scribe")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'hello, {interaction.user.mention}!')


try:
    temp = os.getenv('heroku')
    if temp == 1:
        discord_key = os.getenv('discord_key')
except:
    pass


bot.run(discord_key)