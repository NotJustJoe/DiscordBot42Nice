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
from secret.hidden import cluster
from secret.hidden import token
from flask import Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import math
import sys
import os

db = cluster["42NiceDiscord"]
base = db["base_info"]
cwd = Path(__file__).parents[0]
cwd = str(cwd)

client = commands.Bot(command_prefix = "!",intents = discord.Intents.all(), owner_id=189816540089024512)
client.remove_command('help')
client.x = 0

client.base  = base

@commands.is_owner() #load command
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@commands.is_owner() #unload command, disable X commands
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@commands.is_owner() #unload and reload commands
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

client.run(token)