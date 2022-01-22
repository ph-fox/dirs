import requests, optparse, sys, os, threading
from colorama import Fore, Style
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
parser = optparse.OptionParser()
parser.add_option('-u','--url',dest='url',help='target url')
parser.add_option('-w','--wordlist',dest='wordlist',help='wordlist path')
(value, key) = parser.parse_args()
url = value.url
wordlist = value.wordlist

class Dirsearch:
	def __init__(self, url, wlist):
		self.url = url
		self.wlist = wordlist
		self.word= None

	def banner(self):
		print("""
|=====================================|
| D҈1尺乇匚ㄒㄖ尺ㄚ 丂乇卂尺匚卄乇尺   |
|-------------------------------------|
|By: Anikin Luke | ǝʞnl uᴉʞᴉuɐ         |
|                                     |
|This Tool Is From:                   |
| └─https://github.com/abalesluke     |
|                                     |
|=====================================|""")

	def brute(self):
		site = f'{self.url}/{self.word}'
		try:
			r = requests.get(site, verify=False)
			code = r.status_code
			spacer = ' '*len(site)
			sys.stdout.write(f"\r{spacer}            ")
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
		except KeyboardInterrupt:
			print('\nkeyboard KeyboardInterrupt')
			exit(0)
		except:
			pass


	def dirs(self):
		ds.banner()
		wordlists = open(self.wlist, encoding="ISO-8859-1").read().splitlines()
		for word in wordlists:			
			self.word = word
			threading.Thread(target=ds.brute).start()

	def check(self):
		if self.wlist is None:
			self.wlist = '/usr/share/wordlists/dirb/common.txt'
		if self.url is None:
			ds.banner()
			os.system(f'python3 {os.path.basename(__file__)} -h')
			exit(0)
		ds.dirs()


if __name__=='__main__':
	ds = Dirsearch(url, wordlist)
	ds.check()
