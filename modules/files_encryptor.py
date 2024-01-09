import os
import io
import zipfile

import nacl.secret
import nacl.utils
from nacl.exceptions import CryptoError
from nacl import pwhash
import getpass


def derive_key(password, salt, ops_limit = pwhash.argon2id.OPSLIMIT_MODERATE, mem_limit = pwhash.argon2id.MEMLIMIT_MODERATE):
    # Derivar una clave a partir de la contraseña y la sal usando Argon2id
    key = pwhash.argon2id.kdf(nacl.secret.SecretBox.KEY_SIZE, password.encode('utf-8'), salt, opslimit = ops_limit,
                             memlimit = mem_limit)
    return key

def compress_zip(input_file):
    # Crear un objeto de flujo de bytes en memoria
    zip_buffer = io.BytesIO()

    try:
        # Crear un archivo zip en modo escritura, pero escribir en el objeto de flujo de bytes
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isdir(input_file):
                # Comprimir la carpeta y sus contenidos
                arcname = os.path.basename(input_file)
                for root, dirs, files in os.walk(input_file):
                    for file in files:
                        file_path = os.path.join(root, file)
                        relpath = os.path.relpath(file_path, input_file)
                        zipf.write(file_path, arcname=os.path.join(arcname, relpath))
            else:
                # Si es un archivo, agregar el archivo al archivo zip
                zipf.write(input_file, arcname=os.path.basename(input_file))

        # Obtener el contenido del objeto de flujo de bytes
        zip_content = zip_buffer.getvalue()

        # Devolver el contenido del archivo comprimido
        return zip_content
    except Exception as e:
        print("Error al comprimir el archivo:", str(e))
        return None
    finally:
        # Cerrar el objeto de flujo de bytes en memoria
        zip_buffer.close()

def encrypt_file(password, input_file, output_path, hash_strength, compress_before_encrypt=False):
    # Generar una sal aleatoria
    salt = os.urandom(pwhash.argon2id.SALTBYTES)

    # Establecer los límites de operaciones y memoria para Argon2 por defecto a moderado
    ops_limit = pwhash.argon2id.OPSLIMIT_MODERATE
    mem_limit = pwhash.argon2id.MEMLIMIT_MODERATE

    # Establecer los límites de operaciones y memoria para Argon2 (Interactivo o Sensible)
    if hash_strength == "I":
        ops_limit = pwhash.argon2id.OPSLIMIT_INTERACTIVE
        mem_limit = pwhash.argon2id.MEMLIMIT_INTERACTIVE
    elif hash_strength == "S":
        ops_limit = pwhash.argon2id.OPSLIMIT_SENSITIVE
        mem_limit = pwhash.argon2id.MEMLIMIT_SENSITIVE

    # Derivar la clave a partir de la contraseña y la sal usando Argon2
    key = derive_key(password, salt, ops_limit, mem_limit)

    # Generar un nonce único
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)

    try:
        output_filename = ""
        if compress_before_encrypt:
            # Comprimir el archivo o carpeta original
            file_to_encrypt = compress_zip(input_file)
            output_filename = os.path.basename(input_file) + ".zip.enc"
        else:
            # Leer el archivo original
            with open(input_file, 'rb') as f:
                file_to_encrypt = f.read()
            output_filename = os.path.basename(input_file) + ".enc"

        # Cifrar el contenido
        ciphertext = nacl.secret.SecretBox(key).encrypt(file_to_encrypt, nonce)

        # Unir el nombre del archivo cifrado con la ruta del directorio
        output_path = os.path.join(output_path, output_filename)

        # Escribir la sal y el contenido cifrado en el nuevo archivo
        with open(output_path, 'wb') as f:
            f.write(salt + ciphertext)

        # Obtener ruta absoluta para mostrarla en pantalla
        output_path = os.path.abspath(output_path)
        print(f"Archivo cifrado exitosamente. Guardado en: {output_path}")

        return True
    except CryptoError as e:
        print("Error al cifrar el archivo:", str(e))
        return False


