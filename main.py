import discord
from discord.ext import commands
from discord import *
from discord.ext.commands import *
import random
from bs4 import BeautifulSoup
import requests

bot = commands.Bot(command_prefix='>')

TOKEN = "SU-TOKEN"

@bot.command()
async def search(ctx, *, pp):
	nume = pp
	lista = [int(a) for a in str(nume)]
	img = (f'{lista[3]}{lista[4]}')
	rrr = (f'{lista[6]}{lista[7]}')
	num = 0

	if int(lista[0]) == 1:
		Base = ':seedling: Plant'
	elif int(lista[0]) == 2:
		Base = ':evergreen_tree: Mother Tree'

	if int(lista[5]) == 1:
		rr = 1
		rareza = ":green_circle: Common"

	if int(lista[5]) == 2:
		if int(rrr) <= 88:
			rareza = ":blue_circle: Uncommun"
		else:
			rareza = ":red_circle: Rare"
		rr = 2

	if int(lista[5]) == 3:
		rr = 3
		rareza = ":purple_circle: Mysthic"

	if int(lista[0]) == 1:
		hh = (f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/{img}_{rr}.png")
	else:
		hh = (f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/mtree/{img}_{rr}.png")

	if int(img) == 18:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			num = 1200 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1250 + int(rrr)
			else:
				num = 1311 + int(rrr)
		if int(lista[5]) == 3:
			num = 1401 + int(rrr)
		prd = 240
		poo = num / prd

	elif int(img) == 19:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			num = 1200 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1250 + int(rrr)
			else:
				num = 1311 + int(rrr)
		if int(lista[5]) == 3:
			num = 1401 + int(rrr)
		prd = 240
		poo = num / prd

	elif int(img) == 20:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			num = 1600 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1650 + int(rrr)
			else:
				num = 1711 + int(rrr)
		if int(lista[5]) == 3:
			num = 1901 + int(rrr)
		prd = 312
		poo = num / prd

	elif int(img) == 21:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			num = 1600 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1650 + int(rrr)
			else:
				num = 1711 + int(rrr)
		if int(lista[5]) == 3:
			num = 1901 + int(rrr)
		prd = 312
		poo = num / prd

	elif int(img) == 91:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 5
				num = 1400 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				num = 1450 + sum
			else:
				sum = int(rrr) * 5
				num = 1495 + sum
		if int(lista[5]) == 3:
			num = 2120
		prd = 240
		poo = num / prd

	elif int(img) == 00:
		Plant = ':fire: Fire'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/0_{rr}.png"
		if int(lista[5]) == 1:
			num = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 440 + int(rrr)
			else:
				num = 511 + int(rrr)
		if int(lista[5]) == 3:
			num = 701 + int(rrr)
		prd = 48
		poo = num / prd

	elif int(img) == 1:
		Plant = ':fire: Fire'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/1_{rr}.png"
		if int(lista[5]) == 1:
			num = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 440 + int(rrr)
			else:
				num = 511 + int(rrr)
		if int(lista[5]) == 3:
			num = 701 + int(rrr)
		prd = 48
		poo = num / prd

	elif int(img) == 7:
		Plant = ':fire: Fire'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/7_{rr}.png"
		if int(lista[5]) == 1:
			num = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 440 + int(rrr)
			else:
				num = 511 + int(rrr)
		if int(lista[5]) == 3:
			num = 701 + int(rrr)
		prd = 48
		poo = num / prd

	elif int(img) == 17:
		Plant = ':fire: Fire'
		if int(lista[5]) == 1:
			num = 650 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 700 + int(rrr)
			else:
				num = 811 + int(rrr)
		if int(lista[5]) == 3:
			num = 1001 + int(rrr)
		prd = 72
		poo = num / prd

	elif int(img) == 30:
		Plant = ':fire: Fire'
		if int(lista[5]) == 1:
			num = 650 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 700 + int(rrr)
			else:
				num = 811 + int(rrr)
		if int(lista[5]) == 3:
			num = 1001 + int(rrr)
		prd = 72
		poo = num / prd

	elif int(img) == 90:
		Plant = ':fire: Fire'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 5
				num = 750 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				num = 800 + sum
			else:
				sum = int(rrr) * 5
				num = 855 + sum
		if int(lista[5]) == 3:
			num = 1500
		prd = 48
		poo = num / prd

	elif int(img) == 33:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			if int(rrr) >= 10:
				sum = int(rrr) * 10
				num = 1400 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 1500 + sum
			else:
				sum = int(rrr) * 10
				num = 1610 + sum
		if int(lista[5]) == 3:
			sum = int(rrr) * 10
			num = 1810 + sum
		prd = 216
		poo = num / prd

	elif int(img) == 35:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			if int(rrr) >= 10:
				sum = int(rrr) * 10
				num = 1400 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 1500 + sum
			else:
				sum = int(rrr) * 10
				num = 1610 + sum
		if int(lista[5]) == 3:
			sum = int(rrr) * 10
			num = 1810 + sum
		prd = 216
		poo = num / prd

	elif int(img) == 14:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			if int(rrr) >= 10:
				sum = int(rrr) * 10
				num = 1200 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 1300 + sum
			else:
				sum = int(rrr) * 10
				num = 1410 + sum
		if int(lista[5]) == 3:
			sum = int(rrr) * 10
			num = 1510 + sum
		prd = 192
		poo = num / prd

	elif int(img) == 31:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			sum = int(rrr) * 10
			num = 1200 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 1300 + sum
			else:
				sum = int(rrr) * 10
				num = 1410 + sum
		if int(lista[5]) == 3:
			sum = int(rrr) * 10
			num = 1510 + sum
		prd = 192
		poo = num / prd

	elif int(img) == 93:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 5
				num = 2600 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				num = 2650 + sum
			else:
				sum = int(rrr) * 5
				num = 2705 + sum
		if int(lista[5]) == 3:
			num = 3300
		prd = 216
		poo = num / prd

	elif int(img) == 34:
		Plant = ':zap: Electro'
		if int(lista[5]) == 1:
			num = 650 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 700 + int(rrr)
			else:
				num = 811 + int(rrr)
		if int(lista[5]) == 3:
			num = 1001 + int(rrr)
		prd = 60
		poo = num / prd

	elif int(img) == 32:
		Plant = ':zap: Electro'
		if int(lista[5]) == 1:
			num = 650 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 700 + int(rrr)
			else:
				num = 811 + int(rrr)
		if int(lista[5]) == 3:
			num = 1001 + int(rrr)
		prd = 60
		poo = num / prd

	elif int(img) == 8:
		Plant = ':zap: Electro'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/8_{rr}.png"
		if int(lista[5]) == 1:
			num = 500 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 550 + int(rrr)
			else:
				num = 591 + int(rrr)
		if int(lista[5]) == 3:
			num = 751 + int(rrr)
		prd = 48
		poo = num / prd

	elif int(img) == 3:
		Plant = ':zap: Electro'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/3_{rr}.png"
		if int(lista[5]) == 1:
			num = 500 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 550 + int(rrr)
			else:
				num = 591 + int(rrr)
		if int(lista[5]) == 3:
			num = 751 + int(rrr)
		prd = 48
		poo = num / prd

	elif int(img) == 15:
		Plant = ':zap: Electro'
		if int(lista[5]) == 1:
			num = 500 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 550 + int(rrr)
			else:
				num = 591 + int(rrr)
		if int(lista[5]) == 3:
			num = 751 + int(rrr)
		prd = 48
		poo = num / prd

	elif int(img) == 29:
		Plant = ':snowflake: Ice'
		if int(lista[5]) == 1:
			num = 800 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 850 + int(rrr)
			else:
				num = 911 + int(rrr)
		if int(lista[5]) == 3:
			num = 1151 + int(rrr)
		prd = 96
		poo = num / prd

	elif int(img) == 2:
		Plant = ':snowflake: Ice'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/2_{rr}.png"
		if int(lista[5]) == 1:
			num = 500 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 550 + int(rrr)
			else:
				num = 591 + int(rrr)
		if int(lista[5]) == 3:
			num = 751 + int(rrr)
		prd = 60
		poo = num / prd

	elif int(img) == 6:
		Plant = ':snowflake: Ice'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/6_{rr}.png"
		if int(lista[5]) == 1:
			num = 500 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 550 + int(rrr)
			else:
				num = 591 + int(rrr)
		if int(lista[5]) == 3:
			num = 751 + int(rrr)
		prd = 60
		poo = num / prd

	elif int(img) == 92:
		Plant = ':snowflake: Ice'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 5
				num = 1050 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				num = 1100 + sum
			else:
				sum = int(rrr) * 5
				num = 1155 + sum
		if int(lista[5]) == 3:
			num = 1800
		prd = 96
		poo = num / prd

	elif int(img) == 24:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			num = 1300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1350 + int(rrr)
			else:
				num = 1411 + int(rrr)
		if int(lista[5]) == 3:
			num = 1551 + int(rrr)
		prd = 168
		poo = num / prd

	elif int(img) == 23:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			num = 1300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1350 + int(rrr)
			else:
				num = 1411 + int(rrr)
		if int(lista[5]) == 3:
			num = 1551 + int(rrr)
		prd = 168
		poo = num / prd

	elif int(img) == 22:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			num = 1300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1350 + int(rrr)
			else:
				num = 1411 + int(rrr)
		if int(lista[5]) == 3:
			num = 1551 + int(rrr)
		prd = 168
		poo = num / prd

	elif int(img) == 12:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			num = 900 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 950 + int(rrr)
			else:
				num = 1011 + int(rrr)
		if int(lista[5]) == 3:
			num = 1151 + int(rrr)
		prd = 120
		poo = num / prd

	elif int(img) == 13:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			num = 900 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 950 + int(rrr)
			else:
				num = 1011 + int(rrr)
		if int(lista[5]) == 3:
			num = 1151 + int(rrr)
		prd = 120
		poo = num / prd

	elif int(img) == 11:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			num = 900 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 950 + int(rrr)
			else:
				num = 1011 + int(rrr)
		if int(lista[5]) == 3:
			num = 1151 + int(rrr)
		prd = 120
		poo = num / prd

	elif int(img) == 25:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 10
				num = 3500 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 3700 + sum
			else:
				sum = int(rrr) * 10
				num = 3910 + sum
		if int(rrr) == 3:
			sum = int(rrr) * 10
			num = 4210 + sum
		prd = 336
		poo = num / prd

	elif int(img) == 26:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 10
				num = 3500 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 3700 + sum
			else:
				sum = int(rrr) * 10
				num = 3910 + sum
		if int(rrr) == 3:
			sum = int(rrr) * 10
			num = 4210 + sum
		prd = 336
		poo = num / prd

	elif int(img) == 27:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 10
				num = 5500 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 5800 + sum
			else:
				sum = int(rrr) * 10
				num = 5910 + sum
		if int(lista[5]) == 3:
			sum = int(rrr) * 10
			num = 6110 + sum
		prd = 480
		poo = num / prd

	elif int(img) == 28:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			if int(rrr) >= 0:
				sum = int(rrr) * 10
				num = 5500 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				num = 5800 + sum
			else:
				sum = int(rrr) * 10
				num = 5910 + sum
		if int(lista[5]) == 3:
			sum = int(rrr) * 10
			num = 6110 + sum
		prd = 480
		poo = num / prd

	elif int(img) == 4:
		Plant = ':droplet: Water'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/4_{rr}.png"
		if int(lista[5]) == 1:
			num = 950 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1040 + int(rrr)
			else:
				num = 1111 + int(rrr)
		if int(lista[5]) == 3:
			num = 1301 + int(rrr)
		prd = 108
		poo = num / prd

	elif int(img) == 5:
		Plant = ':droplet: Water'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/5_{rr}.png"
		if int(lista[5]) == 1:
			num = 950 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1040 + int(rrr)
			else:
				num = 1111 + int(rrr)
		if int(lista[5]) == 3:
			num = 1301 + int(rrr)
		prd = 108
		poo = num / prd

	elif int(img) == 36:
		Plant = ':droplet: Water'
		if int(lista[5]) == 1:
			num = 950 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1040 + int(rrr)
			else:
				num = 1111 + int(rrr)
		if int(lista[5]) == 3:
			num = 1301 + int(rrr)
		prd = 108
		poo = num / prd

	elif int(img) == 38:
		Plant = ':droplet: Water'
		if int(lista[5]) == 1:
			num = 1050 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1140 + int(rrr)
			else:
				num = 1211 + int(rrr)
		if int(lista[5]) == 3:
			num = 1401 + int(rrr)
		prd = 120
		poo = num / prd

	elif int(img) == 39:
		Plant = ':droplet: Water'
		if int(lista[5]) == 1:
			num = 1050 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 1140 + int(rrr)
			else:
				num = 1211 + int(rrr)
		if int(lista[5]) == 3:
			num = 1401 + int(rrr)
		prd = 120
		poo = num / prd

	elif int(img) == 37:
		Plant = ':butterfly: Wind'
		if int(lista[5]) == 1:
			num = 900 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 950 + int(rrr)
			else:
				num = 1011 + int(rrr)
		if int(lista[5]) == 3:
			num = 1151 + int(rrr)
		prd = 96
		poo = num / prd

	elif int(img) == 16:
		Plant = ':butterfly: Wind'
		if int(lista[5]) == 1:
			num = 900 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 950 + int(rrr)
			else:
				num = 1011 + int(rrr)
		if int(lista[5]) == 3:
			num = 1151 + int(rrr)
		prd = 96
		poo = num / prd

	elif int(img) == 10:
		Plant = ':butterfly: Wind'
		if int(lista[5]) == 1:
			num = 750 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 800 + int(rrr)
			else:
				num = 861 + int(rrr)
		if int(lista[5]) == 3:
			num = 1051 + int(rrr)
		prd = 72
		poo = num / prd

	elif int(img) == 9:
		Plant = ':butterfly: Wind'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/9_{rr}.png"
		if int(lista[5]) == 1:
			num = 750 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				num = 800 + int(rrr)
			else:
				num = 861 + int(rrr)
		if int(lista[5]) == 3:
			num = 1051 + int(rrr)
		prd = 72
		poo = num / prd

	kkk = round(poo,3)
	ggg = kkk * 24
	aaa = round(ggg,4)
	lll = ggg * 7
	ooo = int(round(lll,0))
	nnn = ggg * 30
	mmm = int(round(nnn,0))

	embed = discord.Embed(title="Type", description=f"{Base}", color=discord.Colour.dark_green())
	embed.set_thumbnail(url=f"{hh}")
	embed.add_field(name="Element", value=f"{Plant}")
	embed.add_field(name="Rarity", value=f"{rareza}")
	embed.add_field(name="Production", value=f":large_blue_diamond: LE: {num}/{prd} HR", inline=False)
	embed.add_field(name="Time-Lapse Production", value=f":large_blue_diamond: LE: {kkk} / HR \n :large_blue_diamond: LE: {aaa} / Day \n :large_blue_diamond: LE: {ooo} / Week \n :large_blue_diamond: LE: {mmm} / Month")
	embed.set_footer(text="Created by @AlexanderJGA#0399")
	await ctx.send(embed=embed)

@bot.command()
async def pvp(ctx, *, pp):
	nume = pp
	lista = [int(a) for a in str(nume)]
	img = (f'{lista[3]}{lista[4]}')
	rrr = (f'{lista[6]}{lista[7]}')
	att1 = 0
	att2 = 0
	att3 = 0
	att4 = 0
	atk = 0
	defet = 0
	hitp = 0
	print(lista)
	print(img)

	if int(lista[0]) == 1:
		Base = ':seedling: Plant'
	elif int(lista[0]) == 2:
		Base = ':evergreen_tree: Mother Tree'

	if int(lista[5]) == 1:
		rr = 1
		rareza = ":green_circle: Common"

	if int(lista[5]) == 2:
		if int(rrr) <= 88:
			rareza = ":blue_circle: Uncommun"
		else:
			rareza = ":red_circle: Rare"
		rr = 2

	if int(lista[5]) == 3:
		rr = 3
		rareza = ":purple_circle: Mysthic"

	if int(lista[0]) == 1:
		hh = (f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/{img}_{rr}.png")
	else:
		hh = (f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/mtree/{img}_{rr}.png")

	if int(img) == 18:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 80 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 145
		if int(lista[5]) == 3:
			att1 = 400

	elif int(img) == 19:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			att3 = 150 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 100 + sum
			else:
				sum = int(rrr) * 5
				att3 = sum - 145
		if int(lista[5]) == 3:
			att3 = 400

	elif int(img) == 20:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			att1 = 1000 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att1 = 1000 + sum
			else:
				sum = int(rrr) * 10
				att1 = 650 + sum
		if int(lista[5]) == 3:
			att1 = 2000

	elif int(img) == 21:
		Plant = ':sunny: Light'
		if int(lista[5]) == 1:
			att3 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att3 = 100 + sum
			else:
				att3 = 574 + int(rrr)
		if int(lista[5]) == 3:
			att3 = 750

	elif int(img) == 91:
		Plant = ':sunny: Light'
		atk = 125
		defet = 300
		if int(lista[5]) == 1:
			sum = int(rrr) * 100
			hitp = 15000 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 200
				hitp = 9000 + sum
			else:
				sum = int(rrr) * 500
				hitp = sum - 15500
		if int(lista[5]) == 3:
			hitp = 37500

	elif int(img) == 00:
		Plant = ':fire: Fire'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/0_{rr}.png"
		if int(lista[5]) == 1:
			att1 = 1000 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				att1 = 650 + sum
			else:
				sum = int(rrr) * 10
				att1 = 650 + sum
		if int(lista[5]) == 3:
			att1 = 2000

	elif int(img) == 1:
		Plant = ':fire: Fire'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/1_{rr}.png"
		if int(lista[5]) == 1:
			att3 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att3 = 100 + sum
			else:
				att3 = 574 + int(rrr)
		if int(lista[5]) == 3:
			att3 = 750

	elif int(img) == 7:
		Plant = ':fire: Fire'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/7_{rr}.png"
		if int(lista[5]) == 1:
			att1 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 280 + sum
			else:
				att1 = 415 + int(rrr)
		if int(lista[5]) == 3:
			att1 = 650

	elif int(img) == 17:
		Plant = ':fire: Fire'
		if int(lista[5]) == 1:
			att1 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 280 + sum
			else:
				att1 = 415 + int(rrr)
		if int(lista[5]) == 3:
			att1 = 650

	elif int(img) == 30:
		Plant = ':fire: Fire'
		if int(lista[5]) == 1:
			att1 = 1000 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 10
				att1 = 650 + sum
			else:
				sum = int(rrr) * 10
				att1 = 650 + sum
		if int(lista[5]) == 3:
			att1 = 2000

	elif int(img) == 90:
		Plant = ':fire: Fire'
		atk = 200
		defet = 200
		if int(lista[5]) == 1:
			sum = int(rrr) * 100
			hitp = 10000 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 200
				hitp = 8000 + sum
			else:
				sum = int(rrr) * 500
				hitp = sum - 17000
		if int(lista[5]) == 3:
			hitp = 35000

	elif int(img) == 33:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 55 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 195
		if int(lista[5]) == 3:
			att1 = 2800
		
	elif int(img) == 35:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 380 + sum
			else:
				sum = int(rrr) * 5
				att3 = 155 + sum
		if int(lista[5]) == 3:
			att3 = 2800

	elif int(img) == 14:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			iii = int(rrr) / 1000
			pppp = 0.200 + iii
			att2 = float(pppp)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				iii = int(rrr) / 1000
				bbb = iii * 2
				pppp = 0.180 + bbb
				att2 = float(pppp)
			else:
				iii = int(rrr) / 1000
				bbb = iii * 5
				pppp = bbb - 0.045
				att2 = float(pppp)
		if int(lista[5]) == 3:
			att2 = 0.5

	elif int(img) == 31:
		Plant = ':spades: Dark'
		if int(lista[5]) == 1:
			att3 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att3 = 100 + sum
			else:
				sum = int(rrr) * 10
				att3 = sum - 290
		if int(lista[5]) == 3:
			att3 = 2500
		
	elif int(img) == 93:
		Plant = ':spades: Dark'
		atk = 400
		defet = 100
		if int(lista[5]) == 1:
			sum = int(rrr) * 50
			hitp = 7500 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 100
				hitp = 5000 + sum
			else:
				sum = int(rrr) * 500
				hitp = sum - 29500
		if int(lista[5]) == 3:
			hitp = 25000

	elif int(img) == 34:
		Plant = ':zap: Electro'
		if int(lista[5]) == 1:
			iii = int(rrr) / 1000
			pppp = 0.200 + iii
			att2 = float(pppp)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				iii = int(rrr) / 1000
				bbb = iii * 2
				pppp = 0.180 + bbb
				att2 = float(pppp)
			else:
				iii = int(rrr) / 1000
				bbb = iii * 5
				pppp = bbb - 0.045
				att2 = float(pppp)
		if int(lista[5]) == 3:
			att2 = 0.5

	elif int(img) == 32:
		Plant = ':zap: Electro'
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att3 = 250 + sum
			else:
				sum = int(rrr) * 10
				att3 = sum - 90
		if int(lista[5]) == 3:
			att3 = 1000

	elif int(img) == 8:
		Plant = ':zap: Electro'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/8_{rr}.png"
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 80 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 145
		if int(lista[5]) == 3:
			att1 = 400

	elif int(img) == 3:
		Plant = ':zap: Electro'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/3_{rr}.png"
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 80 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 145
		if int(lista[5]) == 3:
			att1 = 400

	elif int(img) == 15:
		Plant = ':zap: Electro'
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 380 + sum
			else:
				sum = int(rrr) * 5
				att3 = 155 + sum
		if int(lista[5]) == 3:
			att3 = 700

	elif int(img) == 29:
		Plant = ':snowflake: Ice'
		if int(lista[5]) == 1:
			att3 = 150 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 100 + sum
			else:
				sum = int(rrr) * 5
				att3 = sum - 145
		if int(lista[5]) == 3:
			att3 = 400

	elif int(img) == 2:
		Plant = ':snowflake: Ice'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/2_{rr}.png"
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att3 = 250 + sum
			else:
				sum = int(rrr) * 10
				att3 = sum - 90
		if int(lista[5]) == 3:
			att3 = 1000

	elif int(img) == 6:
		Plant = ':snowflake: Ice'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/6_{rr}.png"
		if int(lista[5]) == 1:
			att3 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 150 + sum
			else:
				sum = int(rrr) * 5
				att3 = 55 + sum
		if int(lista[5]) == 3:
			att3 = 600

	elif int(img) == 92:
		Plant = ':snowflake: Ice'
		atk = 150
		defet = 400
		if int(lista[5]) == 1:
			sum = int(rrr) * 50
			hitp = 10000 + sum
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 100
				hitp = 7500 + sum
			else:
				sum = int(rrr) * 500
				hitp = sum - 27000
		if int(lista[5]) == 3:
			hitp = 25000

	elif int(img) == 24:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			iii = int(rrr) / 1000
			pppp = 0.200 + iii
			att2 = float(pppp)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				iii = int(rrr) / 1000
				bbb = iii * 2
				pppp = 0.180 + bbb
				att2 = float(pppp)
			else:
				iii = int(rrr) / 1000
				bbb = iii * 5
				pppp = bbb - 0.045
				att2 = float(pppp)
		if int(lista[5]) == 3:
			att2 = 0.5

	elif int(img) == 23:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 55 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 195
		if int(lista[5]) == 3:
			att1 = 350

	elif int(img) == 22:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 5
				att3 = 250 + sum
			else:
				sum = int(rrr) * 10
				att3 = sum - 90
		if int(lista[5]) == 3:
			att3 = 1000

	elif int(img) == 12:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 55 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 195
		if int(lista[5]) == 3:
			att1 = 400

	elif int(img) == 13:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 55 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 195
		if int(lista[5]) == 3:
			att1 = 350

	elif int(img) == 11:
		Plant = ':fleur_de_lis: Parasite'
		if int(lista[5]) == 1:
			att3 = 200 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 180 + sum
			else:
				sum = int(rrr) * 5
				att3 = sum - 70
		if int(lista[5]) == 3:
			att3 = 500

	elif int(img) == 25:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 380 + sum
			else:
				sum = int(rrr) * 5
				att3 = 155 + sum
		if int(lista[5]) == 3:
			att3 = 700

	elif int(img) == 26:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			att3 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 280 + sum
			else:
				sum = int(rrr) * 5
				att3 = 55 + sum
		if int(lista[5]) == 3:
			att3 = 600
		
	elif int(img) == 27:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			att1 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 280 + sum
			else:
				sum = int(rrr) * 5
				att1 = 55 + sum
		if int(lista[5]) == 3:
			att1 = 650
		
	elif int(img) == 28:
		Plant = ':gear: Metal'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 55 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 195
		if int(lista[5]) == 3:
			att1 = 400
		
	elif int(img) == 4:
		Plant = ':droplet: Water'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/4_{rr}.png"
		if int(lista[5]) == 1:
			iii = int(rrr) / 1000
			pppp = 0.200 + iii
			att2 = float(pppp)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				iii = int(rrr) / 1000
				bbb = iii * 2
				pppp = 0.180 + bbb
				att2 = float(pppp)
			else:
				iii = int(rrr) / 1000
				bbb = iii * 5
				pppp = bbb - 0.045
				att2 = float(pppp)
		if int(lista[5]) == 3:
			att2 = 0.5
		
	elif int(img) == 5:
		Plant = ':droplet: Water'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/5_{rr}.png"
		if int(lista[5]) == 1:
			att3 = 400 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 380 + sum
			else:
				sum = int(rrr) * 5
				att3 = 155 + sum
		if int(lista[5]) == 3:
			att3 = 700
		
	elif int(img) == 36:
		Plant = ':droplet: Water'

		
	elif int(img) == 38:
		Plant = ':droplet: Water'
		if int(lista[5]) == 1:
			att1 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 80 + sum
			else:
				sum = int(rrr) * 5
				att1 = sum - 145
		if int(lista[5]) == 3:
			att1 = 400
		
	elif int(img) == 39:
		Plant = ':droplet: Water'
		if int(lista[5]) == 1:
			att3 = 100 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 80 + sum
			else:
				sum = int(rrr) * 5
				att3 = sum - 145
		if int(lista[5]) == 3:
			att3 = 400
		
	elif int(img) == 37:
		Plant = ':butterfly: Wind'
		if int(lista[5]) == 1:
			att1 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 280 + sum
			else:
				sum = int(rrr) * 5
				att1 = 55 + sum
		if int(lista[5]) == 3:
			att1 = 650
		
	elif int(img) == 16:
		Plant = ':butterfly: Wind'
		if int(lista[5]) == 1:
			att3 = 300 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 280 + sum
			else:
				sum = int(rrr) * 5
				att3 = 55 + sum
		if int(lista[5]) == 3:
			att3 = 600
		
	elif int(img) == 10:
		Plant = ':butterfly: Wind'
		if int(lista[5]) == 1:
			att1 = 350 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att1 = 330 + sum
			else:
				sum = int(rrr) * 5
				att1 = 75 + sum
		if int(lista[5]) == 3:
			att1 = 600
		
	elif int(img) == 9:
		Plant = ':butterfly: Wind'
		hh = f"https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/9_{rr}.png"
		if int(lista[5]) == 1:
			att3 = 150 + int(rrr)
		if int(lista[5]) == 2:
			if int(rrr) <= 88:
				sum = int(rrr) * 2
				att3 = 100 + sum
			else:
				sum = int(rrr) * 5
				att3 = sum - 145
		if int(lista[5]) == 3:
			att3 = 400

	if int(lista[0]) == 1:
		vrg = (f"Physic :yellow_square: {att1} \n Loss... :red_square: {round(att2,3)} \n Magic :blue_square: {att3} \n Pure... :green_square: {att4}")
	else:
		vrg = (f"ATK :yellow_square: {atk} \n DEF :shield: {defet} \n HP :heart: {hitp}")

	embed = discord.Embed(title="Type", description=f"{Base}", color=discord.Colour.dark_red())
	embed.set_thumbnail(url=f"{hh}")
	embed.add_field(name="Element", value=f"{Plant}")
	embed.add_field(name="Rarity", value=f"{rareza}")
	embed.add_field(name="Stats", value=f"{vrg}",  inline=False)
	embed.set_footer(text="Created by @AlexanderJGA#0399")
	await ctx.send(embed=embed)

@bot.command()
async def clm(ctx, *, pp):
	HHH = pp.split("-")
	posi = 0
	nega = 0
	neut = 0
	if HHH[1] == "Dark":
		ihi = "	https://pvuextratools.com/assets/images/Dark.png"
	if HHH[1] == "Electro":
		ihi = "	https://pvuextratools.com/assets/images/Electro.png"
	if HHH[1] == "Fire":
		ihi = "	https://pvuextratools.com/assets/images/Fire.png"
	if HHH[1] == "Ice":
		ihi = "	https://pvuextratools.com/assets/images/Ice.png"
	if HHH[1] == "Light":
		ihi = "	https://pvuextratools.com/assets/images/Light.png"
	if HHH[1] == "Parasite":
		ihi = "	https://pvuextratools.com/assets/images/Parasite.png"
	if HHH[1] == "Metal":
		ihi = "	https://pvuextratools.com/assets/images/Metal.png"
	if HHH[1] == "Water":
		ihi = "	https://pvuextratools.com/assets/images/Water.png"
	if HHH[1] == "Wind":
		ihi = "	https://pvuextratools.com/assets/images/Wind.png"

	if HHH[0] == "Spring":
		cll = ":sunrise_over_mountains: Spring"
		if HHH[1] == "Dark":
			element = "Dark :spades:"
			posi = 20
			nega = 0
			neut = 80
			maxp = 40
			maxn = 0
		if HHH[1] == "Electro":
			element = 'Electro :zap:'
			posi = 10
			nega = 0
			neut = 90
			maxp = 50
			maxn = 0
		if HHH[1] == "Fire":
			element = 'Fire :fire:'
			posi = 20
			nega = 30
			neut = 50
			maxp = 100
			maxn = 40
		if HHH[1] == "Ice":
			element = 'Ice :snowflake:'
			posi = 20
			nega = 10
			neut = 70
			maxp = 40
			maxn = 40
		if HHH[1] == "Light":
			element = 'Light :sunny:'
			posi = 0
			nega = 30
			neut = 70
			maxp = 0
			maxn = 20
		if HHH[1] == "Parasite":
			element = 'Parasite :fleur_de_lis:'
			posi = 30
			nega = 0
			neut = 70
			maxp = 100
			maxn = 0
		if HHH[1] == "Metal":
			element = 'Metal :gear:'
			posi = 30
			nega = 20
			neut = 50
			maxp = 120
			maxn = 60
		if HHH[1] == "Water":
			element = 'Water :droplet:'
			posi = 40
			nega = 20
			neut = 40
			maxp = 100
			maxn = 30
		if HHH[1] == "Wind":
			element = 'Wind :butterfly:'
			posi = 20
			nega = 10
			neut = 70
			maxp = 50
			maxn = 50

	if HHH[0] == "Summer":
		cll = ":city_sunrise: Summer"
		if HHH[1] == "Dark":
			element = "Dark :spades:"
			posi = 31.25
			nega = 0
			neut = 68.75
			maxp = 100
			maxn = 0
		if HHH[1] == "Electro":
			element = 'Electro :zap:'
			posi = 18.75
			nega = 0
			neut = 81.25
			maxp = 100
			maxn = 0
		if HHH[1] == "Fire":
			element = 'Fire :fire:'
			posi = 37.5
			nega = 18.75
			neut = 43.75
			maxp = 100
			maxn = 40
		if HHH[1] == "Ice":
			element = 'Ice :snowflake:'
			posi = 12.5
			nega = 12.5
			neut = 75
			maxp = 40
			maxn = 60
		if HHH[1] == "Light":
			element = 'Light :sunny:'
			posi = 31.25
			nega = 31.25
			neut = 37.5
			maxp = 200
			maxn = 40
		if HHH[1] == "Parasite":
			element = 'Parasite :fleur_de_lis:'
			posi = 18.75
			nega = 0
			neut = 81.25
			maxp = 100
			maxn = 0
		if HHH[1] == "Metal":
			element = 'Metal :gear:'
			posi = 12.5
			nega = 18.75
			neut = 68.75
			maxp = 100
			maxn = 60
		if HHH[1] == "Water":
			element = 'Water :droplet:'
			posi = 31.25
			nega = 18.75
			neut = 50
			maxp = 100
			maxn = 30
		if HHH[1] == "Wind":
			element = 'Wind :butterfly:'
			posi = 18.75
			nega = 6.25
			neut = 75
			maxp = 100
			maxn = 50

	if HHH[0] == "Autumn":
		cll = ":fallen_leaf: Autumn"
		if HHH[1] == "Dark":
			element = "Dark :spades:"
			posi = 31.25
			nega = 0
			neut = 68.75
			maxp = 400
			maxn = 0
		if HHH[1] == "Electro":
			element = 'Electro :zap:'
			posi = 25
			nega = 0
			neut = 75
			maxp = 100
			maxn = 0
		if HHH[1] == "Fire":
			element = 'Fire :fire:'
			posi = 12.5
			nega = 25
			neut = 62.5
			maxp = 100
			maxn = 40
		if HHH[1] == "Ice":
			element = 'Ice :snowflake:'
			posi = 18.75
			nega = 6.25
			neut = 75
			maxp = 60
			maxn = 40
		if HHH[1] == "Light":
			element = 'Light :sunny:'
			posi = 37.5
			nega = 6.25
			neut = 43.75
			maxp = 20
			maxn = 40
		if HHH[1] == "Parasite":
			element = 'Parasite :fleur_de_lis:'
			posi = 18.75
			nega = 0
			neut = 81.25
			maxp = 100
			maxn = 0
		if HHH[1] == "Metal":
			element = 'Metal :gear:'
			posi = 25
			nega = 18.75
			neut = 56.25
			maxp = 120
			maxn = 100
		if HHH[1] == "Water":
			element = 'Water :droplet:'
			posi = 43.75
			nega = 12.5
			neut = 43.75
			maxp = 100
			maxn = 30
		if HHH[1] == "Wind":
			element = 'Wind :butterfly:'
			posi = 31.25
			nega = 6.25
			neut = 62.5
			maxp = 100
			maxn = 50

	if HHH[0] == "Winter":
		cll = ":snowman: Winter"
		if HHH[1] == "Dark":
			element = "Dark :spades:"
			posi = 0
			nega = 0
			neut = 100
			maxp = 0
			maxn = 0
		if HHH[1] == "Electro":
			element = 'Electro :zap:'
			posi = 22.22
			nega = 0
			neut = 77.78
			maxp = 50
			maxn = 0
		if HHH[1] == "Fire":
			element = 'Fire :fire:'
			posi = 44.44
			nega = 33.33
			neut = 22.23
			maxp = 100
			maxn = 60
		if HHH[1] == "Ice":
			element = 'Ice :snowflake:'
			posi = 33.33
			nega = 11.11
			neut = 55.56
			maxp = 120
			maxn = 40
		if HHH[1] == "Light":
			element = 'Light :sunny:'
			posi = 44.44
			nega = 11.11
			neut = 44.45
			maxp = 100
			maxn = 20
		if HHH[1] == "Parasite":
			element = 'Parasite :fleur_de_lis:'
			posi = 0
			nega = 0
			neut = 0
			maxp = 0
			maxn = 0
		if HHH[1] == "Metal":
			element = 'Metal :gear:'
			posi = 33.33
			nega = 0
			neut = 66.67
			maxp = 100
			maxn = 0
		if HHH[1] == "Water":
			element = 'Water :droplet:'
			posi = 11.11
			nega = 11.11
			neut = 77.78
			maxp = 60
			maxn = 20
		if HHH[1] == "Wind":
			element = 'Wind :butterfly:'
			posi = 33.33
			nega = 0
			neut = 66.67
			maxp = 50
			maxn = 0

	if nega >= posi:
		www = "Use A GreenHouse :white_check_mark:"
	else:
		www = "Do Not Use A GreenHouse :x:"

	embed = discord.Embed(title=f"{cll}", description=f"Type: {element}", color=discord.Colour.dark_blue())
	embed.set_thumbnail(url=f"{ihi}")
	embed.add_field(name="Probability", value=f":grinning: {posi}% |:sweat: -{nega}% |:neutral_face: {neut}%")
	embed.add_field(name="Maximum impacts", value=f":green_circle: {maxp}% |:red_circle: -{maxn}%", inline=False)
	embed.add_field(name="Recomendation", value=f"{www}", inline=False)
	embed.set_footer(text="Created by @AlexanderJGA#0399")
	await ctx.send(embed=embed)

@bot.command()
async def Ssunbox(ctx):
	pol = random.randrange(10001)
	diviv = pol / 100
	imggg = "https://marketplace.plantvsundead.com/_nuxt/img/wish-list-1.ba5c877.png"
	print(diviv)
	if diviv <= 30.00:
		premio = "100 x Water :droplet: \n 20 x Scarecrows :farmer:"
		imggg = "https://marketplace.plantvsundead.com/_nuxt/img/gift-water-100.d9e8d74.png"
		qqqqq = ":neutral_face: 30"
	elif diviv <= 60.00:
		premio = "2 x Small spots :bucket:"
		qqqqq = ":neutral_face: 30"
		imggg = "https://marketplace.plantvsundead.com/_nuxt/img/small%20pot@3x.ff8750b.png"
	elif diviv <= 90.00:
		premio = "1 x Sunflower sapling :potted_plant:"
		qqqqq = ":neutral_face: 30"
	elif diviv <= 99.90:
		premio = "1 x Sunflower mama :sunflower:"
		qqqqq = ":open_mouth: 9.9"
	elif diviv >= 100.00:
		premio = "1 x Seed :seedling:"
		qqqqq = ":partying_face: 0.1"

	embed = discord.Embed(title=":gift: Sunbox :gift:", description=f"{premio}", color=discord.Colour.dark_purple())
	embed.set_thumbnail(url=f"{imggg}")
	embed.add_field(name="Probability", value=f"{qqqqq}%")
	embed.set_footer(text="Created by @AlexanderJGA#0399")
	await ctx.send(embed=embed)

@bot.command()
async def price(ctx):
	url = requests.get("https://coinmarketcap.com/currencies/plantvsundead/")
	soup = BeautifulSoup(url.content, "html.parser")
	resultadoo = soup.find("div", {"class":"priceValue"})
	preciop = resultadoo.text

	embed = discord.Embed(title=":bar_chart: Price", description=f":four_leaf_clover: PVU = {preciop}", color=discord.Colour.gold())
	embed.set_thumbnail(url="https://i.imgur.com/G2LpD8E.png")
	embed.set_footer(text="Created by @AlexanderJGA#0399")
	await ctx.send(embed=embed)

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online ,activity=discord.Activity(type=discord.ActivityType.watching, name="BotPVU | >help"))
	print("		/ /	/ /	    \n	   ________	 	\n	   |      |\	\n	   | Alex | |	\n	   | 	  |/	\n	   \______/   	")

bot.run(TOKEN)
