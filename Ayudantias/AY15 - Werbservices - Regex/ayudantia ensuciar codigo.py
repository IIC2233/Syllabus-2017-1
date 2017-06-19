import random

with open("ayudantia text","r") as file:
    palabras = [p.strip() for p in file.readline().split()]

palabras_sucias = []

for palabra in palabras:
    for i in range(random.randint(0,5)):
        p = random.choice(palabras)
        l = random.choice(range(len(p)))
        suciedad = random.choice(["@.", "045", "_._", "asdasd", "|?"])
        p = p[:l] + suciedad + p[l:]
        palabras_sucias.append(p)
    palabras_sucias.append(palabra)

with open("ayudantia texto sucio", "w") as file:
    for palabra in palabras_sucias:
        file.write(palabra)
        file.write("$")
