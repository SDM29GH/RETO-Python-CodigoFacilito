def new_user(usuarios):
    num_usuarios = int(input("\n¿Cuántos usuarios quieres registrar? "))
    for i in range(num_usuarios):
        id_usuario = len(usuarios) + 1
        print(f"\nRegistro del usuario {id_usuario}")
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

            usuario = {"nombre": nombre, "apellido": apellido, "telefono": telefono, "correo": correo}
            usuarios[id_usuario] = usuario
            print(f"Hola {nombre} {apellido}, tu ID de usuario es {id_usuario}. En breve recibirás un correo a {correo}")
            break

def show_user(usuarios, id_usuario):
    if id_usuario in usuarios:
        print(f"ID: {id_usuario}, Usuario: {usuarios[id_usuario]}")
    else:
        print("No existe un usuario con ese ID.")

def edit_user(usuarios, id_usuario):
    if id_usuario in usuarios:
        print("Ingresa los nuevos datos del usuario.")
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
            usuario = {"nombre": nombre, "apellido": apellido, "telefono": telefono, "correo": correo}
            usuarios[id_usuario] = usuario
            print(f"Los datos del usuario {id_usuario} han sido actualizados.")
            break
    else:
        print("No existe un usuario con ese ID.")

def delete_user(usuarios, id_usuario):
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        print(f"El usuario {id_usuario} ha sido eliminado.")
    else:
        print("No existe un usuario con ese ID.")

def list_users(usuarios):
    print("\nUsuarios registrados:")
    for id_usuario, usuario in usuarios.items():
        print(f"ID: {id_usuario}, Usuario: {usuario}")

usuarios = {}  # Almacenará los usuarios y sus datos
opciones = {"A": new_user, "B": list_users, "C": show_user, "D": edit_user, "E": delete_user}

while True:
    print("\nA.- Registrar nuevos usuarios")
    print("B.- Listar usuarios")
    print("C.- Ver usuario")
    print("D.- Editar usuario")
    print("E.- Eliminar usuario")
    print("F.- Salir")
    opcion = input("Elige una opción: ").upper()

    match opcion:
        case "A":
            print(opciones.get("A"))
        case "B":
            print(opciones.get("C"))
        case "C":
            print(opciones.get("C"))
        case "D":
            print(opciones.get("D"))
        case _:
            print("La opción tiene que ser válida. Inténtalo de nuevo.")
