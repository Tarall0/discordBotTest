import discord
import responses
import random
from discord.ext.commands import Bot, bot
from discord.ui import View, Button
import asyncio

TOKEN = 'Token'
black_words = ["http://", "https://", "www."]
offensive_words = []

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = Bot(command_prefix="!", intents=intents.all())



def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is now running as BOT')

    @client.event
    async def on_member_join(self, member, message):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await message.channel.send(to_send)

    @client.event
    async def on_message(message):
        # if message.author != client.user
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        for text in white_words:
            pass
            print("Checked")
        else:
            for text in black_words:
                if "Key Role" not in str(message.author.roles) and text in str(message.content.lower()):
                    print(f"Moderated message > Deleted - Member: {message.author}")
                    await message.delete()
                    await message.author.send(f"Hey {message.author.display_name}! 👋")
                    await message.author.send(
                        f"I just removed your last message because it is not allowed to entry that tipe of text 😔")
                    await message.channel.send(
                        f"I just deleted {message.author.display_name}'s last message because it is not allowed")
                    return

            print("Moderated message > Ok")

        if "Verified ✅" not in str(message.author.roles):
            if user_message == '!verify':
                view = View()
                button = Button(label="Verify", style=discord.ButtonStyle.green, emoji="✅")
                button2 = Button(label="Exit", style=discord.ButtonStyle.danger, emoji="💀")
                view.add_item(button)
                view.add_item(button2)

                embed = discord.Embed(title="Verify your account",
                                      description='Click Verify in order to get access to all channels')
                await message.channel.send(embed=embed, view=view)

        if user_message == "!roll":
            roll = str(random.randint(1, 6))
            embed = discord.Embed(title=":game_die: Dice roll",
                                  description=f"{username} ha appena lanciato un dado \r \r Risultato: **{roll}**")
            await message.channel.send(embed=embed)

        if user_message == "!roll 20":
            roll = str(random.randint(1, 20))
            embed = discord.Embed(title=":game_die: Dice roll - D20",
                                  description=f"{username} ha appena lanciato un dado \r \r Risultato: **{roll}**")
            await message.channel.send(embed=embed)

        if user_message == "!help":
            await asyncio.sleep(1)
            embed = discord.Embed(title=":heart: MushApp",
                                  description=f"This python bot-application is just here for testing and learning purposes \r \r **Commands available** \r \r **!roll** - Roll a dice (d6) \r **!roll 20** - Roll a dice  (d20) \r **!tod** - Return a Truth or a Dare \r **!quote** - Get a random quote from an array of strings \r \r \r `Currently under developement an auto-moderating system for texting channel, try typing 'https://'`")
            await message.channel.send(embed=embed)

        if user_message == "420" or user_message == "!420":

            gif_list = ["https://media.tenor.com/dl""-5x95WKh8AAAAC/420.gif",
                        "https://media.tenor.com/Qm1qCnh4_TEAAAAS/420-the-simpsons.gif",
                        "https://media.tenor.com/wZTOpYp88VwAAAAS/ah-smoke.gif",
                        "https://media.tenor.com/dl""-5x95WKh8AAAAC/420.gif",
                        "https://media.tenor.com/A6MkSkO-WiEAAAAS/weed-time-weed.gif",
                        "https://media.tenor.com/yGEuK0ItsWsAAAAS/weed-blunt.gif"
                        ]
            random_var = random.randint(0, 5)
            random_gif = gif_list[random_var]

            respons_ft = [f"Felice 420, {message.author.mention}!",
                          f"Hell yeah! {message.author.mention} #420",
                          f"Oggi 04/20 2023, accendila {message.author.mention}"]

            i = random.randint(0, 2)
            random_resp = respons_ft[i]
            await message.channel.send(random_resp)
            await message.channel.send(random_gif)

        if "bot" in str(message.content.lower()):
            bot_impulse = [
                f"Hey {message.author.mention}!",
                f"Si sono proprio io",
                f"Dici a me {message.author}?",
                f"Hai visto gli ultimi aggiornamenti su StonedZone?"
            ]
            z = random.randint(0, 3)
            returned = bot_impulse[z]
            await message.channel.send(returned)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

