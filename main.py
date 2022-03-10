import discord
import time
from math import *
import os

def recupdermessage():
	token = 'OTEyNDg2ODc2NDEyMjc2Nzc3.YZwpoA.ih-tIjzWEQobgs54y6mjAaVj3J8'
	client = discord.Client()
	@client.event
	async def on_ready():
		print(f'{client.user} has connected to Discord!')
		mes=open('myGitFile/projectPerso/adminDiscord/message.txt','+w')
		channel = client.get_channel(912495325997064193)
		message = await channel.fetch_message(channel.last_message_id)
		nomUtilisateur =  message.author
		nomUtilisateur = nomUtilisateur.id
		mes.write(message.content+'\n')
		mes.write(str(nomUtilisateur))
		user = await client.fetch_user(711967096820465777)
		await client.close()
		time.sleep(1)
	client.run(token)
	mes=open('myGitFile/projectPerso/adminDiscord/message.txt','+r')
	
	return mes.read()



def reconaissance():
    pass

def createChanel():
    pass


recupdermessage()