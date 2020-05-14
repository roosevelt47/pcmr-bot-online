import discord
import os
import random
import asyncio

from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix = '?')


@client.event
async def on_ready():
    print('Skynet Online')
    channel = client.get_channel(710109338311852042)
    await channel.send('Skynet Online')


@client.command(aliases = ['f','F'])
async def resp(ctx, amount=1):
    await ctx.send('F\n'*amount)

@client.command(aliases = ['roasting'])
async def roast(ctx):
  roasts = ["You’re the reason God created the middle finger.",

"If your brain was dynamite, there wouldn’t be enough to blow your hat off.",

"You are more disappointing than an unsalted pretzel.",
"Light travels faster than sound which is why you seemed bright until you spoke.",

"We were happily married for one month, but unfortunately we’ve been married for 10 years.",

"Your kid is so annoying, he makes his Happy Meal cry.",

"You have so many gaps in your teeth it looks like your tongue is in jail.",

"Your secrets are always safe with me. I never even listen when you tell me them.",

"I’ll never forget the first time we met. But I’ll keep trying.",


"I forgot the world revolves around you. My apologies, how silly of me.",

"I only take you everywhere I go just so I don’t have to kiss you goodbye.",

"Hold still. I’m trying to imagine you with personality.",

"Our kid must have gotten his brain from you! I still have mine.",

"Your face makes onions cry.",

"You look so pretty. Not at all gross, today.",

"It’s impossible to underestimate you.",


"I’m not insulting you, I’m describing you.",

"I’m not a nerd, I’m just smarter than you.",

"Keep rolling your eyes, you might eventually find a brain.",

"You bring everyone so much joy, when you leave the room.",

"I thought of you today. It reminded me to take out the trash.",


"You are the human version of period cramps.",

"If you’re going to be two-faced, at least make one of them pretty.",

"You are like a cloud. When you disappear it’s a beautiful day.",

"I’d rather treat my baby’s diaper rash than have lunch with you.",

"Don’t worry, the first 40 years of childhood are always the hardest.",

"I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?",

"OH MY GOD! IT SPEAKS!",

"You are so full of shit, the toilet’s jealous.",

"Child, I have forgotten more than you ever knew",

"You just might be why the middle finger was invented in the first place."]

  await ctx.send(f'{random.choice(roasts)}')


@client.command(aliases = ['8b'])
async def _8b(ctx, * , question):
    responses = ['As I see it, yes.',
 'Ask again later.',
 'Better not tell you now.',
 'Cannot predict now.',
 'Concentrate and ask again.',
 'Don’t count on it.',
 'It is certain.',
 'It is decidedly so.',
 'Most likely.',
 'My reply is no.',
 'My sources say no.',
 'Outlook not so good.',
 'Outlook good.',
 'Reply hazy, try again.',
 'Signs point to yes.',
 'Very doubtful.',
 'Without a doubt.',
 'Yes.',
 'Yes – definitely.',
 'You may rely on it.']
    
    await ctx.send(f'Question: {question.capitalize()}\nAnswer: {random.choice(responses)}')

@client.command()
async def hi(ctx):
    uujwal = 'https://i.ibb.co/hcCwfT6/uujwal.jpg'
    await ctx.send(uujwal)
    responses1=('----------------------------------------\nI                HOPE   \n')
    await ctx.send(responses1)
    await asyncio.sleep(2)
    responses2='you all are \n'
    await ctx.send(responses2)
    await asyncio.sleep(1)
    responses3='doing  GUD\n----------------------------------------'
    await ctx.send(responses3)

@client.command()
async def bye(ctx):
    responses = ['BabBai','Gud bai istudants']
    await ctx.send(random.choice(responses))



@client.command()
async def ping(ctx):
    await ctx.send(f'The latency is {round(client.latency*1000)}ms')


keep_alive()

client.run('NzEwMTA1OTc5NDc1MzI5MDc0.Xry_Dw.NvaMwUgIQiBBPFxTEcSAqbwdifU')