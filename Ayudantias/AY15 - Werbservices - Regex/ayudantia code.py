import requests

#r = requests.post('http://httpbin.org/post', data = {'key':'value'})
#data = r.content

r = requests.get('https://api.github.com/events')
data = r.json()
for i in data:
    for k, v in i.items():
        print(k,v)

