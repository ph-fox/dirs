import requests, threading, time, random, optparse, sys, random
from colorama import Fore, Style

parser = optparse.OptionParser()
parser.add_option('-u','--url',dest='url',help='target url')
parser.add_option('-w','--wordlist',dest='wordlist',help='wordlist path')
(value, key) = parser.parse_args()
url = value.url
wordlist = value.wordlist

if url is None:
	print("""
usage : python3 dir3.py -u <url> -w <wordlist>
	-u : Target url
	-w : wordlist path""")

elif wordlist is None:
	wordlist = '/usr/share/wordlists/dirb/common.txt'

class dirsearch:
	def __init__(self, url, wlist):
		self.url = url
		self.wlist = wordlist

	def dirs(self):
		wordlists = open(self.wlist).read().splitlines()
		for word in wordlists:
			site = f'{self.url}/{word}'
			r = requests.get(site)
			code = r.status_code
			spacer = random.choices(' ',k=len(site))
			sys.stdout.write(f"\r{''.join(spacer)}            ")
			sys.stdout.write(f'\r{Style.BRIGHT}{Fore.YELLOW}{site}')

			if code == 404:
				pass
			elif code == 501:
				pass
			else:
				if code == 200:
					print(f'\r{Fore.CYAN}[{Fore.GREEN}{code}{Fore.CYAN}]{Fore.YELLOW} {site}')
				else:
					print(f'\r{Fore.CYAN}[{Fore.RED}{code}{Fore.CYAN}]{Fore.YELLOW} {site}')


if __name__=='__main__':

	start = dirsearch(url, wordlist)
	try:
		start.dirs()
	except:
		pass
