"""
Discord Bot integration for Ocurl link shortener

Commands
  !ocurl [urlToShorten]

Settings
  TOKEN
"""
import discord
from discord.ext import commands
import re
import json
from urllib.parse import urlencode, urlparse
import aiohttp
import os

API_URL = 'https://ocurl.io/api/v1/url'

validateUrl = re.compile("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*")

bot = commands.Bot(command_prefix='!', description='I generate short URLs!')

@bot.event
async def on_ready():
  print('(BOT) Bot connected')

"""
  Request for short URL
"""
@bot.command(description='Kindly ask for a shortened URL')
async def ocurl(ctx):
  # Prevents the bot from echoing itself
  message = ctx.message
  
  if (bot.user == message.author):
    return

  matches = validateUrl.match(message.content[6:].strip())

  if not matches:
    await message.channel.send('Hmmm... That doesn\'t look like a valid link')
    return

  destinationUrl = matches.group()

  parsed = urlparse(destinationUrl)

  if (not parsed.scheme):
    parsed = parsed._replace(**{ "scheme": "http" })

  destinationUrl = parsed.geturl()

  apiReq = '{}?{}'.format(API_URL, urlencode({ 'q': destinationUrl }))

  # Attempt API call
  async with aiohttp.ClientSession() as session:
      async with session.get(apiReq) as r:
          if r.status == 200:
              jsonData = await r.json()
              
              if 'err' in jsonData:
                await message.channel.send('Hmmm... That doesn\'t look like a valid link. Do you have a protocol specified? (http/https)')
                return
              
              await message.channel.send('https://'+jsonData['data']['url']) # Prefix with protocol to allow Discord hyperlinking
          else:
            await message.channel.send('Sorry, the bot is offline at the moment :(')

"""
  Help
"""
@bot.event
async def on_message(message):
  if (bot.user == message.author):
    return  

  if (type(message.channel) is discord.DMChannel):
    await message.channel.send('Hmm... I\'m not sure how I can respond. But this is how you can get a short url...\n `!ocrul www.example.com`')
    
  # Continue processing chain
  await bot.process_commands(message)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
