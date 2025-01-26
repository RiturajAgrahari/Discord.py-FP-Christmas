import discord
import random

from discord import ui, Interaction
from discord._types import ClientT
from discord.errors import HTTPException

from models import Card, Profile, CardCollection
from constant import OFFICIAL_IMAGE, ERROR_RESPONSES
from helper import send_error


"""
EVENT : EVENT FUNCTIONS 
"""


async def get_card(main_interaction: discord.Interaction, client: discord.Client, user: Profile):
    cards = await Card.all()
    if not cards:
        error = 'There is no cards in database, please check it as it is required to use the bot.!!'
        await send_error(__file__, get_card.__name__, error, client)
        response = random.choice(ERROR_RESPONSES)
        await main_interaction.response.send_message(content=f'{response}', ephemeral=True)

    else:
        random_card = random.choice(cards)
        embed = await card_embed(random_card)
        await main_interaction.response.send_message(embed=embed)
        print("adding a card")
        collection = CardCollection(user=user, card=random_card)
        await collection.save()
        print("card added")


async def get_card_collection(main_interaction: discord.Interaction, client: discord.Client, user: Profile):
    cards = await user.collection.all()

    embed = discord.Embed(
        title=f'{main_interaction.user.name} Cards',
        description=f'You have total {len(cards)} cards.',
        color=discord.Color.dark_gray()
    )
    embed.set_footer(text='FragPunk - Coming Mar 6, 2025 (PST)', icon_url=OFFICIAL_IMAGE)

    # embed.set_image(url=card.image)
    await main_interaction.response.send_message(embed=embed, ephemeral=True)


"""
UI : CARD UI COMPONENTS
"""


async def card_embed(card: Card):
    embed = discord.Embed(
        title=card.name,
        description=card.description,
        color=discord.Color.from_rgb(r=255, g=255, b=255),
    )
    embed.set_image(url=card.image)
    embed.set_footer(text='FragPunk - Coming Mar 6, 2025 (PST)', icon_url=OFFICIAL_IMAGE)
    return embed


"""
CONFIGURATION :  EVENT CONFIGURATION
"""


async def card_event_configuration(main_interaction: discord.Interaction, client: discord.Client, edit: bool = False):
    # Fetching all cards
    cards = await Card.all()
    description = ""
    for card in cards:
        description += f'**{card.id}.** {card.name}\n'

    # Creating Embed
    embed = discord.Embed(
        title="Card Event",
        description=description,
        color=discord.Color.gold()
    )

    # Button View
    class MyView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.delete = True

        # Button to add a card into db
        @discord.ui.button(label='Add card', style=discord.ButtonStyle.gray)
        async def add_card_to_db(self, interaction: discord.Interaction, button: discord.ui.Button):
            await add_card(interaction, client)

        # Button to update or delete a card from db
        @discord.ui.button(label=f"{'Update/Delete' if cards else 'No'} card", style=discord.ButtonStyle.gray, disabled=False if cards else True)
        async def update_card_to_db(self, interaction: discord.Interaction, button: discord.ui.Button):
            await choose_card(interaction, client, cards)

        @discord.ui.button(label=f'Import', style=discord.ButtonStyle.green, disabled=True)
        async def import_data(self, interaction: discord.Interaction, button: discord.ui.Button):
            pass

        @discord.ui.button(label=f'Export', style=discord.ButtonStyle.green)
        async def export_data(self, interaction: discord.Interaction, button: discord.ui.Button):
            pass

        async def interaction_check(self, interaction: Interaction, /) -> bool:
            if interaction.user.mention == main_interaction.user.mention:
                self.delete = False
                return True
            return False

        async def on_timeout(self) -> None:
            if self.delete:
                await main_interaction.delete_original_response()

    view = MyView()
    if edit:
        await main_interaction.edit_original_response(content=None, embed=embed, view=view)
    else:
        await main_interaction.response.edit_message(embed=embed, view=view)


async def add_card(main_interaction: discord.Interaction, client: discord.Client):
    class AddCard(discord.ui.Modal, title='Add a Card'):
        card_name = ui.TextInput(label='Name', style=discord.TextStyle.short, placeholder='Card Name', required=True)
        card_description = ui.TextInput(label='Description', style=discord.TextStyle.long, placeholder='Card Description', required=True)
        card_image_url = ui.TextInput(label='Image URL', style=discord.TextStyle.short, placeholder='Card Image URL', required=True)

        async def on_submit(self, interaction: discord.Interaction, /) -> None:
            # Creating instance of a Card
            card = Card(
                name=str(self.card_name),
                description=str(self.card_description),
                image=str(self.card_image_url),
            )

            # Creating embed
            embed = await card_embed(card)

            # Checking the url is in valid form
            try:
                # Sending preview response
                await interaction.response.send_message(
                    content=f"```diff\n+ >>> CARD SAVED, HERE IS ITS PREVIEW```",
                    embed=embed,
                    ephemeral=True
                )

                # Saving card instance
                await card.save()

                # Editing the event menu to add the newly added card in list
                await card_event_configuration(main_interaction, client, edit=True)

            # IF url is not in a valid form
            except HTTPException:
                await interaction.response.send_message(
                    content=f"```diff\n- >>> INVALID URL FORMAT, PLEASE FILL A VALID URL FORMAT```",
                    ephemeral=True
                )

    form = AddCard()
    await main_interaction.response.send_modal(form)


