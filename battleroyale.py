# Import modules
import discord

# Output discord.py version used
print("Using discord.py version {}".format(discord.__version__))

# Create discord.py instance
bot = discord.Client()

# Output when bot is initialised
@bot.event
async def on_ready():
    print("Bot started successfully")

# Run bot using token given
bot.run(#Bot token goes here in quotes)