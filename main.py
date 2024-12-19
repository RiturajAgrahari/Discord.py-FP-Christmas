import os
import sys
import random

import discord
from discord import app_commands
from discord.errors import Forbidden
from dotenv import load_dotenv

from ui import WishlistHyperlinks, christmas_response_embed
from models import Profile, ChristmasResponseEvent
from db import db_init

from constant import CHARACTER


# LOADING ENV
load_dotenv()


# INITIALIZING
MY_GUILD = int(os.getenv("MY_GUILD"))
TEST_GUILD = int(os.getenv("TEST_GUILD"))
MAIN_GUILD = int(os.getenv("MAIN_GUILD"))
guilds = [MY_GUILD, TEST_GUILD, MAIN_GUILD]

permitted_users = ['<@568179896459722753>']

responses = [
    "_magic 🪄... try the command again </hero:1302652188148891690>_",
    "_ghost came into the way 👻... try the command again </hero:1302652188148891690>_",
    "_ uf! high traffic  🚦... try the command again </hero:1302652188148891690>_",
    "_ is this your parcel?  📦... try the command again </hero:1302652188148891690>_"
]


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """
        Initializing guilds and connecting it to the bot.
        :return:
        """
        for guild in guilds:
            main_guild = discord.Object(id=guild)
            try:
                self.tree.copy_global_to(guild=main_guild)
                await self.tree.sync(guild=main_guild)
            except Forbidden:
                print("Forbidden ERROR")
                # info_logger.error(f"GUILD ID : [{guild}] Bot has Missing Access")


# Running the client with specific permissions
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Your LancerGreeter bot in successfully started as {client.user} (ID: {client.user.id})')
    print('-----')
    await db_init()


@client.event
async def on_message(message):
    # Check if the message author is not client itself
    if message.author == client.user:
        pass

    # Checks if the message is recieved in DM
    elif message.channel.type == discord.ChannelType.private:
        print(f'DM --> [{message.author}] : {message.content}')

    # Message in server channels
    else:
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        guild_name = message.guild.name
        # print(f'[channel: {channel}] --> {username}: {user_message}')

        if message.author.mention in permitted_users:
            if user_message == "tommy!":
                await message.reply(content="wuff wuff!")

            elif user_message == "$config":
                # await config_bot(message, luck, client)
                pass

        if "merry christmas" in str(user_message).lower():
            try:
                user = await Profile.get_or_none(discord_id=str(message.author.mention))
                if not user:
                    u = Profile(
                        discord_id=str(message.author.mention),
                        discord_name=str(message.author.name)
                    )
                    await u.save()
                    user = u

                random_character = random.choice(list(CHARACTER.keys()))
                embed = await christmas_response_embed(random_character)
                view = WishlistHyperlinks()
                event_data = ChristmasResponseEvent(
                    user_id=user,
                    hero_name=random_character,
                )
                await event_data.save()
                await message.reply(embed=embed, view=view)

            except Exception as e:
                print(e)
                response = random.choice(responses)
                await message.reply(response)


async def send_error(file, function_name, error, server='FragPunk'):
    embed = discord.Embed(title=f'{server} Server', description=file, color=discord.Color.red())
    embed.add_field(name=function_name, value=error, inline=False)
    user = await client.fetch_user(568179896459722753)
    await user.send(embed=embed)


@client.event
async def on_error(event, *args, **kwargs):
    error = str(sys.exc_info())
    error = error.replace(',', '\n')
    # error_logger.error(error)
    await send_error(__file__, event, error)


client.run(token=os.getenv("TOKEN"))





