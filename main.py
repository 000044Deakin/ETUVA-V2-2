#imports
import random
import sys
from calculator import *
from dessert_game import *
from crosses import *
from code import *
from word import *
from tetris import *
from readchar import readchar
from colorama import Fore
import replit, time
# entry program

while True:
	print (Fore.GREEN + "Welcome to the ETUDA V2, i have added a program so that you now can press a key and have a program exacuted.")
	print(Fore.RED + "[ Select Function ]" + Fore.BLUE + "\n\n[1] Test Key Detection" + Fore.GREEN + "\n[2] Exit - End all\n" + Fore.BLUE + "[3] calculator")
	print (Fore.GREEN + "[4] norts and crosses")
	print (Fore.BLUE + "[5] Dessert Game")
	print (Fore.GREEN + "[6] notation")
	print (Fore.BLUE + "[7]tetris")
  #Step 2 - Naming your variable
  #I named my variable 'r.c' - meaning 'readchar'
	rc = readchar()

  #Step 3 - Input detection and output options
	if rc == '1':
		replit.clear()
		print(Fore.BLUE + "Hello, World!\n")
		time.sleep(1)
		replit.clear()
	elif rc == '2':
		replit.clear()
		sys.exit()
	elif rc == '3' :
		replit.clear()
		calculator()
		time.sleep(5)
		replit.clear()
	elif rc == '4':
		replit.clear()
		crosses()
		replit.clear()
	elif rc == '5':
		replit.clear()
		dessert()
		replit.clear()
	elif rc == '6':
		replit.clear()
		word()
		replit.clear()
	elif rc == '7':
		replit.clear()
		import signal
		import sys

		from board import BoardDrawer
		from game import Game


		def main():
		    Game().run()

		def signal_handler(_signal, _frame):
		    sys.exit(0)
		signal.signal(signal.SIGINT, signal_handler)

		if __name__ == '__main__':
		    main()
		replit.clear()
	else:
		print(Fore.LIGHTRED_EX + "Invalid input.\n")
		time.sleep(1)
		replit.clear()