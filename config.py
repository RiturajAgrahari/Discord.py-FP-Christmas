import discord
from discord.ui import View

from models import Profile, Event
from cardEvent import card_event_configuration


async def x_config_bot(message: discord.Message, client: discord.Client):
    # Creating Embed
    embed = discord.Embed(
        title="BOT CONFIGURATION",
        description="configure all the bot functionality here.",
        color=discord.Color.red()
    )

    # Button View
    class MyView(View):
        def __init__(self):
            super().__init__(timeout=60)
            self.delete = True
            self.viewing_user = None

        @discord.ui.button(label='Configure', style=discord.ButtonStyle.gray)
        async def configure(self, interaction: discord.Interaction, button: discord.ui.Button):
            self.delete = False
            await response.delete()
            await x_config_menu(interaction, client)

        async def interaction_check(self, interaction: discord.Interaction):
            # Check if the interaction is from the original user
            if interaction.user.mention == self.viewing_user:
                return True
            else:
                await interaction.response.send_message("`>>> Access Denied!`", ephemeral=True)

        async def on_timeout(self) -> None:
            if self.delete:
                await response.delete()

    view = MyView()
    view.viewing_user = message.author.mention
    response = await message.reply(embed=embed, view=view)


async def x_config_menu(main_interaction: discord.Interaction, client: discord.Client):
    is_christmas_event = await Event.get_or_none(name="christmas_event")
    print(is_christmas_event.archived)
    is_card_event = await Event.get_or_none(name="card_event")

    # Creating Embed
    embed = discord.Embed(
        title="BOT CONFIGURATION MENU",
        description="- configure christmas event\n- configure card event",
        color=discord.Color.gold()
    )

    # Button View
    class MyView(View):
        def __init__(self):
            super().__init__(timeout=60)
            self.delete = True

        @discord.ui.button(label='Christmas Event', style=discord.ButtonStyle.gray, disabled=is_christmas_event.archived if is_christmas_event else True)
        async def config_christmas_event(self, interaction: discord.Interaction, button: discord.ui.Button):
            pass

        @discord.ui.button(label=f'Card Event', style=discord.ButtonStyle.green, disabled=is_card_event.archived if is_card_event else True)
        async def config_card_event(self, interaction: discord.Interaction, button: discord.ui.Button):
            self.delete = False
            await card_event_configuration(interaction, client)

        async def on_timeout(self) -> None:
            if self.delete:
                await main_interaction.delete_original_response()

    view = MyView()
    await main_interaction.response.send_message(embed=embed, view=view, ephemeral=True)


async def get_data():
    profiles = await Profile.all()
    with open("data.txt", "a") as f:
        f.truncate(0)
        f.write(f"{'id'.center(6)} | {'discord_id'.center(30)} | {'discord_name'.center(50)} \n")
        f.write(f"-------+--------------------------------+----------------------------------------------------"
                f"----------\n")
        for i in range(0, len(profiles)):
            f.write(f"{str(profiles[i].id).center(6)} | {str(profiles[i].discord_id).center(30)} |"
                    f" {str(profiles[i].discord_name).center(50)}\n")

