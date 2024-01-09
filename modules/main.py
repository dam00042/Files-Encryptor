from interface import FileEncryptorApp
import tkinter as tk

import params

if __name__ == "__main__":
    # Obtener los parámetros
    params_list = params.get_params()

    # Crear la ventana
    root = tk.Tk()

    # Crear la aplicación
    app = FileEncryptorApp(root, params_list['ANCHURA_VENTANA'], params_list['ALTURA_VENTANA'])

    # Ejecutar la aplicación
    root.mainloop()
