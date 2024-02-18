usuarios = {}  # Almacenará los usuarios y sus datos

while True:
    print("\nA.- Registrar nuevos usuarios")
    print("B.- Listar usuarios")
    print("C.- Ver usuario")
    print("D.- Editar usuario")
    print("E.- Salir")
    opcion = input("Elige una opción: ").upper()

    if opcion == "A":
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

    elif opcion == "B":
        print("\nUsuarios registrados:")
        for id_usuario, usuario in usuarios.items():
            print(f"ID: {id_usuario}, Usuario: {usuario}")
    elif opcion == "C":
        id_usuario = int(input("Ingresa el ID del usuario que quieres ver: "))
        if id_usuario in usuarios:
            print(f"ID: {id_usuario}, Usuario: {usuarios[id_usuario]}")
        else:
            print("No existe un usuario con ese ID.")

    elif opcion == "D":
        id_usuario = int(input("Ingresa el ID del usuario que quieres editar: "))
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
    elif opcion == "E":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")