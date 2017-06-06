import sys
import json
import socket
import threading

__author__ = 'Vicente' # Modificado por Ivania :) Remodificado por fringles y diiru

PORT = 3492

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



if __name__ == '__main__':
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