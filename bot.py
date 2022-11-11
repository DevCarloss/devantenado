import discord
from discord.ext import tasks
from news import adrenaline
from news import olhardigital
from news import veja
import config

# dev antenado by devcarlos

Intents = discord.Intents.all()

client = discord.Client(intents=Intents)

# Discord Embeds


async def createEmbed(news):
    embed = discord.Embed(
        title=f"** {news.newsTitle} **",
        description="\n" + news.newsDescription,
        url=news.newsLink,
        color=discord.Color.from_rgb(204, 0, 0),
    )
    embed.set_image(url=news.newsImage)
    embed.add_field(name="Fonte", value=f"{news.URL}")
    return embed

@tasks.loop(hours=24)



async def embedsnews():
    channelId = client.get_channel(config.CHANNEL_ID)

    # Veja News

    vejaEmbed = await createEmbed(veja)
    await channelId.send(embed=vejaEmbed)

    # Adrenaline News

    adrenalineEmbed = await createEmbed(adrenaline)
    await channelId.send(embed=adrenalineEmbed)

    # Olhar Digital News

    olharDigitalEmebed = await createEmbed(olhardigital)
    await channelId.send(embed=olharDigitalEmebed)


# Client Event

@client.event

async def on_ready():
  embedsnews.start()


client.run(config.BOT_TOKEN)
