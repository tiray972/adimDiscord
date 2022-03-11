import discord
import time
from math import *
import os
import csv
chemin = "./myGitFile/projectPerso/adminDiscord/fichier_export.csv"
def recupdermessage():
	token = input('entre ton token :')
	client = discord.Client()
	@client.event
	async def on_ready():
		print(f'{client.user} has connected to Discord!')
		channel = client.get_channel(912495325997064193)
		mes=open('myGitFile/projectPerso/adminDiscord/message.txt','+w')
		message = await channel.fetch_message(channel.last_message_id)
		nomUtilisateur =  message.author
		idUtilisateur = nomUtilisateur.id
		
		with open(chemin, mode='a') as mon_fichier:
			mon_fichier_ecrire = csv.writer(mon_fichier, delimiter=',',
											quotechar='"',
											quoting=csv.QUOTE_MINIMAL)
			mon_fichier_ecrire.writerow([nomUtilisateur, idUtilisateur, message.content, 0])	
		
		
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