color = "green"

match color:
    case "red":
        print("El color es rojo")
    case "blue":
        print("El color es azul")
    case "green":
        print("El color es verde")
    case _:
        print("El color es otro")

cantidad_usuarios = int(input("Indique la cantidad de usuarios para registrarse: "))
print("Ingrese", cantidad_usuarios, "usuarios")
numero = 0

while numero < cantidad_usuarios:
    id_usuario = numero + 1
    nombre = input("Ingrese el nombre del usuario " + str(id_usuario) + ": ")
    while len(nombre) < 5 or len(nombre) > 50:
        print("Asegúrese que el nombre sea entre 5 y 50 id_racteres")
        nombre = input("Ingrese el nombre del usuario " + str(id_usuario) + ": ")
        if 5 <= len(nombre) <= 50:
            print("El nombre de usuario ", id_usuario," es: ", nombre)
    apellido = input("Ingrese el apellido del usuario " + str(id_usuario) + ": ")
    while len(apellido) < 5 or len(apellido) > 50:
        print("Asegúrese que el apellido sea entre 5 y 50 caracteres")
        apellido = input("Ingrese el apellido del usuario " + str(id_usuario) + ": ")
        if 5 <= len(apellido) <= 50:
            print("El apellido del usuario ", id_usuario," es: ", apellido)
    telefono = input("Ingrese el número de teléfono del usuario " + str(id_usuario) + ": ")
    while len(telefono) < 5 or len(telefono) > 50:
        print("Asegúrese que el número de teléfono sea de 10 o más dígitos")
        telefono = input("Ingrese el número de teléfono del usuario " + str(id_usuario) + ": ")
        if len(telefono) >= 10:
            print("El teléfono del ", id_usuario, " es: ", telefono)
    correo = input("Ingrese el correo electrónico del usuario " + str(id_usuario) + ": ")
    while len(correo) < 5 or len(correo) > 50:
        print("Asegúrese que el correo electrónico sea entre 5 y 50 caracteres")
        correo = input("Ingrese el correo electrónico del usuario " + str(id_usuario) + ": ")
        if 5 <= len(correo) <= 50:
            print("El correo electrónico del usuario ", id_usuario, " es: ", correo)         
    print("El usuario", nombre, apellido, telefono, correo, "se ha registrado correctamente")
    lista_usuario = [id_usuario, nombre, apellido, telefono, correo]
    for index, lista in enumerate(lista_usuario):
        print( index, "es: ", lista)
        
    print(lista_usuario)
    numero = numero + 1