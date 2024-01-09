# Instrucciones de Instalación y uso de Files Encryptor

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

> [!DANGER]
> NO CIERRES esta ventana de carga durante el proceso. El programa crashearía.

- **Éxito o Error:**
   - Después de completar la operación, recibirás un mensaje indicando si la operación fue exitosa o si hubo algún error. En caso de ser un error, revisa si la contraseña es correcta o si has seleccionado la misma fuerza de encriptado que seleccionaste al cifrar el archivo, así como las rutas y los nombres de los archivos.

- **Limpiar Todo:**
   - Puedes utilizar el botón **Limpiar Todo** para restablecer todos los campos y preparar la aplicación para una nueva operación. Por defecto, cuando se lleva a cabo un proceso de cifrado o descifrado, se limpia toda la pantalla y los archivos cargados para evitar errores si se utiliza la aplicación para otros archivos distintos. También se hace por seguridad, para que la contraseña no se quede recordada. Lo único que no se reinicia es la lista de *radio buttons*, para evitar así errores en caso de que se siga usando la aplicación y no recuerdes seleccionar la fuerza que habías utilizado para encriptar. 
 
> [!WARNING]
> Una vez cierres la aplicación, deberás recordar con qué fuerza encriptaste un archivo, porque debes poner la misma para desencriptarlo posteriormente.

Siguiendo estos pasos, podrás utilizar File Encryptor para cifrar y descifrar archivos de manera segura.

