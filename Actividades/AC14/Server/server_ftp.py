import os


def send():
    # Funcion para mandar comandos y archivos
    pass


def receive():
    # Funcion que recibe cualquier dato mandado por el servidor
    return ""


def get_path(path):
    abs_path = get_abs_path(path)
    if not os.path.exists(abs_path):
        return -1
    elif not os.path.isdir(abs_path):
        return 0
    else:
        return abs_path


def get_abs_path(path):
    if os.path.isabs(path):
        return path
    else:
        return os.path.abspath(os.sep.join(C_DIR.split(os.sep) +
                                           path.split(os.sep)))


if __name__ == '__main__':

    HOST = "localhost"
    PORT = 8080
    C_DIR = os.getcwd()

    client = None

    while True:
        # Conectarse al servidor

        connected = True
        while connected:
            # Recibir comandos
            message = receive()

            action = ""
            if action == "ls":
                pass

            elif action == "logout":
                pass


            elif action == "get":
                pass

            elif action == "send":
                pass
