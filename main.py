import discord
from discord.ext import commands

description = "Este es un programa donde vinculamos a Discord con VS Code para lanzar imagenes"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logueado como {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    
    if message.content.lower()=="$meme":
        with open('18-611f9819d6e8f_6cdsxbbxfbz61-png__700-6124fe20cb297__700.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="Aqui está la imagen de un meme", file=picture)

bot.run("token")