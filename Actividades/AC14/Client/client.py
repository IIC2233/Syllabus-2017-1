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

    C_DIR = os.getcwd()
    HOST = "localhost"
    PORT = 8080

    S_DIR = receive()
    connected = True
    while connected:
        command = input(S_DIR + " $ ")
        commands = command.split(" ")

        if command[0] == "logout":
            # Aviso al servidor que me desconecto
            connected = False

        elif commands[0] == "ls":
            # Muetra carpetas y archivos en el directorio del servidor
            pass


        elif commands[0] == "get":
            # Le pides un archivo al servidor
            pass

        elif commands[0] == "send":
            # le mandas un archivo al servidor
            file_path = get_abs_path(commands[1])
            if os.path.exists(file_path):
                pass

            else:
                print(commands[1] + " doesn't exist.")
