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

    #Name of the class to import in setup
class subjects_pool_c(commands.Cog):
    #Initialisation of class
    def __init__(self, client):
        self.client = client
    #This is a event command
    @commands.Cog.listener()
    async def on_ready(self):
        print("Subjects Pool is loaded")
    #This is a command
    @commands.command()
    async def pool(self, ctx):
        embed = discord.Embed(
            title = f"All Pool Subjects",
            colour =  discord.Colour.dark_blue()
        )
        embed.add_field(name = "Shell00", value = "[PDF Shell00](https://cdn.intra.42.fr/pdf/pdf/15748/fr.subject.pdf)")
        embed.add_field(name = "Shell01", value = "[PDF Shell01](https://cdn.intra.42.fr/pdf/pdf/15975/fr.subject.pdf)")
        embed.add_field(name="\u200b",value="\u200b")
        embed.add_field(name = "C00", value = "[PDF C00](https://cdn.intra.42.fr/pdf/pdf/15975/fr.subject.pdf)")
        embed.add_field(name = "C01", value = "[PDF C01](https://cdn.intra.42.fr/pdf/pdf/15999/fr.subject.pdf)")
        embed.add_field(name = "C02", value = "[PDF C02](https://cdn.intra.42.fr/pdf/pdf/12978/fr.subject.pdf)")
        embed.add_field(name = "C03", value = "[PDF C03](https://projects.intra.42.fr/projects/c-piscine-c-03)")
        embed.add_field(name = "C04", value = "[PDF C04](https://cdn.intra.42.fr/pdf/pdf/12962/fr.subject.pdf)")
        embed.add_field(name = "C05", value = "[PDF C05](https://cdn.intra.42.fr/pdf/pdf/15396/fr.subject.pdf)")
        embed.add_field(name = "C06", value = "[PDF C06](https://cdn.intra.42.fr/pdf/pdf/16048/fr.subject.pdf)")
        embed.add_field(name = "C07", value = "[PDF C07](https://cdn.intra.42.fr/pdf/pdf/16031/fr.subject.pdf)")
        embed.add_field(name = "C08", value = "[PDF C08](https://cdn.intra.42.fr/pdf/pdf/16042/fr.subject.pdf)")
        embed.add_field(name = "C09", value = "[PDF C09](https://cdn.intra.42.fr/pdf/pdf/16007/fr.subject.pdf)")
        embed.add_field(name = "C10", value = "[PDF C10](https://cdn.intra.42.fr/pdf/pdf/13795/fr.subject.pdf)")
        embed.add_field(name = "C11", value = "[PDF C11](https://cdn.intra.42.fr/pdf/pdf/16023/fr.subject.pdf)")
        embed.add_field(name = "C12", value = "[PDF C12](https://cdn.intra.42.fr/pdf/pdf/16388/fr.subject.pdf)")
        embed.add_field(name = "C13", value = "[PDF C13](https://cdn.intra.42.fr/pdf/pdf/16186/fr.subject.pdf)")
        embed.add_field(name="\u200b",value="\u200b")

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(subjects_pool_c(client))