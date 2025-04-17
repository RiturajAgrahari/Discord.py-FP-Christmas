import discord
from constant import CHARACTER


class WishlistHyperlinks(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        links = [
            'https://store.steampowered.com/app/2943650/FragPunk/',
            'https://store.epicgames.com/p/fragpunk-366318',
            'https://store.playstation.com/concept/10012871',
            'https://xbox.com/games/store/fragpunk/9mw715j1p29d'
        ]
        emojis = [
            '<:steam:1319265332757528636>',
            '<:epic_games:1319265251736162314>',
            '<:ps5:1319265317603512380>',
            '<:xbox:1319265344086347806>'

        ]
        main_button = discord.ui.Button(label="Wishlist Now!", style=discord.ButtonStyle.url, row=0,
                                        url="https://www.fragpunk.com/")
        self.add_item(main_button)
        for i in range(0, len(links)):
            button = discord.ui.Button(label="", style=discord.ButtonStyle.url, row=0, emoji=str(emojis[i]),
                                       url=str(links[i]))
            self.add_item(button)


async def christmas_response_embed(random_character):
    random_message = CHARACTER[random_character]["message"]

    embed = discord.Embed(
        title=f"🎄From {random_character}",
        description=random_message,
        color=CHARACTER[random_character]["color"],
    )
    embed.set_thumbnail(
        url=CHARACTER[random_character]["image"])
    embed.set_footer(
        text="FragPunk - Coming Mar 6, 2025 (PST)",
        icon_url="https://cdn.discordapp.com/attachments/1199253624350576692/1319344448739610654/Screenshot_2024-12-19"
                 "_at_10.13.25_PM.png?ex=67659ec4&is=67644d44&hm=b09a0ae850dbdf5ba4bc35b9a1de4130fefdab6a12d14da3b8911"
                 "fb6063abd4e&"
    )
    return embed


async def easter_response_embed(random_character):
    random_message = CHARACTER[random_character]["easter_response"]

    embed = discord.Embed(
        title=f"From {random_character}",
        description=random_message if random_message else '',
        color=CHARACTER[random_character]["color"],
    )

    embed.set_thumbnail(
        url=CHARACTER[random_character]["image"])
    embed.set_footer(
        text="FragPunk",
        icon_url="https://cdn.discordapp.com/attachments/1318864196137648128/1362388544529895707/1744889125967.jpg?ex=680236b4&is=6800e534&hm=64b8a0882a658fd13d9f447a9e43303fbd9b94e3edb5627b07ac225f1261e3a8&"
    )
    return embed
