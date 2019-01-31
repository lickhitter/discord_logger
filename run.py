from config.emoji_unicodefix import *
#import above is a fix i found so emojis dont make it crash^^
from config.config import *
import os
import shutil
import sys
import discord
import datetime
import requests

client = discord.Client()
@client.event
async def on_ready():
	print("Ready, logged messages: ")

#Check if a the given directory exists, if not create it
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#messy ass code soz in advance
@client.event
async def on_message(message):
	image = "/image"
	now = datetime.datetime.now()
	now = now.strftime("%m-%d-%y %H;%M;%S")
	m = str(message.content)
	a = str(message.author)
	for att in message.attachments:
		attachment = att.get("url").lower()
		filename = attachment.split('/')[-1]
		if message.channel.is_private:
			if filename.find(".png") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".png", 'wb').write(r.content)
			if filename.find(".jpg") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".jpg", 'wb').write(r.content)
			if filename.find(".gif") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".gif", 'wb').write(r.content)
			if filename.find(".mp4") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".mp4", 'wb').write(r.content)
			if filename.find(".mov") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".mov", 'wb').write(r.content)
			if filename.find(".webm") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".webm", 'wb').write(r.content)
			if filename.find(".txt") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open('./PMS/image/'+a+" - "+now+".txt", 'wb').write(r.content)
		else: 
			s = message.server.name
			if filename.find(".png") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".png", 'wb').write(r.content)
			if filename.find(".jpg") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".jpg", 'wb').write(r.content)
			if filename.find(".gif") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".gif", 'wb').write(r.content)
			elif filename.find(".mp4") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".mp4", 'wb').write(r.content)
			elif filename.find(".mov") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".mov", 'wb').write(r.content)
			elif filename.find(".webm") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".webm", 'wb').write(r.content)
			elif filename.find(".txt") != -1:
				r = requests.get(attachment, allow_redirects=True)
				open(s +'/image/'+a+" - "+now+".txt", 'wb').write(r.content)
	#check if message has an attachment, if it does save it and print the url
	if message.attachments:
		#pms
		if message.channel.is_private:
			#create folders
			createFolder("PMS")
			createFolder("PMS"+image)
			#print logged message & attachment URL.
			maintsr = now+ "(PM) " + str(a) + ': ' + str(m) + " " + att.get("url")
			print(maintsr)
			#write logged message & attachemnt URL to file
			writepath = "PMS/pms.txt"
			mode = 'a' if os.path.exists(writepath) else 'w'
			aaa = open(writepath, mode, encoding='utf-8')
			aaa.write(maintsr +'\n')
			aaa.close()
		#servers
		else:
			s = str(message.server.name)
			c = str(message.channel.name)
			#create folders
			createFolder(s)
			createFolder(s+image)
			e = ".txt"
			#print logged message & attachment URL.
			maintsr = "["+now+"] "+"(" + message.server.name +"/" +message.channel.name +") " + str(a) + ': ' + str(m) + " " + att.get("url")
			print(maintsr)
			#write logged message & attachemnt URL to file
			writepath = s + "/" + s + e 
			mode = 'a' if os.path.exists(writepath) else 'w'
			text_file = open(writepath, mode, encoding='utf-8')
			text_file.write(maintsr +'\n')
			text_file.close()
	#no attachments:
	else: 
		#pms
		if message.channel.is_private:
			#print logged message
			maintsr = "["+now+"] "+"(PM) " + str(a) + ': ' + str(m)
			print(maintsr)
			#create folders
			createFolder("PMS")
			createFolder("PMS"+image)
			#write logged messages to file
			writepath = "PMS/pms.txt"
			mode = 'a' if os.path.exists(writepath) else 'w'
			aaa = open(writepath, mode, encoding='utf-8')
			aaa.write(maintsr +'\n')
			aaa.close()
		#servers
		else:
			s = message.server.name
			c = message.channel.name
			f = s
			#create folders
			createFolder(s)
			createFolder(s+image)
			#print logged message
			maintsr = "["+now+"] "+"(" + message.server.name +"/" +message.channel.name +") " + str(a) + ': ' + str(m)
			print(maintsr)
			#write logged messages to file
			e = ".txt"
			writepath = f + "/" + s + e 
			mode = 'a' if os.path.exists(writepath) else 'w'
			text_file = open(writepath, mode, encoding='utf-8')
			text_file.write(maintsr +'\n')
			text_file.close()
			
			
client.run(token, bot=False)
