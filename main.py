import discord
import time
from math import *
import os

def recupdermessage():
	token = input('entre le token')
	client = discord.Client()
	@client.event
	async def on_ready():
		print(f'{client.user} has connected to Discord!')
		mes=open('message.txt','+w')
		channel = client.get_channel(912495325997064193)
		message = await channel.fetch_message(channel.last_message_id)
		nomUtilisateur = await channel.fetch_message(channel.last_message_id)
		mes.write(message.content)
		user = await client.fetch_user(711967096820465777)
		await client.close()
		time.sleep(1)
	client.run(token)
	mes=open('message.txt','+r')
	
	return mes.read()



def reconaissance():
    pass

def createChanel():
    pass
recupdermessage()