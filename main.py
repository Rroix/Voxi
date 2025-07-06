import discord
import asyncio
import random
import os

TOKEN = os.getenv("MTM5MTQ3ODc0NDMxMjQ1MTE4NQ.GqBxhT.wuq4aP2dE17d8DMUyIjdyJcYo5Sd3xiuXTE3Y8")

# IDs configuradas
GUILD_ID = 1272287120983064599
CHANNEL_ID = 1391482432661749841
ROLE_ID = 1391480637323608237

# URLs de imágenes
IMAGES = [
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2F66%2Fe5%2Fd7%2F66e5d75c34e40de9a9593c9b4dac91ad.jpg&f=1&nofb=1&ipt=fd11f6c65c50fe11ab5ba5dd0f91340fa49876e5e9866495ac6910f966d86627",
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fccc4ca8f-6bd4-4e08-a8b0-e2abbbd42abd%2Fscale-to-width%2F755&f=1&nofb=1&ipt=7cc43e17fef6f815a2f6a7c9038997d46bd630328b2066f9ca12d2c8d855aae3"
]

# Intents necesarios
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

async def send_image_loop():
    await client.wait_until_ready()

    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("Couldn't find the server, bruh")
        return

    channel = guild.get_channel(CHANNEL_ID)
    role = guild.get_role(ROLE_ID)

    if not channel or not role:
        print("No channel or role selected, are you stupid??")
        return

    while not client.is_closed():
        image_url = random.choice(IMAGES)
        embed = discord.Embed()
        embed.set_image(url=image_url)

        try:
            await channel.send(content=f"{role.mention}", embed=embed)
            print("Image sent, enjoy!")
        except Exception as e:
            print(f"Couldn't send the image... {e}")

        await asyncio.sleep(600)  # 10 minutos

@client.event
async def on_ready():
    print(f"Bot connected to {client.user}, which is our client, Xd")
    client.loop.create_task(send_image_loop())

@client.event
async def on_message(message):
    if not message.guild or message.guild.id != GUILD_ID:
        return  # Ignorar DMs y otros servidores

client.run(TOKEN)