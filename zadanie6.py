import requests

url = 'http://localhost:8098/buckets/s14015/keys/warszawa'

status1 = { 
	'rok': 2000
	'iloscMieszkancow': 1672000
	}
	
status2 = { 'rok': 2020
	'iloscMieszkancow': 1794166
}


r1 = requests.put(url, json=status1)
print(requests.get('http://localhost:8098/buckets/s14015/keys/warszawa').text)

r2 = request.post(url, json=status2)
print(requests.get('http://localhost:8098/buckets/s14015/keys/warszawa').text)

r3 = request.delete(url)
print(requests.get('nic nie ma')
