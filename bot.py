from irc import *
import os
import random
server = "SERVER-IP/HOSTNAME"
port = 6667
channel = "SERVER-CHANNEL"
botnick = "NICKAME-FOR-BOT"
botnickpass = "guido"
botpass = "<%= @guido_password %>"
if channel.startswith("#") == False:
	channel = "#"+channel
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)
while True:
    text = irc.get_response()
    if "PRIVMSG" in text and channel in text and "--hello" in text.lower():
        irc.send(channel, "Greetings dumbass")
    if "PRIVMSG" in text and channel in text and "--ping" in text.lower():
        irc.send(channel, "Pong idiot")