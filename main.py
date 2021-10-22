import discord
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from keep_alive import keep_alive
import random
import io
import aiohttp

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$howdy'):
        await message.channel.send('Howdy!')

    if message.content.startswith('$Love'):
      card_num = random.randint(1, 22)
      url = "https://www.horoscope.com/images-US/tarot/card_150x285-GoldenRider-Horoscope-" + str(card_num) + ".jpg"
      async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))

    if message.content.startswith('$Mood'):
      card_num = random.randint(1, 22)
      url = "https://www.horoscope.com/images-US/tarot/card_150x285-GoldenRider-Horoscope-" + str(card_num) + ".jpg"
      async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))

    if message.content.startswith('$Career'):
      card_num = random.randint(1, 22)
      url = "https://www.horoscope.com/images-US/tarot/card_150x285-GoldenRider-Horoscope-" + str(card_num) + ".jpg"
      async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'cool_image.png'))

    if message.content.startswith('$Aries'):
      url = "https://www.horoscope.com/star-ratings/today/aries"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Taurus'):
      url = "https://www.horoscope.com/star-ratings/today/taurus"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Gemini'):
      url = "https://www.horoscope.com/star-ratings/today/gemini"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Cancer'):
      url = "https://www.horoscope.com/star-ratings/today/cancer"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Leo'):
      url = "https://www.horoscope.com/star-ratings/today/leo"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Virgo'):
      url = "https://www.horoscope.com/star-ratings/today/virgo"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Libra'):
      url = "https://www.horoscope.com/star-ratings/today/libra"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)
    
    if message.content.startswith('$Scorpio'):
      url = "https://www.horoscope.com/star-ratings/today/scorpio"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Sagittarius'):
      url = "https://www.horoscope.com/star-ratings/today/sagittarius"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Capricorn'):
      url = "https://www.horoscope.com/star-ratings/today/capricorn"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$Aquarius'):
      url = "https://www.horoscope.com/star-ratings/today/aquarius"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)
    
    if message.content.startswith('$Pisces'):
      url = "https://www.horoscope.com/star-ratings/today/pisces"
      try:
        page = urlopen(url)
      except:
        print("Error opening the URL")
      soup = BeautifulSoup(page, 'html.parser')
      content = soup.find('div', {"class": "module-skin"})
      article = ''
      count = 0
      for tag in content.find_all('i', {'class': 'icon-star-filled'} or 'i', {'class': 'icon-star-filled highlight'}):
        count = count + 1
        if len(tag.get('class')) == 2:
          article = article + ':star:'
        if count == 4:
          article = article + ' sex\n'
        if count == 9:
          article = article + ' hustle\n'
        if count == 14:
          article = article + ' vibe\n'
        if count == 19:
          article = article + ' success\n'
      await message.channel.send(article)

    if message.content.startswith('$help'):
      article = 'Get your daily star rating by sending $YourSign.\nExample: $Virgo'
      await message.channel.send(article)
      
keep_alive()
client.run(os.getenv('TOKEN'))     