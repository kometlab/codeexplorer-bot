from tools import handle_response
from dotenv import dotenv_values
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import discord

cnf = dotenv_values(".env")

async def send_message(message: discord.Message=None, user_message: str=None, is_private: bool=False, *args) -> (None):
    try:
        response = handle_response(user_message, message, *args)
        if len(response) == 3:
            await message.author.send(embed=embed_message(response[0], response[1], response[2])) if is_private else await message.reply(mention_author=True, embed=embed_message(response[0], response[1], response[2]))
        else:
            await message.author.send(embed=embed_message(response[0], response[1])) if is_private else await message.reply(mention_author=True, embed=embed_message(response[0], response[1]))
    except Exception as error:
        print(error)

def embed_message(message: str="null", title: str="null", image: str=None) -> (discord.Embed|None):
    embed=discord.Embed(
            title=title,
            description=message,
            color=discord.Color.blue()
    )
    if not image == None:
        embed.set_image(url=image)
    return embed

def run_bot() -> None:
    intents = discord.Intents.all()
    client = Bot("!", intents=intents)

    @client.event
    async def on_ready() -> None:
        pass
    
    @client.event
    async def on_message(message: discord.Message=None, *args) -> None:
        if message.author == client.user: return
        username, user_message, channel = str(message.author), str(message.content), str(message.channel)
        try:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True, *args)
            elif user_message[0] == '!':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=False, *args)
        except Exception as error:
            print(error)
            
    client.run(cnf['TOKEN'])