import requests, re, sys, time

def pat(url):
	pattern = r'http'
	if(re.match(pattern, url)):
		pass
	else:
		url = f'http://{url}'
		return(url)


def data():
	DIR = open('/usr/share/wordlists/dirb/common.txt', 'r')
	dirlist = DIR.read().splitlines()
	return dirlist

dirlist = data()

url = '192.168.0.1'
#url = input('[+] Enter url: ')
url = pat(url)
print("starting..")
print('[URL] ==================== [code]')
dirlist = data()
for wordlist in dirlist:
	site = url+'/'+wordlist
	r = requests.get(site)
	code = r.status_code
	sys.stdout.write('\r                                                      ')
	sys.stdout.write(f"\rError: {site}")
	sys.stdout.flush()
	time.sleep(.1)
	if(code == 200):
		print('\r'+site+'   ====>> 200')
	elif(code == 300):
		print('\r'+site+'  ====>> 300')
	elif(code == 401):
		print('\r'+site+'   ====>> 401')

sys.stdout.write('\r                                                      ')
print('Search Complete!')
