from client_class import Client, ClientEncoder, client_decoder
from os import listdir
from json import dump, load


class Pizzeria:
    def __init__(self, name, db_directory):
        self.name = name
        self.db_directory = db_directory

    def sale_old_client(self, name):
        # venta a un cliente antiguo
        client = self.find_client(name)

        # se canjean los cupones
        if client.cupons >= 10:
            print('{} se ha ganado una pizza gratis'.format(client.name))
            client.cupons -= 10
        print('{} ha comprado una pizza. Número de cupones acomulados {}'.format(client.name, client.cupons))

        # se guarda nueva informacion
        self.update_client(client)

    def find_client(self, name):
        # busqueda del archivo del cliente
        for file_name in listdir(self.db_directory):
            if file_name == name+'.json':
                # si lo encuentra, lo decodifica y retorna
                with open(self.db_directory + '/'+file_name, 'r') as file_client:
                    cliente = load(file_client, object_hook=lambda json_obj : client_decoder(json_obj))
                return cliente

    def sale_new_client(self, name, phone, address):
        # se crea un nuevo cliente
        client = Client(name, phone, address, 0)
        print("Venta a nuevo cliente {}, phone {}, address {}".format(client.name, client.phone, client.address))

        # se guarda su informacion
        self.update_client(client)

    def update_client(self, client):
        # se actualiza la informacion del cliente en el archivo
        with open(self.db_directory+'/'+client.name+'.json', 'w') as client_file:
            dump(client, client_file,cls=ClientEncoder)


if __name__ == "__main__":
    p = Pizzeria('PapAndrés', './clients')
    # p.sale_new_client("Dr. Mavrakis", 96663, "Stgo")
    # p.sale_new_client("Flo", 98113454, "Rancagua")
    # p.sale_new_client("La otra Flo", 98113455, "Concepción")
    # p.sale_new_client("Andrés", 98113456, "Viña")
    # p.sale_new_client("Rodolfo", 98113457, "Puerto Montt")
    # p.sale_new_client("El benevolente Bucci", 98113458, "Curicó")

    # mavrakis tiene mas de 10 pizzas
    p.sale_old_client("Dr. Mavrakis")
    # flo no tiene cupones de pizza
    p.sale_old_client("Flo")
