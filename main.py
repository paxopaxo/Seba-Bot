import discord 
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from serpapi import GoogleSearch

print ( os.environ['rer'] ) 




client = discord.Client()

rer_words = ['duro', 'dura' , 'buena' ,'rica', 'rico']

tragos = ['whiskey', 'pisco', 'vodka', 'chela', 'piscola', 'ron', 'vino',]

starter_encouragements =[
  'y tu hermana?',
  'y tu mama?',
  'y mi pichula?'
]


if 'res' not in db.keys():
  db['res'] = True


def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote) 

def update_encouragements(encouraging_message):
  if 'encouragements' in db.keys():
    encouragements = db['encouragements']
    encouragements.append(encouraging_message)
    db['encouragements'] = encouragements 
  else:
    db['encouragements'] = [encouraging_message]


def delete_encouragement(index):
  encouragements = db['encouragements']
  if len(encouragements) > index:
    del encouragements [index]
    db ['encouragements'] = encouragements


@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('rer'):
    await message.channel.send('sas')
  
  if message.content.startswith('sas'):
    await message.channel.send('rer')

  if message.content.startswith('cockiller'):
    await message.channel.send('cocos')
  
  if message.content.startswith('%inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db['res']:
    options = starter_encouragements
    if 'encouragements' in db.keys():
      options.extend(db["encouragements"])

    if any(word in msg for word in rer_words):
      await message.channel.send(random.choice(options))

  if msg.startswith('%new'):
    encouraging_message = msg.split('%new ',1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send('nuevo mesaje añadido')

  if msg.startswith('%del'):
    encouragements = []
    if 'encouragements' in db.keys():
      index = int(msg.split('%del ',1)[1])
      delete_encouragement(index)
      encouragemenets = db['encouragements']
    await message.channel.send(encouragements)

  if msg.startswith('%list'):
    encouragements = []
    if 'encouragements' in db.keys():
      encouragements = db['encouragements']
    await message.channel.send(encouragements)

  if msg.startswith('%res '):
    value = msg.split('%res ' ,1) [1]

    if value.lower() == 'true':
      db['res'] = True
      await message.channel.send('Responding is on.')
    else:
      db['res'] = False
      await message.channel.send('Responding is off.')

  if msg.startswith('%bar'):
    await message.channel.send(tragos)


keep_alive()

client.run(os.getenv('rersasrer'))


  

