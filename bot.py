import discord
import responses
from discord.ext import commands

description = '''TEST DESC'''

TOKEN = 'MTA5MzkzNjE1NzQ1ODQ0ODQ1NA.GzqCEB.j-eeT_YWe4Bhwo6bv2Th_x15sEdlp5VLDgxUog'
black_words = ["http://", "https://"]




async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)




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
                await message.channel.send(f"I just deleted {message.author.display_name}'s last message because it is not allowed")
                return

        print("Moderated message > Ok")

        if message.content.lower().startswith("bot"):
            await message.channel.send(f"Hi, {message.author.display_name}")
            await message.channel.send("What can I do for you? Digit !help")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
