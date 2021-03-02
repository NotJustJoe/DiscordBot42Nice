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
        self.user2 = discord.User
        self.idmember = 420
        self.intra_name = 'error 31 new_user.py'
        self.channel = 808327973056938007
        self.intraembed = discord.Embed
        self.intrasend = 'error 103 new_user.py'
        self.msg = 'error 96 new_user.py'
        self.nema = 69
        self.embed = discord.Embed
        self.guild = 808327973056938004
        self.remrole = 'hi'
    #Name of the class to import in setup
class intralog(commands.Cog):
    #Initialisation of class
    def __init__(self, client):
        self.client = client
    #This is a event command
    @commands.Cog.listener()
    async def on_ready(self):
        print("Intralog is loaded")

    #This is a command
    @commands.command()
    async def intralog(self, ctx):
        newuser = new_memb()
        newuser.guild = self.client.get_guild(808327973056938004)
        newuser.user2 = newuser.guild.get_member(ctx.message.author.id)
        newuser.remrole = newuser.guild.get_member.roles

        async def remove(self, member, ROLE):
            role = get(member.guild.roles, name=ROLE)
            await newuser.user2.remove_roles(role)

        for newuser.remrole in newuser.guild.members:
            for roles in newuser.user2.roles:
                if roles.name == 'Student':
                    await remove(self, newuser.user2, 'Student')
                elif roles.name == 'Pool':
                    await remove(self, newuser.user2, 'Pool')
        #user_data = {"_id": intraname, "cur": cursus, "bh": days} #DB
        #user_data = {"_id": trofidal, "cursus": Pool, "blackwhole_absorption": 194} EXEMPLE
        #collection.find_one("_id") muted to silence errors
        newuser.idmember = newuser.user2.id #idmember = member.id

        newuser.embed = discord.Embed(colour=discord.Colour.dark_gold(), description=f'Welcome to The 42 Nice Discord ! Open the private message of the bot to access the discord !')
        newuser.embed.set_thumbnail(url=f'{newuser.user2.guild.icon_url}')
        newuser.embed.set_author(name=f'{str(newuser.user2)}', icon_url=f'{newuser.user2.avatar_url}')
        newuser.embed.add_field(name="Account Created", value=newuser.user2.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        newuser.embed.set_footer(text=f'{newuser.user2.guild}', icon_url=f'{newuser.user2.guild.icon_url}')
        newuser.embed.timestamp = datetime.datetime.utcnow()
        newuser.channel = self.client.get_channel(id=808327973056938007)
        await newuser.channel.send(embed=newuser.embed)
        await asyncio.sleep(2)
        #######################################################

        async def add_role(self, member, ROLE):
            role = get(member.guild.roles, name=ROLE)
            await newuser.user2.add_roles(role)
        
        async def chnick(member: discord.Member, nick):
            await newuser.user2.edit(nick=nick)
            await newuser.user2.send(f'Your nickname was changed for {newuser.user2.nick}')

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
            title = 'Please write your intra name in lower case',
            colour = discord.Colour.dark_gold()
        )
        newuser.intrasend = await newuser.user2.send(embed=newuser.intra_name)
        ##########################################################
        #HERE WAS FUNCTION DEFENITION
        try:
            newuser.msg = await self.client.wait_for(
                "message",
                timeout = 300,
                check = lambda message: message.author == newuser.user2 and str(newuser.user2.id) != "808368692068876298"
            )
            if newuser.msg:
                await newuser.user2.send(f"Your intra name is {newuser.msg.content} ?")
                newuser.intra_db = newuser.msg.content
            intra_emoji = [
            "✅",
            "❌",
            ]
            for i in intra_emoji:
                asyncio.gather(newuser.intrasend.add_reaction(i))
            def checkEmoji1(reaction):
                if str(reaction.user_id) == "808368692068876298":
                    return False
                return True
            while(True):
                try:
                    reaction = await self.client.wait_for("raw_reaction_add", timeout = 0.1,check = checkEmoji1)
                except asyncio.TimeoutError:
                    continue
                else:
                    if reaction.emoji.name == "❌":
                        await newuser.user2.send("Aborting ... Rerun the command with !intralog")
                        return
                    elif reaction.emoji.name == "✅":                    
                        if 0 == 0: #CHECK IF USER IS STUDENT
                            await newuser.user2.send(f"Your account will be checked for 👨‍🎓 Student.")
                            newuser.cursus = 'Student' #WE WILL CHECK INSIDE INTRA TO SEE IF HE IS POOL
                            newuser.days = '160' #WE WILL CHECK INSIDE INTRA TO SEE NUMBERS OF DAYS LEFT  
                            #if not self.base.find_one({"_id":newuser.idmember}):
                            #    self.base.insert_one(newuser.user_data)
                            #elif self.base.find_one({"_id":newuser.idmember}):  #Si deja database
                            #    newuser.nema = self.base.find({"_id":newuser.idmember})
                            #    for newuser.i in newuser.nema:
                            #        newuser.intre = newuser.i["intra"]
                            #        await newuser.user2.send(f"You are already in the database as {newuser.intre}, use !clearintra to remove you from the database.")
                            #        return
                            #    await newuser.user2.send(f"Error ! The bot didn't found you on the Intra or your account has run out of time !\nIf you think this is an error, contact the bot owner.")
                            #    return
                            await chnick(newuser.user2, newuser.intra_db)
                            await add_role(self, newuser.user2, 'Student')
                            channel_stud = self.client.get_channel(id=809813638981877820)
                            await channel_stud.send(f'Welcome to our new Student {newuser.user2.nick} !')
                            await newuser.user2.send(f"Everything went perfectly, welcome to the 42 Discord !")
                            return
                        elif 0 == 1: #CHECK IF USER IS POOL
                            await newuser.user2.send(f"Choice Confirmed ! Your account will be checked for 🏊‍♂️ Pool.")
                            newuser.cursus = 'Pool'
                            newuser.days = '113' #WE WILL CHECK INSIDE INTRA TO SEE NUMBERS OF DAYS LEFT
                            #if not self.base.find_one({"_id":newuser.idmember}): #REGARDE SI PAS SUR DB
                            #    self.base.insert_one(newuser.user_data) #insert base de donnee
                            #elif self.base.find_one({"_id":newuser.idmember}): #Si deja database
                            #    newuser.nema = self.base.find({"_id":newuser.idmember})
                            #    for newuser.i in newuser.nema:
                            #        newuser.intre = newuser.i["intra"]
                            #        await newuser.user2.send(f"You are already in the database as {newuser.intre}, use !clearintra to remove you from the database.")
                            #        return
                            #    await newuser.user2.send(f"Error ! The bot didn't found you on the Intra or your account has run out of time !\nIf you think this is an error, contact the bot owner.")
                            #    return
                            await chnick(newuser.user2, newuser.intra_db)
                            await add_role(self, newuser.user2, newuser.cursus) #'Pool' was here before
                            channel_pool = self.client.get_channel(id=809813705290022922)
                            await channel_pool.send(f'Welcome to our new Pool member {newuser.user2.nick} !')
                            await newuser.user2.send("Everything went perfectly, welcome to the 42 Discord !")
                            return                        
                        else: #Message si l'user n'est pas sur l'intra
                            pass
                            await newuser.user2.send("Aborting... rerun the command !intralog, if you want to remove yourself from the database, use !clearintra")
                            return

        except asyncio.TimeoutError:
            await newuser.intrasend.delete()
            await newuser.user2.send("Cancelling due to timeout, rerun the command with !intralog")
            return  

def setup(client):
    client.add_cog(intralog(client))