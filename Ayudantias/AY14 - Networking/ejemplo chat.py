import socket
import threading
import sys
import json

__author__ = 'Vicente' # Modificado por Ivania :)

PORT = 3491

class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = PORT
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port)) # El cliente revisa que el servidor esté disponible
            # Una vez que se establece la conexión, se pueden recibir mensajes
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            self._isalive = True
            recibidor.start()

        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        while self._isalive:
            data = self.s_cliente.recv(1024)
            data_decoded = data.decode('utf-8')
            mensaje = json.loads(data_decoded)
            print('Datos recibidos del server: {}'.format(data_decoded))
            if mensaje['status'] == 'msg':
                print('Mensaje recibido del server: {}'.format(mensaje['content']))

    def enviar(self, mensaje):
        msj_final = {'status': 'msg', 'content': self.usuario + ": " + mensaje}
        msj_final_json = json.dumps(msj_final)
        self.s_cliente.send(msj_final_json.encode('utf-8'))

    def desconectar(self):
        self._isalive = False
        msj_final = {'status': 'disconnect'}
        msj_final_json = json.dumps(msj_final)
        self.s_cliente.send(msj_final_json.encode('utf-8'))


class Servidor:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = PORT
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Debemos hacer el setup para poder escuchar a los clientes que se quieran conectar
        self.s_servidor.bind((self.host, self.port))
        # En este caso solo queremos escuchar un cliente
        self.s_servidor.listen(2)
        self.cliente = None
        thread = threading.Thread(target=self.aceptar, daemon=True)
        thread.start()

    def recibir_mensajes(self):
        while True:
            try:
                data = self.cliente.recv(2048)
                data_decoded = data.decode('utf-8')
                mensaje = json.loads(data_decoded)
                print('Datos recibidos en el server: {}'.format(mensaje))
                if mensaje['status'] == 'msg':
                    print('Mensaje recibido: {}'.format(mensaje['content']))
                elif mensaje['status'] == 'disconnect':
                    self.desconectar_cliente()
            except AttributeError:
                print('Cliente desconectado')
                break

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        print('Cliente conectado')
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(target=self.recibir_mensajes, args=())
        thread_cliente.daemon = True
        thread_cliente.start()

    def enviar(self, mensaje):
        if self.cliente:
            msj_final = {'status': 'msg', 'content': self.usuario + ": " + mensaje}
            msj_final_json = json.dumps(msj_final)
            self.cliente.send(msj_final_json.encode('utf-8'))
        else:
            print('No hay cliente conectado')

    def desconectar_cliente(self):
        self.cliente = None
        thread = threading.Thread(target=self.aceptar, daemon=True)
        thread.start()


if __name__ == "__main__":

    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre)
        while True:
            texto = input('>    ')
            server.enviar(texto)

    elif pick == "C":
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        while True:
            inputing = input('[1] Mandar mensaje\n[2] Desconectarse\n>  ')
            if inputing == '1':
                texto = input('>    ')
                client.enviar(texto)
            elif inputing == '2':
                client.desconectar()
                break