async def choose_card(main_interaction: discord.Interaction, client: discord.Client, cards: list[Card]):
    # Creating options for select menu.
    card_options = [discord.SelectOption(label=card.name, value=card.id) for card in cards]

    # Select View
    class CardSelectMenu(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.delete = True

        # Choose a card from select menu from the options.
        @discord.ui.select(placeholder='Choose a card to update', max_values=1, options=card_options, disabled=False, row=1)
        async def select_a_card(self, interaction: discord.Interaction, select: discord.ui.Select):
            self.delete = False
            # Fetching the selected card instance.
            card = await Card.get_or_none(id=int(select.values[0]))
            # Update card menu
            await update_card(interaction, client, card, cards)

        # On timeout, when not responded for a long time.
        async def on_timeout(self) -> None:
            if self.delete:
                await main_interaction.message.delete()

    # Sending response.
    select_menu = CardSelectMenu()
    await main_interaction.response.edit_message(view=select_menu)


async def update_card(main_interaction: discord.Interaction, client: discord.Client, card: Card, cards: list[Card], edit: bool = False):
    # Creating embed for the card
    embed = await card_embed(card)

    # Creating view for card with multiple buttons
    class CardView(discord.ui.View):
        def __init__(self):
            self.delete = True
            super().__init__(timeout=60)

        # Button to update card name
        @discord.ui.button(label='Update Name', style=discord.ButtonStyle.green)
        async def update_card_name_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            await update_card_form(interaction, client, field="name", card=card)

        # Button to update card description
        @discord.ui.button(label='Update Description', style=discord.ButtonStyle.green)
        async def update_card_description_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            await update_card_form(interaction, client, field="description", card=card)

        # Button to update card image url
        @discord.ui.button(label='Update Image URL', style=discord.ButtonStyle.green)
        async def update_card_image_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            await update_card_form(interaction, client, field="image", card=card)

        # Button to update card image url
        @discord.ui.button(label='Choose another card', style=discord.ButtonStyle.gray)
        async def choose_another_card_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            await choose_card(interaction, client, cards)

        # Button to delete the card form db
        @discord.ui.button(label='Delete Card', style=discord.ButtonStyle.red)
        async def delete_card_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            cards.remove(card)
            await card.delete()
            await interaction.response.send_message('```diff\n- >>> card deleted!```', ephemeral=True)
            await card_event_configuration(main_interaction, client, edit=True)

        async def interaction_check(self, interaction: Interaction, /) -> bool:
            if interaction.user.mention == main_interaction.user.mention:
                self.delete = False
                return True
            return False

        async def on_timeout(self) -> None:
            if self.delete:
                await main_interaction.message.delete()

    # Sending view
    card_view = CardView()
    if edit:
        await main_interaction.edit_original_response(content=None, embed=embed, view=card_view)
    else:
        await main_interaction.response.edit_message(embed=embed, view=card_view)


async def update_card_form(main_interaction: discord.Interaction, client: discord.Client, field: str, card: Card):
    class UpdateFieldForm(discord.ui.Modal, title=f'Update card {field}'):
        if field == "description":
            update_field = discord.ui.TextInput(label=field.title(), style=discord.TextStyle.long)
        else:
            update_field = discord.ui.TextInput(label=field.title(), style=discord.TextStyle.short)

        async def on_submit(self, interaction: Interaction[ClientT], /) -> None:
            if field == "name":
                card.name = str(self.update_field)
            elif field == "description":
                card.description = str(self.update_field)
            elif field == "image":
                card.image = str(self.update_field)
            else:
                print("UNKNOWN FIELD.")

            embed = await card_embed(card)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=1)
                await card.save()
                cards = await Card.all()
                await update_card(main_interaction, client, card, cards, edit=True)
            except HTTPException:
                await interaction.response.send_message(content=f'```diff\n- >>>Invalid url form```', ephemeral=True)

    form = UpdateFieldForm()
    await main_interaction.response.send_modal(form)

