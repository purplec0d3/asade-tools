import os, sys, re
import requests
def banner():
	print("""

[*] AUTHOR : Purplec0d3 ~ Fleur De Bleau
		==== ASEDE ===
[1] Unfriend FB
[2] Mass CHECKER FB
[3] Spotify Account Checker
""")
def yok():
	karina = os.system('cd Facebook;python unf.py')
def yok2():
	moskov = os.system('cd FBChecker;python ceker.py')
def yok3():
	peler = os.system('cd Spotify;python spotify.py')

if __name__ == "__main__":
	os.system('clear')
	banner()
	r = input("Choose => ")
	if r == 1:
		yok()
	if r == 2:
		yok2()
	if r == 3:
		yok3()

