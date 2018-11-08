#!/usr/bin/python
import threading
import requests
import signal
import time
import sys
import netifaces as net
try:
	from getchats import apikey
except:
	pass
#made by r4j1337
args = sys.argv
if len(args) == 1:
	print("""\033[96m[+] \033[92mTry These Commands:

\033[96m[+] \033[92mhtb chat  {Starts a terminal chat client}
\033[96m[+] \033[92mhtb chat shout {See all messages like resets}
\033[96m[+] \033[92mhtb reset machine  {Resets A Machine}
\033[96m[+] \033[92mhtb machine/challenge pro/sucks {rates a machine or challenge}
\033[96m[+] \033[92mhtb sendmsg yourmessage {send a quick message to shoutbox}
\033[96m[+] \033[92mhtb respect user {respects a user}
\033[96m[+] \033[92mhtb startvpn {starts openvpn in background}
\033[96m[+] \033[92mhtb ip  {Shows your plain hackthebox ip}
	""")
	exit()

def signal_handler(sig, frame):
        print('Bye! :)')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

from os import system
if args[1] == "chat":
	system("clear")
	print("\033[96m[+] \033[92mTip: You Can Send Any Message Just Type On The Terminal :) \n")
	from getchats import *
	try:
		get_message()
	except:
		print("")
	try:
		arg2 = args[2]
	except Exception as e:
		arg2 = ""
	def background():
	        while True:
	            time.sleep(10)
	            if arg2 != "":
	            	get_last_message(quite=False)
	            else:
	            	get_last_message(quite=True)

	threading1 = threading.Thread(target=background)
	threading1.daemon = True
	threading1.start()

	help = '''
\033[92m[+]\033[97m \033[91mAvailable Commands:
\033[92m[+]\033[97m \033[91m/help \033[90m :: Returns this text
\033[92m[+]\033[97m \033[91m/respect \033[93m<username> \033[90m :: Gives respect to selected user.
\033[92m[+]\033[97m \033[91m/reset \033[93m<machine> \033[90m :: Resets the specified machine.
\033[92m[+]\033[97m \033[91m/cancel \033[93m<reset_id> \033[90m :: Cancels a pending reset.
\033[92m[+]\033[97m \033[91m/rate \033[93m<machine/challenge> \033[96m<pro/sucks> \033[90m :: Rates the machine accordingly.
\033[92m[+]\033[97m \033[91m/slap \033[93m<username> \033[90m :: Slaps the user.
\033[92m[+]\033[97m \033[91m/shame \033[93m<username> \033[90m :: Shames the user.
\033[92m[+]\033[97m \033[91m/beer \033[93m<username> \033[90m :: Offers a beer to user.
\033[92m[+]\033[97m \033[91m/milk \033[93m<username> \033[90m :: Offers a milk bottle to user.
\033[92m[+]\033[97m \033[91m/cocktail \033[93m<username> \033[90m :: Offers a cocktail to a stressed user.
\033[92m[+]\033[97m \033[91m/poke \033[93m<username> \033[90m :: Pokes a user.
\033[92m[+]\033[97m \033[91mAdmin-Only Commands:
\033[92m[+]\033[97m \033[91m/powerofthor \033[93m<username> \033[90m :: Bans resets/cancels/shouts of user for 5 minutes.\033[92m
	'''

	while True:
		try:
			mymessage = input("\033[92m")
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")
			if mymessage == "/help":
				print(help)
			elif mymessage == "":
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
			elif mymessage == "/quite":
				quite = False
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K")
			else:
				requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":mymessage})
		except Exception as e:

			system("clear")
			exit("Thank You")
elif args[1] == "reset":
	try:
		nameofbox = "/reset "+args[2]
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":nameofbox})
		cont = r.content
		if 'Invalid' in cont:
			print("[!] Machine does not exist.")
		elif 'will be reset' in cont:
			print("[+] reset requested successfully")
	except Exception as e:

		nameofbox = input("Name of box > ")
		nameofbox = "/respect "+nameofbox
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":nameofbox})
		cont = r.content
		if 'Invalid' in cont:
			print("[!] Machine does not exist.")
		elif 'will be reset' in cont:
			print("[+] reset requested successfully")
elif args[1] == "respect":
	try:
		nameofuser = "/respect "+args[2]
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":nameofuser})
		cont = r.content
		if 'invalid user' in cont:
			print("[!] User Not Found.")
		elif 'User respected' in cont:
			print("[+] User respected successfully")
	except Exception as e:

		nameofuser = input("Name of user > ")
		nameofuser = "/respect "+nameofuser
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":nameofuser})
		cont = r.content
		if 'invalid user' in cont:
			print("[!] User Not Found.")
		elif 'User respected' in cont:
			print("[+] User respected successfully")

elif args[1] == "rate":
	try:
		nameofbox = "/rate "+args[2] + " " + args[3]
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":nameofbox})
	except Exception as e:

		rt = input("rate pro/sucks > ")
		nameofbox = input("Name of box or challenge > ")
		nameofbox = "/rate "+ nameofbox + " " + rt
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":nameofbox})

elif args[1] == "sendmsg":
	try:
		msg = args[2]
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":msg})
		cont = r.content
		if 'success' in cont:
			print("Message Sent!")
		else:
			print("There was some problem")
	except Exception as e:

		msg = input('> ')
		r = requests.post("https://www.hackthebox.eu/api/shouts/new/?api_token="+apikey, data={"text":msg})
		cont = r.content
		if 'success' in cont:
			print("Message Sent!")
		else:
			print("There was some problem")
elif args[1] == "startvpn":
	cmd = "openvpn "+getcwd()+"/htb.ovpn"
	system(cmd)
elif args[1] == "ip":
	try:
  		net.ifaddresses('tun0')
  		ip = net.ifaddresses('tun0')[net.AF_INET][0]['addr']
  		print(ip)
	except Exception as e:

		print("\033[91m[+] Please connect first\033[91m")
