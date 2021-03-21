import discord
from discord.ext import commands
from discord.utils import get
import random
import asyncio
from discord.ext.commands import Bot
import datetime
from datetime import timedelta
from datetime import date
import json
from pathlib import Path
import time
import math
import os
class new_member():
    def __init__(self):
        self.intra_db = 'Unchanged'
        self.days = '35'
        self.cursus = 'Pool'
        self.intre = '0'
        self.pool_stud = 0
        self.student = 0
        self.member = discord.Member
        self.user2 = discord.User
        self.idmember = 420
        self.intra_name = 'error 31 new_user.py'
        self.channel = 808327973056938007
        self.intraembed = discord.Embed
        self.intrasend = 'error 103 new_user.py'
        self.msg = 'error 96 new_user.py'
        self.nema = 69
        self.embed = discord.Embed
        self.insert = "INSERT INTO base_info (discord_id, intra, cursus, days) VALUES (%s, %s, %s, %s)"
        self.userdata = 'data'
class New_user(commands.Cog):
    #Initialisation of class
    def __init__(self, client):
        self.client = client
        self.base = self.client.base
    #This is a event command
    @commands.Cog.listener()
    async def on_ready(self):
        print("Member Join is loaded")

    @commands.command()
    async def newcommer(self, ctx):
        await ctx.send("Le bot vous a envoyé un message privé !")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        newuser = new_member()
        newuser.user2 = member
        newuser.idmember = newuser.user2.id #idmember = member.id
        #user_data = {"_id": discord id, "cursus": Pool, "blackwhole_absorption": 133}
        newuser.embed = discord.Embed(colour=discord.Colour.dark_gold(), description=f"Bienvenu.e sur le Discord 42 Nice, Ecrivez !intra LOGIN (LOGIN de l'intra) dans le channel newcommers pour avoir votre role sur le discord.")
        newuser.embed.set_thumbnail(url=f'{newuser.user2.guild.icon_url}')
        newuser.embed.set_author(name=f'{str(newuser.user2)}', icon_url=f'{newuser.user2.avatar_url}')
        newuser.embed.add_field(name="Account Created", value=newuser.user2.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        newuser.embed.set_footer(text=f'{newuser.user2.guild}', icon_url=f'{newuser.user2.guild.icon_url}')
        newuser.embed.timestamp = datetime.datetime.utcnow()
        newuser.channel = self.client.get_channel(id=808327973056938007)
        await newuser.channel.send(embed=newuser.embed)
        #######################################################
        await newuser.user2.send("Ecrivez !intra LOGIN (LOGIN de l'intra) dans le channel newcommers pour avoir votre role sur le discord.")
        return

def setup(client):
    client.add_cog(New_user(client))