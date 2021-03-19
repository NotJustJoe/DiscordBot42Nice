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

        newuser.embed = discord.Embed(colour=discord.Colour.dark_gold(), description=f'Welcome to The 42 Nice Discord ! Open the private message of the bot to access the discord !')
        newuser.embed.set_thumbnail(url=f'{newuser.user2.guild.icon_url}')
        newuser.embed.set_author(name=f'{str(newuser.user2)}', icon_url=f'{newuser.user2.avatar_url}')
        newuser.embed.add_field(name="Account Created", value=newuser.user2.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        newuser.embed.set_footer(text=f'{newuser.user2.guild}', icon_url=f'{newuser.user2.guild.icon_url}')
        newuser.embed.timestamp = datetime.datetime.utcnow()
        newuser.channel = self.client.get_channel(id=808327973056938007)
        await newuser.channel.send(embed=newuser.embed)
        #######################################################

        async def add_role(self, member, ROLE):
            role = get(member.guild.roles, name=ROLE)
            await newuser.user2.add_roles(role)
        
        async def chnick(member: discord.Member, nick):
            await newuser.user2.edit(nick=nick)
            await newuser.user2.send(f'Votre pseudo a été changé pour {newuser.user2.nick} sur le Discord')

        async def cleardm(self, amount):
            async for message in self.client.get_user(189816540089024512).history(limit=(int(amount))):
                if message.author.id == self.client.user.id:
                    amount = int(amount) + 1
                    await message.delete()
                    await asyncio.sleep(0.5)
                elif message.author.id == self.client.user.id:
                    amount = int(amount) + 1
        await asyncio.sleep(1)
        newuser.intra_name = discord.Embed(
            title = 'Ecrivez votre intra en minuscule',
            colour = discord.Colour.dark_gold()
        )
        newuser.intrasend = await newuser.user2.send(embed=newuser.intra_name)
        ##########################################################
        #HERE WAS FUNCTION DEFENITION
        try:
            newuser.msg = await self.client.wait_for(
                "message",
                timeout = 600,
                check = lambda message: message.author == newuser.user2 and str(newuser.user2.id) != "808368692068876298"
            )
            if newuser.msg:
                newuser.intra_db = newuser.msg.content
        except asyncio.TimeoutError:
            await newuser.intrasend.delete()
            await newuser.user2.send("Cancelling due to timeout, rerun the command with !intralog")
            return  
        if 0 == 0: #Condition is 1 == 1 because i dont have access to the intra API yet, every user joining the discord at the moment are confirmed students
            user_data = {"_id": newuser.idmember, "intra": newuser.intra_db, "cur": newuser.cursus, "bh": newuser.days}
            newuser.cursus = 'Student' #WE WILL CHECK INSIDE INTRA TO SEE IF HE IS STUDENT
            newuser.days = '160' #WE WILL CHECK INSIDE INTRA TO SEE NUMBERS OF DAYS LEFT  
            #PROBLEME ICI POSSIBLE -> INT -> CHAR IDMEMBER
            await asyncio.sleep(0.05)
            if not self.base.find_one({"_id":newuser.idmember}):#if not in database, insert
                self.base.insert_one(user_data) #insert database
            elif self.base.find_one({"_id":newuser.idmember}): #if already in database
                newuser.nema = self.base.find({"_id":newuser.idmember})
                await newuser.user2.send(f"Erreur ! Vous avez déjà essayer de rejoindre ce discord par le passé.")
                return
            await asyncio.sleep(0.05)
            await chnick(newuser.user2, newuser.intra_db)
            await add_role(self, newuser.user2, 'Student')
            channel_stud = self.client.get_channel(id=809813638981877820)
            await channel_stud.send(f'Bienvenu à {newuser.user2.nick} !')
            await newuser.user2.send(f"Bienvenu(e) sur le Discord de 42 Nice !")
            await asyncio.sleep(0.05)
            return
        elif 0 == 1: #Condition is 0 == 1 because i dont have access to the intra API yet, so i can't check if the user IS pool or not
            user_data = {"_id": newuser.idmember, "intra": newuser.intra_db, "cur": newuser.cursus, "bh": newuser.days}
            newuser.cursus = 'Pool'
            newuser.days = '113' #WE WILL CHECK INSIDE INTRA TO SEE NUMBERS OF DAYS LEFT
            await asyncio.sleep(0.05)
            if not self.base.find_one({"_id":newuser.idmember}): #if not in database, insert
                self.base.insert_one(user_data) #insert database
            elif self.base.find_one({"_id":newuser.idmember}): #if already in database
                newuser.nema = self.base.find({"_id":newuser.idmember})
                await newuser.user2.send(f"Erreur ! Vous avez déjà essayer de rejoindre ce discord par le passé.")
                return
            await asyncio.sleep(0.05)
            await chnick(newuser.user2, newuser.intra_db) #Change username with intraname given
            await add_role(self, newuser.user2, newuser.cursus) #add role piscine (Pool)
            channel_pool = self.client.get_channel(id=809813705290022922) #Welcome channel
            await channel_pool.send(f'Bienvenu à {newuser.user2.nick} !') #Send welcome message
            await newuser.user2.send("Bienvenu(e) sur le Discord de 42 Nice !") #Final Message
            await asyncio.sleep(0.05)
            return                        
        else: #Else, if user couldn't be found on the intra
            pass
            await newuser.user2.send("Nous n'avons pas pu vous trouver sur L'intra, si vous pensez que c'est une erreur contactez NotJustJoe#3756")
            return

def setup(client):
    client.add_cog(New_user(client))