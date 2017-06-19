import re

def valida(s):
    pattern = "\@\.|045|\_\.\_|asdasd|\|\?"
    return not bool(re.search(pattern, s))

with open("ayudantia texto sucio", "r") as file:
    palabras = re.split("\$", file.readline())

validas = []

for palabra in palabras:
    if valida(palabra):
        #print(palabra)
        validas.append(palabra)
        
with open("ayudantia texto limpio", "w") as file:
    file.write(" ".join(validas))
