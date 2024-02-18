print("¿Cuántos usuarios quieres registrar?")
num_usuarios = int(input())
identificadores = []  # Almacenará los identificadores de los usuarios
usuarios = []

for i in range(num_usuarios):
    print(f"\nRegistro del usuario {i+1}")
    while True:
        nombre = input("Nombre(s): ")
        apellido = input("Apellido(s): ")
        telefono = input("Número de teléfono: ")
        correo = input("Correo electrónico: ")

        if len(nombre) < 5 or len(nombre) > 50:
            print("El nombre debe tener entre 5 y 50 caracteres.")
            continue
        if len(apellido) < 5 or len(apellido) > 50:
            print("El apellido deben tener entre 5 y 50 caracteres.")
            continue
        if len(telefono) < 10:
            print("El número de teléfono debe ser de 10 o mas dígitos.")
            continue
        if len(correo) < 5 or len(correo) > 50:
            print("El correo electrónico debe tener entre 5 y 50 caracteres.")
            continue

        lista_usuario = [nombre, apellido, telefono, correo]  # Creamos una lista con los datos del usuario
        usuarios.append(lista_usuario)  # Añadimos la lista a la lista de usuarios
        
        id_usuario = i + 1  # Generamos un identificador único para el usuario
        identificadores.append(id_usuario)  # Añadimos el identificador a la lista
        print(f"Hola {nombre} {apellido}, tu ID de usuario es {id_usuario}. En breve recibirás un correo a {correo}")
        break

    print("\nUsuarios registrados:")
    for lista_usuario in usuarios:
        print(lista_usuario)
    
    print("\nIdentificadores de los usuarios registrados:")
    for id_usuario in identificadores:
        print(id_usuario)