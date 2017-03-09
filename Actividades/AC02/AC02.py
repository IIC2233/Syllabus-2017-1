__author__ = "cotehidalgov"

#Herencia
# -*- coding: utf-8 -*-

import random

class Plate:
	def __init__(self, food, drink):
		self.food = food
		self.drink = drink

class Food:
	def __init__(self, ingredients):
		# RELLENAR
		pass

	def check_time(self): 
		# RELLENAR
		pass

class Drink:
	def __init__(self):
		# RELLENAR
		pass

class Personality:
	def react(plate):
		pass

class Person: # Solo los clientes tienen personalidad en esta actividad
	def __init__(self, name):
		self.name = name

class Restaurant:
	def __init__(self, chefs, clients):
		self.chefs = chefs
		self.clients = clients

	def start(self):
		for i in range(3): # Se hace el estudio por 3 dias
			print("----- Día {} -----".format(i + 1))
			plates = []
			for chef in self.chefs: 
				for j in range(3):  # Cada chef cocina 3 platos
					plates.append(chef.cook()) # Retorna platos de comida y bebida

			for client in self.clients:
				for plate in plates:
					client.eat(plate)



if __name__ == '__main__':
	chefs = [Chef("Cote"), Chef("Joaquin"), Chef("Andres")]
	clients = [Client("Bastian", Hater()), Client("Flori", Cool()), 
				Client("Antonio", Hater()), Client("Felipe", Cool())]

	restaurant = Restaurant(chefs, clients)
	restaurant.start()





