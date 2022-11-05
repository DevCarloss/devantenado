from news import veja
import discord
from discord.ext import tasks
from news import adrenaline
from news import olhardigital

# dev antenado by devcarlos

Intents = discord.Intents.all()

client = discord.Client(intents=Intents)

# Discord Embeds

@tasks.loop(hours=24)

async def embedsnews():
  channelId = client.get_channel()
  
  # Veja News
  
  embed = discord.Embed(
    title = "**Notícias!**",
    description = "\n" + "Fonte: " + '\n' + veja.vejaUrl + "\n\n" + veja.vejanewsName,
    color = discord.Color.from_rgb(255,153,0)
  )
  
  embed.set_image(url=veja.vejanewsImg)
  
  await channelId.send(embed=embed)
  
  # Adrenaline News 
  
  embed = discord.Embed(
         title = "**Notícias!**",
         description = "\n" + "Fonte: " + '\n' + adrenaline.adrenalineUrl + "\n\n" + adrenaline.adrenalinenewsName + "\n\n" + adrenaline.adrenalinenewsExcerpt ,
    color = discord.Color.from_rgb(204,0,0))
  
  embed.set_image(url=adrenaline.adrenalinenewsImg)
  
  await channelId.send(embed=embed)
  
  # Olhar Digital News
  
  embed = discord.Embed(
         title = "**Notícias!**",
         description = "\n" + "Fonte: " + '\n' + olhardigital.olhardigitalUrl + "\n\n" + olhardigital.olhardigitalnewsName + "\n\n" + olhardigital.olhardigitalnewsExcerpt,
    color = discord.Color.from_rgb(255,255,255))
  
  embed.set_image(url=olhardigital.olhardigitalnewsImg)
  
  await channelId.send(embed=embed)
 

# Client Event

@client.event

async def on_ready():
  embedsnews.start()

client.run("")
