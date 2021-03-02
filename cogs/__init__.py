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
class __init__cogs(commands.Cog):
    #Initialisation of class
    def __init__(self, client):
        self.client = client
    #This is a event command
    @commands.Cog.listener()
    async def on_ready(self):
        print("__init__ Cogs is loaded")
    #This is a command

def setup(client):
    client.add_cog(__init__cogs(client))