import socket
import re
import requests
import threading
import urllib
import json
import pprint

def getMessages(channel):
	HOST = "irc.twitch.tv"
	PORT = 6667
	NICK = "minnalgg" #The account Name
	PASS = "oauth:gy8eqh97aujkgae5ou3zda1mjlj59g" #http://www.twitchapps.com/tmi/
	CHAN = channel

	s = socket.socket()

	s.connect((HOST, PORT))

	s.send("PASS {}\r\n".format(PASS))

	s.send("NICK {}\r\n".format(NICK))

	s.send("JOIN {}\r\n".format(CHAN))

	while True:
	    resp = s.recv(1024)
	    result = resp.split("beyondthesummit :", 1)
	    if(len(result) > 1):
	    	print result[1]
	    #print(resp)
	    #if resp == "PING :tmi.twitch.tv\r\n":
	    #    s.send("PONG :tmi.twitch.tv\r\n")
	    #if resp.find("hi")!=-1:
	    #    s.send("PRIVMSG "+CHAN+" :HELLO\r\n")
	    resp = ""

def getChannels():
	'''
	url = 'https://api.twitch.tv/kraken/streams/summary'
	req = urllib.request.Request(url)
	req.add_header("Client-ID","oauth:gy8eqh97aujkgae5ou3zda1mjlj59g")
	resp = urllib.request.urlopen(req)
	data = resp.read()
	'''
	#url = 'https://api.twitch.tv/kraken/'
	#r = requests.get(url)

	clientid = 'a2zmbka2e087rgmw26ctch8ro6xofq'
	oauth = 'oauth:gy8eqh97aujkgae5ou3zda1mjlj59g'
	headers = {'Authorization':oauth, 'Client-ID':clientid}
	r = requests.get("https://api.twitch.tv/kraken/streams/featured", headers=headers)

	print(r)
	#json =  r.json()
	#parsed = json.loads(json)
	#print json.dumps(parsed, indent=4, sort_keys=True)
	#print(json.get('featured'))
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(r.json())
	#print(r.json().values())
	
	
	#print(r.json().get('name'))



def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

getChannels()

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


