# Installation and Usage Instructions for Files Encryptor (🇬🇧)

## Steps to Install and Configure Python and Required Modules

1. **Install Python:**
   - Visit the [official Python website](https://www.python.org/downloads/).
   - Download the latest version of Python 3.x for your operating system (Windows, macOS, or Linux).
   - Run the downloaded installer and follow the on-screen instructions.
   - Make sure to check the *Add Python to PATH* checkbox during the installation.

2. **Verify Python Installation:**
   - Open a new terminal window (Command Prompt on Windows or Terminal on macOS/Linux).
   - Execute the following command to verify the installation:

     ```bash
     python --version
     ```

   - You should see the installed Python version.

3. **Update pip (Python Package Manager):**
   - Execute the following command to upgrade pip to the latest version:

     ```bash
     python -m pip install --upgrade pip
     ```

4. **Install Required Modules:**
   - Open a terminal window.

   - Navigate to the directory C:/Users/xxxx, where xxxx represents your username. If your username is pepe, you would need to enter the following in the terminal:

     ```bash
     cd C:/Users/pepe
     ```

   - Check if you already have the required modules for the project to work. Follow these steps:
	
     1. Type 'python' and press ENTER. 
     ```bash 
     python
     ```
     2. Next, type 'help' and press ENTER
     ```bash 
     help
     ```
     3. Now type 'help()' and press ENTER
     ```bash 
     help()
     ```
     4. From now on, you can check different Python help topics. In our case, type 'modules' and press ENTER
     ```bash 
     modules
     ```
     5. It will display all the installed modules for Python on your computer. Ensure that these modules are present: `os`, `io`, `zipfile`, `zlib`, `nacl`, `getpass`, `tkinter`, `threading`.
     6. The following modules should be installed by default when installing Python: `os`, `io`, `zipfile`, `zlib`, `getpass`, `threading`, and possibly `tkinter`. Therefore, the only module that should be installed separately is `nacl`. If any other module is missing, simply search Google for how to install it.

	 To install `nacl`:

     ```bash
     python -m pip install PyNaCl
     ```

	 To install `tkinter`:

     ```bash
     python -m pip install tk
     ```

5. **Run the Application:**
   - After installing Python and the modules, you can run the application.
   - Simply run the `execute_encryptor.bat` file located in this directory.

With these steps, you should have Python installed and the necessary modules configured to run the application.

---

## Usage Instructions

Once you have installed Python and configured the required modules, you can access its various functionalities:

- **Open the Application:**
   - Run the `execute_encryptor.bat` file located in the project directory.

- **User Interface:**
   - The File Encryptor user interface will open. It includes:
	   + A text bar to enter the password, along with a button to hide or show the password.
	   + Buttons to select a file and a folder; after selection, the chosen path will be displayed in the text box. If the first option is selected, you can encrypt a single file, and in the second case, an entire folder will be compressed automatically without marking the compression checkbox.
	   + 3 *Radio* buttons with three options: *Interactive*, *Moderate*, and *Sensitive*. In ascending order of strength, they indicate whether more memory should be used and more operations should be performed in the encryption process using the *Salsa20 - Poly1305* algorithm.
	   + Encryption and decryption buttons that will execute the command to encrypt the content after selecting the output folder for the encrypted file.
	   + *Checkbox* buttons that allow indicating whether to compress before encryption or decompress a decrypted file afterward.
	   + A button to clear the entire screen.

- **Enter Information:**
   - Enter a password in the corresponding field.
   - Select a file or folder using the **Select File** or **Select Folder** buttons.
   - Choose the desired hash strength using the radio buttons.

- **Additional Options:**
   - Check the **Compress before Encrypting** box if you want to compress the file before encrypting it. If a folder is selected, it will be compressed as well.
   - Check the **Decompress when Decrypting** box if the file is compressed and you want to decompress it when decrypting.

> [!WARNING]
> Ensure that you are decompressing a file with the **.zip.enc** extension. Otherwise, the file cannot be decrypted correctly.

- **Encrypt File:**
   - Click the **Encrypt File** button to encrypt the selected file. A dialog box will appear to choose the destination folder for the encrypted file. Once selected, the file will be encrypted and saved in that directory.

- **Decrypt File:**
   Click the **Decrypt File** button to decrypt the selected file. A dialog box will appear to choose the destination folder for the decrypted file. Once selected, the file will be decrypted and saved in that directory.

- **Operation Progress:**
   - During encryption or decryption, a progress window will be displayed.

> [!WARNING]
> DO NOT CLOSE this loading window during the process. The program will crash.

- **Success or Error:**
   - After completing the operation, you will receive a message indicating whether the operation was successful or if there was an error. In case of an error, check if the password is correct or if you have selected the same encryption strength as when encrypting the file, as well as the paths and names of the files.

- **Clear Everything:**
   - You can use the **Clear Everything** button to reset all fields and prepare the application for a new operation. By default, when encryption or decryption is performed, the entire screen and loaded files are cleared to avoid errors if the application is used for other files. This is also done for security reasons so that the password is not remembered. The only thing that is not reset is the list of *radio buttons* to avoid errors if the application is still being used and you forget to select the strength you had used for encryption.

> [!WARNING]
> Once you close the application, you must remember with what strength you encrypted a file, as you need to use the same strength to decrypt it later.

Following these steps, you can use File Encryptor to securely encrypt and decrypt files.


# Instrucciones de Instalación y uso de Files Encryptor (🇪🇸)

## Pasos para instalar y configurar Python y los módulos necesarios

1. **Instalar Python:**
   - Visita el [sitio web oficial de Python](https://www.python.org/downloads/).
   - Descarga la versión más reciente de Python 3.x para tu sistema operativo (Windows, macOS o Linux).
   - Ejecuta el instalador descargado y sigue las instrucciones en pantalla.
   - Asegúrate de marcar la casilla *Agregar Python a la variable de entorno PATH* durante la instalación.

2. **Verificar la Instalación de Python:**
   - Abre una nueva ventana de terminal (Command Prompt en Windows o Terminal en macOS/Linux).
   - Ejecuta el siguiente comando para verificar la instalación:

     ```bash
     python --version
     ```

   - Deberías ver la versión de Python instalada.

3. **Actualizar pip (Administrador de Paquetes de Python):**
   - Ejecuta el siguiente comando para actualizar pip a la última versión:

     ```bash
     python -m pip install --upgrade pip
     ```

4. **Instalar Módulos Necesarios:**
   - Abre una ventana de terminal.

   - Navega al directorio C:/Users/xxxx. Donde xxxx representa tu usuario. Si tu usuario es pepe, tendrías que escribir lo siguiente en el terminal:
	
     ```bash
     cd C:/Users/pepe
     ```

   - Comprueba si ya tienes los módulos necesarios para que el proyecto funcione. Para ello, sigue los siguientes pasos:
	
     1. Escribe 'python' y pulsa ENTER. 
     ```bash 
     python
     ```
     2. A continuación, escribe 'help' y pulsa ENTER
     ```bash 
     help
     ```
     3. Ahora escribe 'help()' y pulsa ENTER
     ```bash 
     help()
     ```
     4. A partir de ahora podrás consultar diferentes ayudas sobre Python, en nuestro caso escribiremos 'modules' y pulsaremos ENTER
     ```bash 
     modules
     ```
     5. Se mostrarán todos los módulos instalados para Python en nuestro ordenador. Debes comprobar que estén todos estos módulos: `os`, `io`, `zipfile`, `zlib`, `nacl`, `getpass`, `tkinter`, `threading`
     6. Los siguientes módulos deberían estar instalados por defecto al instalar Python: `os`, `io`, `zipfile`, `zlib`, `getpass`, `threading`, e incluso creo que `tkinter`. Por tanto, el único módulo que debería instalarse aparte sería `nacl`. Si hay alguno más que no lo esté, simplemente busca en Google cómo instalarlo.

	 Para instalar `nacl`:

     ```bash
     python -m pip install PyNaCl
     ```

	 Para instalar `tkinter`:

     ```bash
     python -m pip install tk
     ```

5. **Ejecutar la Aplicación:**
   - Después de instalar Python y los módulos, puedes ejecutar la aplicación.
   - Basta con ejecutar el archivo `execute_encryptor.bat` que se encuentra dentro de este directorio.

Con estos pasos, deberías tener Python instalado y los módulos necesarios configurados para ejecutar la aplicación.

---

## Instrucciones de Uso

Una vez que hayas instalado Python y configurado los módulos necesarios, puedes acceder a sus diferentes funcionalidades:

- **Abrir la Aplicación:**
   - Ejecuta el archivo `execute_encryptor.bat` ubicado en el directorio del proyecto.

- **Interfaz de Usuario:**
   - Se abrirá la interfaz de usuario de File Encryptor. Como se puede observar, tiene:
	   + Una barra de texto para introducir la contraseña, junto con un botón que permite ocultar o mostrar dicha contraseña
	   + Un botón para seleccionar un archivo y otro para seleccionar la carpeta; tras ello, se mostrará en el cuadro de texto la ruta seleccionada. En caso de seleccionar el primero, podrás encriptar un único archivo, en el segundo caso, una carpeta completa que se comprimirá previamente de forma automática sin tener que marcar la casilla de compresión.
	   + 3 Botones de tipo *radio* con tres opciones. *Interactivo*, *moderado* y *sensible*. En orden de menos a más fuerza, permitirán indicar si se quiere usar más memoria y realizar más operaciones en el proceso de cifrado mediante el algoritmo *Salsa20 - Poly1305*.
	   + Los botones de cifrado y descifrado, que enviarán la orden para cifrar el contenido tras seleccionar la ruta a la carpeta de salida del archivo cifrado
	   + Los botones *checkbox* que permiten indicar si se quiere comprimir previo al cifrado, o descomprimir un archivo descifrado a posteriori.
	   + Un botón para limpiar toda la pantalla.

- **Ingresar Información:**
   - Ingresa una contraseña en el campo correspondiente.
   - Selecciona un archivo o carpeta utilizando los botones **Seleccionar Archivo** o **Seleccionar Carpeta**.
   - Selecciona la fuerza del hash deseada utilizando los *radio buttons*.

- **Opciones Adicionales:**
   - Marca la casilla **Comprimir antes de cifrar** si deseas comprimir el archivo antes de encriptarlo. Si es una carpeta lo que está seleccionando, se comprimirá igualmente
   - Marca la casilla **Descomprimir al descifrar** si el archivo está comprimido y deseas descomprimirlo al descifrarlo.

> [!WARNING]
> Debes asegurarte de que estás descomprimiendo un archivo con extensión **.zip.enc**. De lo contrario, no sé podrá desencriptar correctamente el archivo.

- **Cifrar Archivo:**
   - Haz clic en el botón **Cifrar Archivo** para encriptar el archivo seleccionado. Te aparecerá un cuadro de selección de la carpeta de destino del archivo cifrado. Una vez seleccionado, se cifrará el archivo y se guardará en dicho directorio.

- **Descifrar Archivo:**
   Haz clic en el botón **Descifrar Archivo** para desencriptar el archivo seleccionado. Te aparecerá un cuadro de selección de la carpeta de destino del archivo descifrado. Una vez seleccionado, se descifrará el archivo y se guardará en dicho directorio.

- **Progreso de la Operación:**
   - Durante la encriptación o desencriptación, se mostrará una ventana de progreso.

> [!WARNING]
> NO CIERRES esta ventana de carga durante el proceso. El programa crashearía.

- **Éxito o Error:**
   - Después de completar la operación, recibirás un mensaje indicando si la operación fue exitosa o si hubo algún error. En caso de ser un error, revisa si la contraseña es correcta o si has seleccionado la misma fuerza de encriptado que seleccionaste al cifrar el archivo, así como las rutas y los nombres de los archivos.

- **Limpiar Todo:**
   - Puedes utilizar el botón **Limpiar Todo** para restablecer todos los campos y preparar la aplicación para una nueva operación. Por defecto, cuando se lleva a cabo un proceso de cifrado o descifrado, se limpia toda la pantalla y los archivos cargados para evitar errores si se utiliza la aplicación para otros archivos distintos. También se hace por seguridad, para que la contraseña no se quede recordada. Lo único que no se reinicia es la lista de *radio buttons*, para evitar así errores en caso de que se siga usando la aplicación y no recuerdes seleccionar la fuerza que habías utilizado para encriptar. 
 
> [!WARNING]
> Una vez cierres la aplicación, deberás recordar con qué fuerza encriptaste un archivo, porque debes poner la misma para desencriptarlo posteriormente.

Siguiendo estos pasos, podrás utilizar File Encryptor para cifrar y descifrar archivos de manera segura.

