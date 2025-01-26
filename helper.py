import discord
from constant import ME


async def send_error(file, function_name, error, client, server='FragPunk'):
    embed = discord.Embed(title=f'{server} Server', description=file, color=discord.Color.red())
    embed.add_field(name=function_name, value=error, inline=False)
    user = await client.fetch_user(ME)
    await user.send(embed=embed)

