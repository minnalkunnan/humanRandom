import socket
import re
import requests
import urllib
import json
import pprint
import time
from multiprocessing import Pool


def getMessages(channel):
	HOST = "irc.twitch.tv"
	PORT = 6667
	NICK = "minnalgg" #The account Name
	PASS = "oauth:gy8eqh97aujkgae5ou3zda1mjlj59g" #http://www.twitchapps.com/tmi/
	CHAN = '#' + channel
	s = socket.socket()

	s.connect((HOST, PORT))

	s.send("PASS {}\r\n".format(PASS))

	s.send("NICK {}\r\n".format(NICK))

	s.send("JOIN {}\r\n".format(CHAN))

	gathers = 0
	result = ''
	resp = s.recv(1024)
	resp = s.recv(1024)
	resp = s.recv(1024)
	while True:
		resp = s.recv(1024)
		message = resp.split(CHAN + " :", 1)
		if len(message) > 1:
			result += message[1].strip()
			print(message[1].strip())
			gathers += 1
			print(gathers)
	    #print(resp)
	    #if resp == "PING :tmi.twitch.tv\r\n":
	    #    s.send("PONG :tmi.twitch.tv\r\n")
	    #if resp.find("hi")!=-1:
	    #    s.send("PRIVMSG "+CHAN+" :HELLO\r\n")
		resp = ""
		if gathers > 400:
			break;

	return result

def getChannels():
	clientid = 'a2zmbka2e087rgmw26ctch8ro6xofq'
	oauth = 'oauth:gy8eqh97aujkgae5ou3zda1mjlj59g'
	headers = {'Authorization':oauth, 'Client-ID':clientid}
	r = requests.get("https://api.twitch.tv/kraken/streams/featured", headers=headers)

	data = r.json()

	numStreams = len(data.get('featured'))

	i = 0
	streamNames = []
	while i < numStreams:
		streamNames.append(str(data['featured'][i]['stream']['channel']['name']))
		i += 1

	print(streamNames)
	return streamNames

streamNames = getChannels()

answer = getMessages('summit1g')
print(answer)
'''
pool = Pool()
result1 = pool.apply_async(getMessages, ['summit1g'])
result2 = pool.apply_async(getMessages, [streamNames[1]])
result3 = pool.apply_async(getMessages, [streamNames[2]])
answer1 = result1.get(timeout=60)
answer2 = result2.get(timeout=60)
answer3 = result3.get(timeout=60)
print("First string " + answer1)
print("Second string " + answer2)
print("Third string " + answer3)
'''

