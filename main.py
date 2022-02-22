import requests


payload = {'company': 'Tesla'}
r = requests.get('https://www.sec.gov/cgi-bin/cik_lookup', params=payload)
print(r.url)
print(r.text)
