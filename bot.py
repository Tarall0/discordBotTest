import discord
import responses
import random
from discord.ui import View, Button

description = '''TEST DESC'''

TOKEN = 'Token'
black_words = ["http://", "https://", "www."]
offensive_words = []

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is now running as BOT')

    @client.event
    async def on_message(message):
        # if message.author != client.user
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        for text in black_words:
            if "Key Role" not in str(message.author.roles) and text in str(message.content.lower()):
                print(f"Moderated message > Deleted - Member: {message.author}")
                await message.delete()
                await message.author.send(f"Hey {message.author.display_name}! 👋")
                await message.author.send(
                    f"Ho rimosso il tuo ultimo messaggio, perchè contiene del testo non ammesso. 😔")
                await message.channel.send(
                    f"Ho appena rimosso il messaggio di {message.author.display_name} perchè pare contenga contenuto "
                    f"non ammesso")
                return

            print("Moderated message > Ok")

        if "Limited Access" not in str(message.author.roles):
            if user_message == '!tod':
                view = View()
                button = Button(label="Verità", style=discord.ButtonStyle.grey, emoji="🔥")
                button2 = Button(label="Obbligo", style=discord.ButtonStyle.grey, emoji="💀")
                view.add_item(button)
                view.add_item(button2)

                embed = discord.Embed(title="Obbligo o verità?",
                                      description='Genera un obbligo o una verità, casuale!')
                await message.channel.send(embed=embed, view=view)

        if user_message == "!roll":
            roll = str(random.randint(1, 6))
            embed = discord.Embed(title=":game_die: Dice roll",
                                  description=f"{username} just rolled a dice \r \r Result: **{roll}**")
            await message.channel.send(embed=embed)

        if user_message == "!roll 20":
            roll = str(random.randint(1, 20))
            embed = discord.Embed(title=":game_die: Dice roll - D20",
                                  description=f"{username} just rolled a dice \r \r Result: **{roll}**")
            await message.channel.send(embed=embed)

        if user_message == "!help":
            view = View()
            button_link = Button(label="stonedzone.it", url="https://stonedzone.it", style=discord.ButtonStyle.url)
            view.add_item(button_link)
            embed = discord.Embed(title=":heart: MushApp",
                                  description=f"This python bot-application is just here for testing and learning "
                                              f"purposes \r \r **Commands available** \r \r **!roll** - Roll a dice ("
                                              f"d6) \r **!roll 20** - Roll a dice  (d20) \r **!tod** - Generate a "
                                              f"truth or a dare \r **!quote** - Get a random quote from an array\r \r "
                                              f"\r `Currently under developement an auto-moderating system for "
                                              f"texting channel, try typing 'https://'`")
            await message.channel.send(embed=embed, view=view)

        if message.content.lower().startswith("bot"):
            await message.channel.send(f"Ciao, {message.author.mention}")
            await message.channel.send("What can I do for you? Digit !help")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)



