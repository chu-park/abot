import discord
from discord.ext import commands
import os
import time
import sys
sys.path.append(r'C:\Users\sa485\OneDrive\Desktop\test\abot\item')
from item import a
from item1 import a1
from item import j

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="대기"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",'정보 봇',"봇 아이디:",'1022184013714182174',"봇 버전:",discord.__version__)

@client.command()
async def 정보(ctx, *, txt):    
    try:
        w1 = a[txt]["b"]
        w2 = a[txt]["c"]
        w3 = a[txt]["d"]
        w4 = a[txt]["e"]
        w5 = a[txt]["f"]
        w6 = a[txt]["g"]
        w7 = a[txt]["h"]
        w8 = a[txt]["i"]
        w9 = a[txt]["j"]
        w10 = a[txt]["k"]
        w11 = a[txt]["l"]
        w12 = a[txt]["m"]
        w13 = a[txt]["n"]
        w14 = a[txt]["o"]
        w15 = a[txt]["p"]
        w16 = a[txt]["q"]
        w17 = a[txt]["r"]
        w18 = a[txt]["s"]
        w19 = a[txt]["t"]

        embed=discord.Embed(title=w1, description=w2, color=discord.Color.random())
        embed.set_footer(text=w3 + j + w4 + j + w5 + j + w6 + j + w7 + j + w8 + j + w9 + j + w10 + j + w11 + j + w12 + j + w13 + j + w14 + j + w15 + j + w16 + j + w17 + j + w18)
        embed.set_image(url=w19)
        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('등록되지 않은 무기 입니다.')

@client.command()
async def 재료(ctx, *, txt1):    
    try:
        ww1 = a1[txt1]["b1"]
        ww2 = a1[txt1]["c1"]
        ww3 = a1[txt1]["d1"]
        ww4 = a1[txt1]["e1"]
        ww5 = a1[txt1]["f1"]
        ww6 = a1[txt1]["g1"]
        ww7 = a1[txt1]["h1"]

        embed=discord.Embed(title=ww1, description=ww2, color=discord.Color.random())
        embed.add_field(name=ww3, value=ww4, inline=False)
        embed.add_field(name=ww5, value=ww6, inline=False)
        embed.set_image(url=ww7)
        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('등록되지 않은 재료 입니다.')

client.run(os.environ['token'])