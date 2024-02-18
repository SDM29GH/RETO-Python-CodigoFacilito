print("¿Cuántos usuarios quieres registrar?")
num_usuarios = int(input())

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
        if len(telefono) != 10:
            print("El número de teléfono debe tener 10 dígitos.")
            continue
        if len(correo) < 5 or len(correo) > 50:
            print("El correo electrónico debe tener entre 5 y 50 caracteres.")
            continue

        print(f"Hola {nombre} {apellido}, en breve recibirás un correo a {correo}")
        break