cantidad_usuarios = int(input("Indique la cantidad de usuarios para registrarse: "))
print("Ingrese", cantidad_usuarios, "usuarios")
numero = 0

while numero < cantidad_usuarios:
    usuario = numero + 1
    nombre = input("Ingresa el nombre del usuario " + str(usuario) + ":")
    while len(nombre) < 5 or len(nombre) > 50:
        print("Asegúrese que el nombre sea entre 5 y 50 caracteres")
        nombre = input("Ingresa el nombre del usuario " + str(usuario) + ":")
        if 5 <= len(nombre) <= 50:
            print("El nombre de usuario ", usuario," es: ", nombre)
    apellido = input("Ingresa del apellido del usuario " + str(usuario) + ":")
    while len(apellido) < 5 or len(apellido) > 50:
        print("Asegúrese que el apellido sea entre 5 y 50 caracteres")
        apellido = input("Ingresa el apellido del usuario " + str(usuario) + ":")
        if 5 <= len(apellido) <= 50:
            print("El apellido del usuario ", usuario," es: ", apellido)
    telefono = input("Ingresa el número de teléfono del usuario " + str(usuario) + ":")
    while len(telefono) < 5 or len(telefono) > 50:
        print("Asegúrese que el número de teléfono sea de 10 o más dígitos")
        telefono = input("Ingresa el número de teléfono del usuario " + str(usuario) + ":")
        if len(telefono) >= 10:
            print("El teléfono del ", usuario, " es: ", telefono)
    correo = input("Ingresa el correo electrónico del usuario " + str(usuario) + ":")
    while len(correo) < 5 or len(correo) > 50:
        print("Asegúrese que el correo electrónico sea entre 5 y 50 caracteres")
        correo = input("Ingresa el correo electrónico del usuario " + str(usuario) + ":")
        if 5 <= len(correo) <= 50:
            print("El correo electrónico del usuario ", usuario, " es:", correo)         
    print("El usuario", nombre, apellido, telefono, correo, "se ha registrado correctamente")
    numero = numero + 1

