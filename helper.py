import discord
from constant import ME
from models import Profile


async def send_error(file, function_name, error, client, server='FragPunk'):
    embed = discord.Embed(title=f'{server} Server', description=file, color=discord.Color.red())
    embed.add_field(name=function_name, value=error, inline=False)
    user = await client.fetch_user(ME)
    await user.send(embed=embed)


async def check_profile(discord_id, discord_name):
    # Checking for user's profile
    user = await Profile.get_or_none(discord_id=str(discord_id))
    if not user:
        # Creating user profile
        user = Profile(discord_id=str(discord_id), discord_name=str(discord_name))
        await user.save()

    return user

