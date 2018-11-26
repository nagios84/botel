#!C:\Users\papa\AppData\Local\Programs\Python\Python37-32\python.exe
import requests
from clipboard import copy
import webbrowser

def get_url(short):
	URL = 'https://linkunshorten.com/api/link?url='
	r = requests.get(URL + short)
	resp = r.json()['redirectUrl']
	return resp


short = input('Enter short URL:> ')
addr = get_url(short)
copy(addr)
print('Your URL copied!')

opera = 'C:\\Program Files\\Opera\\launcher.exe'
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera))
webbrowser.get('opera').open_new_tab(addr)
