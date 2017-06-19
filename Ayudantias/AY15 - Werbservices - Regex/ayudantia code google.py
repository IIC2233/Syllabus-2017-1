from google import search

links = search('python', tld='cl', lang='es', stop=5)

for url in links:
    print(url)

urlretrieve2
