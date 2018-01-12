#!/usr/bin/python 2.7

import SimpleHTTPServer
import SocketServer
import time
import os

from blessings import Terminal

t = Terminal()

def quickshell():
	cwd = os.system('pwd')
	print "[" + t.green("+") + "]OS Shell in " + cwd 
	print "[" + t.green("+") + "]Enter 'Q' to quit"
	
	try:
		
		while True:
			command = raw_input("\n<" + t.cyan("SERVER") + ">$ ")
			if not command in ('q', 'Q'):
				os.system(command)
			else:
				print "\n[" + t.red("!") + "]Exiting shell."
				time.sleep(1.5)
				break
	
	except KeyboardInterrupt:
		print "\n[" + t.red("!") + "]Critical. User Aborted"

print "\n[" + t.green("+") + "]Basic HTTP Server.\n"

default = raw_input("[" + t.magenta("?") + "]Default Config? [Y]es/[N]o: ")
if default == 'y' or 'Y':
	
	PORT = 8000
	IP = "127.0.0.1"
	print "\n[" + t.green("+") + "]Default settings loaded.\n"
	
elif default == 'n' or 'N':
	
	print "[" + t.green("+") + "]Specify custom values.\n"
	PORT = raw_input(int("[" + t.magenta("?") + "]Enter port: ")) 
	IP = raw_input("[" + t.magenta("?") + "]Enter host: ")
	
	print "[" + t.green("+") + "]Invoke a shell to make adjustments in server directory?"
	invoke = raw_input("[" + t.magenta("?") + "][Y]es/[N]o: ")
	if invoke == 'y' or 'Y':
		quickshell()
	elif invoke == 'n' or 'N':
		print "[" + t.green("+") + "]Done."
	else:
		print "\n[" + t.red("!") + "]Unhandled Option."
		
else:
	print "\n[" + t.red("!") + "]Unhandled Option."


print "[" + t.green("+") + "]Starting Server.\n"

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

try:
	httpd = SocketServer.TCPServer((IP, PORT), Handler)
except Exception as e:
	print "\n[" + t.red("!") + "]Critical. An exception was raised with the following error message"
	print e

print "[" + t.green("+") + "]Serving at", IP, repr(PORT)

# Catching keyboard interrupt for aesthetics purposes
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	print "\n[" + t.red("!") + "]User Aborted."
