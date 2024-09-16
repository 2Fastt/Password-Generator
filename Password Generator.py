import random

def generar_password(longitud, incluir_mayus=True, incluir_numeros=True, incluir_simbolos=True):
    # Se definen todos los caracteres posibles que pueden ser utilizados a la hora de generar la contraseña.
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    caracteres = minusculas
    
    if incluir_mayus:
        caracteres += mayusculas  # Metemos mayúsculas a la contraseña si el usuario responde "s"
    if incluir_numeros:
        caracteres += numeros  # Lo mismo con números
    if incluir_simbolos:
        caracteres += simbolos  # Lo mismo con los símbolos
    
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))  # Genera una password aleatoriamente cogiendo caracteres del conjunto 'caracteres' y dependiendo de las respuestas del usuario.
    return contrasena

def main():
    ascii_art = """
 $$$$$$\\  $$$$$$$$\\                   $$\\     $$\\     
$$  __$$\\ $$  _____|                  $$ |    $$ |    
\\__/  $$ |$$ |   $$$$$$\\   $$$$$$$\\ $$$$$$\\ $$$$$$\\   
 $$$$$$  |$$$$$\\ \\____$$\\ $$  _____|\\_$$  _|\\_$$  _|  
$$  ____/ $$  __|$$$$$$$ |\\$$$$$$\\    $$ |    $$ |    
$$ |      $$ |  $$  __$$ | \\____$$\\   $$ |$$\\ $$ |$$\\ 
$$$$$$$$\\ $$ |  \\$$$$$$$ |$$$$$$$  |  \\$$$$  |\\$$$$  |
\\________|\\__|   \\_______|\\_______/    \\____/  \\____/ 
                                                      
                                                      
    """
    print(ascii_art)
    
    try:
        longitud = int(input("¿Cuál quieres que sea la longitud de la contraseña?: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return
    
    incluir_mayus = input("¿Quieres que la contraseña tenga mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Quieres que la contraseña tenga números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Quieres que la contraseña tenga símbolos? (s/n): ").lower() == 's'

    contrasena = generar_password(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)
    print("\nTu contraseña generada es:\n")
    print(contrasena)
    
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()
