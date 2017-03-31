from random import randint, choice
import os




#si los archivos estan en otra carpeta, ingresar el path como parametro de la funcion
def generate_connections(path = "./",file_names = ["airports"]):
	for name in file_names:

		#reviso si el archivo esta en la carpeta dada por path
		if not os.path.exists("{0}/{1}.csv".format(path, name)):
			raise  FileNotFoundError("El archivo debe estar en la misma carpeta!")

		with open("{0}/random_{1}.csv".format(path, name), "w") as file:
			file.write("{0},{1}\n".format("Pais 1", "Pais 2"))

		dict_countries = {}
		with open("{}.csv".format(name),"r") as file_in:
			#le quito el header
			file_in.readline()

			#sigo leyendo linea por linea
			#primero completamos el diccionario con los paises respectivos
			for line in file_in:
				line = line.strip().replace(",","").title()
				if not dict_countries.get(line):
					dict_countries[line] = set()

		#obtengo una lista ordenada de los paises
		all_countries = sorted(dict_countries, key = lambda llave: llave[0], reverse = False)



		######### ahora generamos el archivo ############

		total_countries = len(dict_countries)
		#le restamos uno, dado que no puedo llegar a mi
		total_countries -= 1

		for country in all_countries:
			random_number_generator = 0
			#para que sea mas "realista"
			for cycle in range(100):
				random_number_generator += randint(2,total_countries)
			random_number_generator //= 100


			#iteramos para llenar el set de cada pais
			while random_number_generator > 0:

				#elegimos un pais y evitamos que sea yo
				link_country = choice(all_countries)
				while link_country == country:
					link_country = choice(all_countries)

				#agregamos el pais al set de forma (pais_actual, pais_donde_puedo_llegar)
				dict_countries[country].add((country, link_country))
				random_number_generator -= 1

			#escribimos el archivo
			with open("random_{}.csv".format(name), "a") as file:
				for sets in dict_countries[country]:
					file.write(",".join(list(sets)) + "\n")
					


if __name__ == '__main__':
	generate_connections()