import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import files_encryptor as fe
import threading

class FileEncryptorApp:
    def __init__(self, root, width, height):
        # Variables para almacenar la contraseña, la ruta del archivo seleccionado y la fuerza del hash
        self.password_var = tk.StringVar()
        self.file_path_var = tk.StringVar()
        self.hash_strength_var = tk.StringVar(value="Moderado")  # Valor por defecto

        # Variable para controlar el estado del botón "Mostrar Contraseña"
        self.show_password_var = tk.BooleanVar(value=False)

        # Inicialización de la ventana
        self.root = root
        self.root.title("File Encryptor")
        self.size_center_window(self.root, width, height)

        # Atributos para la ventana de progreso
        self.progress_window = None
        self.progress_bar = None

        # Variable para saber si se quiere comprimir el archivo o descomprimir en caso de estar comprimido
        self.compress_var = tk.BooleanVar(value=False)
        self.decompress_var = tk.BooleanVar(value=False)

        # Crear widgets
        self.create_widgets()

    def size_center_window(self, window, w, h):
        # Obtener las dimensiones de la pantalla
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # Establecer las dimensiones y la posición de la ventana
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def create_widgets(self):
        # Etiqueta y entrada para la contraseña
        password_label = tk.Label(self.root, text="Contraseña:")
        password_label.grid(row=0, column=0, pady=5, padx=10, sticky=tk.E)
        self.password_entry = tk.Entry(self.root, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=0, column=1, pady=5, padx=10, sticky=tk.W)

        # Botón para mostrar/ocultar la contraseña
        self.show_password_button = tk.Button(self.root, text="Mostrar Contraseña", command=self.toggle_show_password)
        self.show_password_button.grid(row=0, column=2, pady=5, padx=10, sticky=tk.W)

        # Botón para seleccionar el archivo
        select_file_button = tk.Button(self.root, text="Seleccionar Archivo", command=self.select_file)
        select_file_button.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)

        # Botón para seleccionar carpeta
        select_file_button = tk.Button(self.root, text="Seleccionar Carpeta", command=self.select_folder)
        select_file_button.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

        # Cuadro de texto para mostrar la ruta del archivo seleccionado con barra de desplazamiento
        self.file_path_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=4, state=tk.DISABLED)
        self.file_path_text.grid(row=2, column=0, columnspan=3, pady=5, padx=10, sticky=tk.W + tk.E)

        # Radio buttons para la fuerza del hash
        hash_strength_label = tk.Label(self.root, text="Fuerza del Hash:")
        hash_strength_label.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)

        hash_strength_choices = ["Interactivo", "Moderado", "Sensible"]
        for i, choice in enumerate(hash_strength_choices):
            rb = tk.Radiobutton(self.root, text=choice, variable=self.hash_strength_var, value=choice)
            rb.grid(row=3 + i, column=1, pady=5, padx=10, sticky=tk.W)

        # Botón para limpiar toda la ventana
        clear_all_button = tk.Button(self.root, text="Limpiar Todo", command=self.clear_all)
        clear_all_button.grid(row=7, column=2, pady=5, padx=10, sticky=tk.E)

        # Botones para cifrar y descifrar
        encrypt_button = tk.Button(self.root, text="Cifrar Archivo", command=self.encrypt_file)
        encrypt_button.grid(row=6, column=0, pady=5, padx=10, sticky=tk.W)

        decrypt_button = tk.Button(self.root, text="Descifrar Archivo", command=self.decrypt_file)
        decrypt_button.grid(row=7, column=0, pady=5, padx=10, sticky=tk.W)

        # Botón checkbox para comprimir
        compress_button = tk.Checkbutton(self.root, text="Comprimir antes de cifrar", variable=self.compress_var)
        compress_button.grid(row=6, column=1, pady=5, padx=10, sticky=tk.W)

        #Botón checkbox para descomprimir
        decompress_button = tk.Checkbutton(self.root, text="Descomprimir al descifrar", variable=self.decompress_var)
        decompress_button.grid(row=7, column=1, pady=5, padx=10, sticky=tk.W)

    def create_progress_window(self, message):
        # Crear una nueva ventana para mostrar el progreso
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Proceso en ejecución")
        self.size_center_window(progress_window, 400, 100)

        # Etiqueta y barra de progreso
        progress_label = tk.Label(progress_window, text=message)
        progress_label.pack(pady=10)
        progress_bar = ttk.Progressbar(progress_window, mode="indeterminate")
        progress_bar.start(10)
        progress_bar.pack(pady=10)

        return progress_window, progress_bar

    def clear_all(self):
        # Limpiar todas las variables y los widgets
        self.password_var.set("")
        self.file_path_var.set("")
        self.show_password_var.set(False)
        self.update_password_visibility()
        self.file_path_text.config(state=tk.NORMAL)
        self.file_path_text.delete(1.0, tk.END)
        self.file_path_text.config(state=tk.DISABLED)
        self.compress_var.set(False)
        self.decompress_var.set(False)

    def toggle_show_password(self):
        # Cambiar el estado del botón "Mostrar Contraseña" y actualizar la visibilidad de la contraseña
        show_password_state = self.show_password_var.get()
        self.show_password_var.set(not show_password_state)
        self.update_password_visibility()

    def update_password_visibility(self):
        # Actualizar la visibilidad de la contraseña según el estado del botón "Mostrar Contraseña"
        show_password_state = self.show_password_var.get()
        show_char = "" if show_password_state else "*"
        self.password_entry.config(show=show_char)
        # Actualizar el texto del botón "Mostrar Contraseña"
        button_text = "Ocultar Contraseña" if show_password_state else "Mostrar Contraseña"
        self.show_password_button.config(text=button_text)

    def select_file(self):
        # Utilizar el gestor de archivos para seleccionar un archivo
        file_path = filedialog.askopenfilename()

        # Actualizar la variable y el cuadro de texto con la nueva ruta del archivo
        self.file_path_var.set(file_path)
        self.file_path_text.config(state=tk.NORMAL)
        self.file_path_text.delete(1.0, tk.END)
        self.file_path_text.insert(tk.END, file_path)
        self.file_path_text.config(state=tk.DISABLED)

    def select_folder(self):
        # Utilizar el gestor de archivos para seleccionar un directorio
        folder_path = filedialog.askdirectory()

        # Actualizar la variable y el cuadro de texto con la nueva ruta del directorio
        self.file_path_var.set(folder_path)
        self.file_path_text.config(state=tk.NORMAL)
        self.file_path_text.delete(1.0, tk.END)
        self.file_path_text.insert(tk.END, folder_path)
        self.file_path_text.config(state=tk.DISABLED)


    def encrypt_file(self):
        file_path = self.file_path_var.get()
        password = self.password_var.get()
        hash_strength = self.hash_strength_var.get()
        hash_strength_copy = hash_strength[0]

        if not file_path or not password:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo e ingrese una contraseña.")
            return

        output_path = filedialog.askdirectory()

        if not output_path:
            messagebox.showwarning("Advertencia", "Debe seleccionar un directorio de salida.")
            return

        # Crear la ventana de progreso
        self.progress_window, self.progress_bar = self.create_progress_window("Cifrando archivo...")

        # Función para realizar el cifrado en un hilo separado
        def encrypt_in_thread():
            self.progress_bar.start()
            compress_bool = self.compress_var.get()
            if os.path.isdir(file_path):
                success = fe.encrypt_file(password, file_path, output_path, hash_strength_copy, compress_before_encrypt=True)
            else:
                success = fe.encrypt_file(password, file_path, output_path, hash_strength_copy, compress_before_encrypt=compress_bool)
            self.progress_bar.stop()
            self.progress_window.destroy()

            if success:
                messagebox.showinfo("Éxito", "Archivo cifrado con éxito. Directorio:\n " + output_path)
                self.clear_all()
            else:
                messagebox.showerror("Error", "La contraseña es incorrecta o el tipo de fuerza elegida no es correcto.")

        # Iniciar el cifrado en un hilo separado
        threading.Thread(target=encrypt_in_thread).start()


    def decrypt_file(self):
        file_path = self.file_path_var.get()
        password = self.password_var.get()
        hash_strength = self.hash_strength_var.get()

        # Convertir el hash_strength y quedarte con la primera letra
        hash_strength_copy = hash_strength[0]

        if not file_path or not password:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo e ingrese una contraseña.")
            return

        # Comprobar si se trata de un archivo cifrado con extensión .enc y mostrar un mensaje de error si no lo es
        if not file_path.endswith(".enc"):
            messagebox.showerror("Error", "El archivo o directorio no está cifrado o no tiene extensión .enc. Seleciona un archivo cifrado correctamente.")
            return

        output_path = filedialog.askdirectory()

        if not output_path:
            messagebox.showwarning("Advertencia", "Debe seleccionar un directorio de salida.")
            return

        # Crear la ventana de progreso
        self.progress_window, self.progress_bar = self.create_progress_window("Descifrando archivo...")

        # Función para realizar el descifrado en un hilo separado
        def decrypt_in_thread():
            self.progress_bar.start(50)
            decompress_bool = self.decompress_var.get()
            success = fe.decrypt_file(password, file_path, output_path, hash_strength_copy, decompress_after_decrypt= decompress_bool)
            self.progress_bar.stop()
            self.progress_window.destroy()

            if success:
                messagebox.showinfo("Éxito", "Archivo descifrado con éxito. Directorio:\n " + output_path)
                # Limpiar la interfaz después de descifrar
                self.clear_all()
            else:
                messagebox.showerror("Error", "La contraseña es incorrecta, el tipo de fuerza elegida no es correcto o el archivo no es un archivo cifrado.")

        # Iniciar el descifrado en un hilo separado
        threading.Thread(target=decrypt_in_thread).start()