def decrypt_file(password, input_file, output_path, hash_strength, decompress_after_decrypt=False):
    # Leer la sal y el contenido cifrado del archivo
    with open(input_file, 'rb') as f:
        data = f.read()

    # Extraer la sal y el texto cifrado
    salt = data[:pwhash.argon2id.SALTBYTES]
    ciphertext = data[pwhash.argon2id.SALTBYTES:]

    # Derivar la clave a partir de la contraseña y la sal usando Argon2
    # Establecer los límites de operaciones y memoria para Argon2 por defecto a moderado
    ops_limit = pwhash.argon2id.OPSLIMIT_MODERATE
    mem_limit = pwhash.argon2id.MEMLIMIT_MODERATE
    if hash_strength == "I":
        ops_limit = pwhash.argon2id.OPSLIMIT_INTERACTIVE
        mem_limit = pwhash.argon2id.MEMLIMIT_INTERACTIVE
    elif hash_strength == "S":
        ops_limit = pwhash.argon2id.OPSLIMIT_SENSITIVE
        mem_limit = pwhash.argon2id.MEMLIMIT_SENSITIVE

    key = derive_key(password, salt, ops_limit, mem_limit)

    try:
        # Descifrar el contenido
        plaintext = nacl.secret.SecretBox(key).decrypt(ciphertext)

        # Quitar la extensión ".enc" del archivo cifrado
        output_filename = os.path.basename(input_file).replace(".enc", "")

        # Unir el nombre del archivo descifrado con la ruta del directorio
        output_path = os.path.join(output_path, output_filename)

        # Crear un objeto BytesIO a partir del contenido descifrado
        decrypted_file = io.BytesIO(plaintext)

        # Descomprimir el archivo descifrado en caso de ser un archivo comprimido, distinguir si es carpeta o archivo
        if decompress_after_decrypt and output_filename.endswith(".zip"):
            output_path = os.path.dirname(output_path)
            # Descomprimir usando el algoritmo deflate
            with zipfile.ZipFile(decrypted_file, 'r', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.extractall(output_path)
        else:
            # Escribir el contenido descifrado en el nuevo archivo
            with open(output_path, 'wb') as f:
                f.write(plaintext)

        # Obtener ruta absoluta para mostrarla en pantalla
        output_path = os.path.abspath(output_path)
        print(f"Archivo descifrado exitosamente. Guardado en: {output_path}")
        return True
    except CryptoError as e:
        print("Error al descifrar el archivo:", str(e))
        return False


def main():
    while True:
        # Mostrar opciones al usuario
        print("Seleccione una opción:")
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Salir")

        # Obtener la opción del usuario
        choice = input("Opción: ")

        if choice == "1":
            # Cifrar el archivo de origen y guardarlo en el directorio de destino
            file_name = input("Ruta de origen del archivo (incluido nombre de archivo): ")
            input_path = os.path.abspath(file_name)
            output_path = input("Directorio de destino del archivo cifrado (ENTER para usar el directorio del archivo original): ")
            if output_path == "":
                output_path = os.path.dirname(input_path)

            # Elegir la fuerza del hash para la contraseña (Interactiva, Moderada, Sensible)
            hash_strength = input("Elija la fuerza del hash para la contraseña:\n"
                                  "(I)nteractiva, (M)oderada, (S)ensible (Moderada por defecto): ")
            hash_strength = hash_strength.upper()

            # Mostrar la fuerza elegida
            if hash_strength == "I":
                print("Fuerza del hash elegida: Interactiva\n.")
            elif hash_strength == "S":
                print("Fuerza del hash elegida: Sensible\n.")
            else:
                print("Fuerza del hash elegida: Moderada\n.")

            # Se obtiene la contraseña del usuario sin mostrarla en pantalla
            password = getpass.getpass("Ingrese la contraseña (no aparece en pantalla): ")

            #Se informa al usuario que el proceso de cifrado ha comenzado
            print("Cifrando archivo...")
            # Se cifra el archivo
            if encrypt_file(password, input_path, output_path, hash_strength):
                # Mostrar por pantalla el fin de la ejecución
                print("Cifrado completado con éxito.\n----------------------------------\n")
            else:
                print("Error al cifrar. Revise los parámetros e intente de nuevo")

        elif choice == "2":
            # Descifrar el archivo cifrado y guardarlo en el directorio de destino
            input_path = input("Ruta de origen del archivo cifrado (incluido nombre de archivo): ")
            output_path = input("Directorio de destino del archivo descifrado (ENTER para usar el directorio del archivo original): ")
            if output_path == "":
                output_path = os.path.dirname(input_path)

            # Elegir la fuerza del hash para la contraseña (Interactiva, Moderada, Sensible)
            hash_strength = input("Elija la fuerza del hash para la contraseña:\n"
                                  "(I)nteractiva, (M)oderada, (S)ensible (Moderada por defecto)\n"
                                  "OJO: La fuerza del hash debe ser la misma que la usada para cifrar el archivo: ")
            hash_strength = hash_strength.upper()
            # Se obtiene la contraseña del usuario sin mostrarla en pantalla
            password = getpass.getpass("Ingrese la contraseña(no aparece en pantalla): ")
            # Se cifra el archivo
            if decrypt_file(password, input_path, output_path, hash_strength):
                # Mostrar por pantalla el fin de la ejecución
                print("Descifrado completado con éxito.\n----------------------------------\n")
            else:
                print("Contraseña incorrecta. Intente nuevamente.")

        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")


# if __name__ == "__main__":
#     main()


