from json import JSONEncoder


class Client:
    def __init__(self, name, phone, address, cupons):
        self.name = name
        self.phone = phone
        self.address = address
        self.cupons = cupons


class ClientEncoder(JSONEncoder):
       def default(self, obj):
            # Creamos una serialización personalizada para el
            # el tipo de objeto Persona

            if isinstance(obj, Client):
                return {'name': obj.name,
                        'phone': obj.phone,
                        'address': obj.address,
                        'cupons' : obj.cupons + 1}

            # Mantenemos la serialización por defecto para
            # cualquier otro tipo de objeto
            return super().default(obj)


def client_decoder(dict_obj):
    if "cupons" not in dict_obj.keys():
        print("Agregando atributo cupones a información de {}".format(dict_obj["name"]))
        dict_obj["cupons"] = 0
    client = Client(**dict_obj)
    return client
