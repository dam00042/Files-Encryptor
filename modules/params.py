import json

def get_params():
    # Cargar los parámetros de config.json en una variable
    with open("config.json", "r") as file:
        params = json.load(file)
    # Cerrar el fichero
    file.close()

    return params