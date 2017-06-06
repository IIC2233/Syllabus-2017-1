import socket
import threading
import sys
import json

__author__ = 'Vicente' # Modificado por Ivania :)

PORT = 3490



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

        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre)
        while True:
            texto = input('>    ')
            server.enviar(texto)
