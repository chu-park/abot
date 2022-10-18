import discord
from discord.ext import commands
import os
import time
import sys
sys.path.append(r'C:\Users\sa485\OneDrive\Desktop\test\abot\item')
from item import a
from item1 import a1
from item2 import a2
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

        embed=discord.Embed(title=ww1, description=ww2, color=discord.Color.random())
        embed.add_field(name="드랍 장소(구매 장소)", value=ww3, inline=False)
        embed.add_field(name="중요도", value=ww4, inline=False)
        embed.set_image(url=ww5)
        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('등록되지 않은 재료 입니다.')

@client.command()
async def 인챈(ctx, *, txt2):    
    try:
        w2_1 = a2[txt2]["b2"]
        w2_2 = a2[txt2]["c2"]
        w2_3 = a2[txt2]["d2"]
        w2_4 = a2[txt2]["e2"]
        w2_5 = a2[txt2]["f2"]
        w2_6 = a2[txt2]["g2"]
        w2_7 = a2[txt2]["h2"]
        w2_8 = a2[txt2]["i2"]
        w2_9 = a2[txt2]["j2"]
        w2_10 = a2[txt2]["k2"]
        w2_11 = a2[txt2]["l2"]
        w2_12 = a2[txt2]["m2"]
        w2_13 = a2[txt2]["n2"]
        w2_14 = a2[txt2]["o2"]
        w2_15 = a2[txt2]["p2"]

        embed=discord.Embed(title=w2_1, description=w2_2, color=discord.Color.random())
        embed.add_field(name="입수 정보", value=w2_3, inline=False)
        embed.add_field(name="부위", value=w2_4, inline=False)
        embed.add_field(name="중요도", value=w2_5, inline=False)
        embed.add_field(name="효과", value="", inline=False)
        embed.set_footer(text=w2_6 + j + w2_7 + j + w2_8 + j + w2_9 + j + w2_10 + j + w2_11 + j + w2_12 + j + w2_13 + j + w2_14 + j + w2_15)
        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('등록되지 않은 재료 입니다.')

client.run(os.environ['token'])