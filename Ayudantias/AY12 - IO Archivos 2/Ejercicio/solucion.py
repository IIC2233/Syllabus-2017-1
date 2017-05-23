with open('confidencial1.iic2233', 'rb') as file:
    datos1 = file.read()

with open('confidencial2.iic2233', 'rb') as file:
    datos2 = file.read()

signature = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

mitad1 = bytearray()
mitad2 = bytearray()

for num in datos1:
    mitad1 += bytes([(num - 2233) % 256])

n = 1
pos = 0
terminado = False
while not terminado:
    if pos + n > len(datos2):
        terminado = True
        n = len(datos2) - pos
    if n % 2 == 1:
        mitad2 += datos2[pos:pos+n]
        pos += n
    else:
        inv = bytearray(datos2[pos:pos + n])
        inv.reverse()
        mitad2 += inv
        pos += n
    n += 1

final = signature + mitad1 + mitad2

with open('confidencial.png', 'wb') as file:
    file.write(final)
