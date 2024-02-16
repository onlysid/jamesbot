from typing import Final
import os
from dotenv import load_dotenv
import discord

# Load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
WELCOME_CHANNEL_ID: Final[int] = os.getenv('WELCOME_CHANNEL_ID')

# JamesBot setup
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.members = True
client: discord.Client = discord.Client(intents=intents)

# Message functionality
async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        return
            
    if(user_message == 'ruh'):
        try:
            await message.channel.send('... ruh')
    
        except Exception as e:
            print(e)
        
        
# Handling JamesBot initialisation
@client.event
async def on_ready() -> None:
    await client.change_presence(status=discord.Status.online, activity=discord.Game(': All of Joe Turone\'s songs on infinite repeat.'))
    print(f'{client.user} is now running!')
    
# Handling incoming messages
@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
# Handling members joining and sending their first message
@client.event
async def on_member_join(member: discord.member = None):
    await client.wait_until_ready()
    channel = client.get_channel(int(WELCOME_CHANNEL_ID))
    print(channel)
    name = member.display_name
    embed = discord.Embed(title=(f'{member} has joined the server! \nWelcome!'), description = 'please nativate to rules channel and read all relavent information\nWe hope you enjoy your stay here <3', colour= 0xFFF0A1,)  
    embed.set_image(url='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWE5bDh0NHZpeDVkcXI0YzF0ZmVybTJ3bDRqZGJvZnRxdnJ6dHF6cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OnnUZxcHsbBN6/giphy.gif')
    await channel.send(embed=embed)

def main() -> None:
    client.run(token=TOKEN)
    
if __name__ == '__main__':
    main()