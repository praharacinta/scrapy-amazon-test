# remember to install the library: pip install scraperapi-sdk
import requests
YOURAPIKEY="fb4b79cd6c1ccc2be55fdc3723f5b4a1"
payload = {'api_key': YOURAPIKEY, 'url':
'https://httpbin.org/ip'}

r = requests.get('http://api.scraperapi.com', params=payload)

print(r.text)