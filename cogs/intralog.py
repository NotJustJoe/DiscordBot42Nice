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

class new_memb():
    def __init__(self):
        self.intra_db = 'Unchanged'
        self.days = '35'
        self.cursus = 'Pool'
        self.intre = '0'
        self.pool_stud = 0
        self.student = 0
        self.member = discord.Member
        self.user2 = discord.Member
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
class intralog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.base = self.client.base
    @commands.Cog.listener()
    async def on_ready(self):
        print("Intralog is loaded")

    @commands.command()
    async def intra(self, ctx, intranick):
        mem = ctx.message.author.id
        member = ctx.message.guild.get_member(mem)
        newuser = new_memb()
        newuser.user2 = member
        newuser.intra_db = intranick
        newuser.idmember = newuser.user2.id #idmember = member.id
        #user_data = {"_id": discord id, "cursus": Pool, "blackwhole_absorption": 133}
        async def add_role(self, member, ROLE):
            role = get(member.guild.roles, name=ROLE)
            await newuser.user2.add_roles(role)

        async def chnick(member: discord.Member, intranick):
            await newuser.user2.edit(nick=intranick)

        await asyncio.sleep(0.05)
        await chnick(newuser.user2, newuser.intra_db)
        if 0 == 0: #Condition is 1 == 1 because i dont have access to the intra API yet, every user joining the discord at the moment are confirmed students
            newuser.cursus = 'Student' #WE WILL CHECK INSIDE INTRA TO SEE IF HE IS STUDENT
            newuser.days = '160' #WE WILL CHECK INSIDE INTRA TO SEE NUMBERS OF DAYS LEFT  
            user_data = {"_id": newuser.idmember, "intra": newuser.intra_db, "cur": newuser.cursus, "bh": newuser.days}
            await asyncio.sleep(0.05)
            if not self.base.find_one({"_id":newuser.idmember}):#if not in database, insert
                self.base.insert_one(user_data) #insert database
            elif self.base.find_one({"_id":newuser.idmember}): #if already in database
                newuser.nema = self.base.find({"_id":newuser.idmember})
                await newuser.user2.send(f"Erreur innatendue, demandez de l'aide à un Bot Helper.")
                return
            await asyncio.sleep(0.05)

            await add_role(self, newuser.user2, 'Student')
            channel_stud = self.client.get_channel(id=767431141095374860)
            await channel_stud.send(f'Bienvenu à {newuser.user2.nick} !')
            await newuser.user2.send(f"Bienvenu(e) sur le Discord de 42 Nice !")
            await asyncio.sleep(0.05)
            return
        elif 0 == 1: #Condition is 0 == 1 because i dont have access to the intra API yet, so i can't check if the user IS pool or not
            newuser.cursus = 'Pool'
            newuser.days = '113' #WE WILL CHECK INSIDE INTRA TO SEE NUMBERS OF DAYS LEFT
            user_data = {"_id": newuser.idmember, "intra": newuser.intra_db, "cur": newuser.cursus, "bh": newuser.days}
            await asyncio.sleep(0.05)
            if not self.base.find_one({"_id":newuser.idmember}): #if not in database, insert
                self.base.insert_one(user_data) #insert database
            elif self.base.find_one({"_id":newuser.idmember}): #if already in database
                newuser.nema = self.base.find({"_id":newuser.idmember})
                await newuser.user2.send(f"Erreur innatendue, demandez de l'aide à un Bot Helper.")
                return
            await asyncio.sleep(0.05)

            await add_role(self, newuser.user2, newuser.cursus) #add role piscine (Pool)
            channel_pool = self.client.get_channel(id=809813638981877820) #Welcome channel
            await channel_pool.send(f'Bienvenu à {newuser.user2.nick} !') #Send welcome message
            await newuser.user2.send("Bienvenu(e) sur le Discord de 42 Nice !") #Final Message
            await asyncio.sleep(0.05)
            return                        
        else: #Else, if user couldn't be found on the intra
            pass
            await newuser.user2.send("Nous n'avons pas pu vous trouver sur L'intra, si vous pensez que c'est une erreur contactez NotJustJoe#3756 ou un Bot Helper sur le Discord")
            return

def setup(client):
    client.add_cog(intralog(client))