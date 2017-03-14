import socket
import re
import requests


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


getMessages("#beyondthesummit")