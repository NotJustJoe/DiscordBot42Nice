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
class intralinkdata():
	def __init__(self):
		self.name = "Name not Found"
		self.black_whole_days = "Days left not found"
		self.last_project_done = "No project redeemed"
		self.actual_cursus = "Not Found"
		self.correction_points = "0"
		self.level = "0"

class intralinked(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("intralinked is loaded")

	@commands.command()
	async def stats(self, ctx, intra):
		intra = intralinkdata()
		intra.name = "Name not Found"
		intra.black_whole_days = "Days left not found"
		intra.last_project_done = "No project redeemed"
		intra.actual_cursus = "Not Found"
		intra.correction_points = "0"
		intra.level = "0"

		embed = discord.Embed(
			title = f'Intra Card',
			colour = discord.Colour.dark_gold()
		)
		embed.add_field(name="Intra Log", value=intra.name)
		embed.add_field(name="Blackwhole", value=f"{intra.black_whole_days} Days left")
		embed.add_field(name="Last Project",value=f"{intra.last_project_done}")
		embed.add_field(name="Correction Points", value=f"{intra.correction_points} Points")
		embed.add_field(name="Level", value=f"{intra.level}")

		await ctx.send(embed=embed)


def setup(client):
	client.add_cog(intralinked(client))