import os

#hash para asociar el nombre del cliente con su archivo
clientes_archivos = {}

#diccionario para guardar los clientes en memoria
clientes_info = {}

#cargar la información de los clientes desde los archivos
def cargar_clientes():
    archivos_clientes = os.listdir()
    for archivo in archivos_clientes:
        if archivo.endswith(".txt"):
            nombre_cliente = archivo.replace(".txt", "")
            clientes_archivos[nombre_cliente] = archivo
            with open(archivo, "r") as f:
                clientes_info[nombre_cliente] = f.read()

#crear nuevo cliente


        nueva_descripcion = input("Ingrese la nueva descripción del servicio: ")
        nuevo_telefono = input("Ingrese el nuevo número de teléfono del cliente: ")

        #actualizar descripción del servicio
        with open(clientes_archivos[nombre_cliente], "a") as archivo:
            archivo.write(f"Nueva descripción del servicio: {nueva_descripcion}\n")
            archivo.write(f"Nuevo número de teléfono: {nuevo_telefono}\n")

        #actualizar información del diccionario
        clientes_info[nombre_cliente] += f"\nNueva descripción del servicio: {nueva_descripcion}\nNuevo número de teléfono: {nuevo_telefono}\n"

        print("Descripción del servicio y número de teléfono actualizados correctamente.")
    else:
        print("Cliente no encontrado.")

#borrar un cliente
def borrar_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente a borrar: ")

    #checar si el cliente existe
    if nombre_cliente in clientes_archivos:
        os.remove(clientes_archivos[nombre_cliente])
        del clientes_archivos[nombre_cliente]
        del clientes_info[nombre_cliente]
        print("Cliente borrado correctamente.")
    else:
        print("Cliente no encontrado.")

#cargar información de los clientes al inicio
cargar_clientes()

#interfaz
print("Bienvenido, ingrese una opción.")
print("1. Crear nuevo cliente")
print("2. Buscar y actualizar cliente recurrente")
print("3. Borrar cliente")
opcion = input("Seleccione una opción: ")

if opcion == "1":
    crear_cliente_nuevo()
elif opcion == "2":
    buscar_actualizar_cliente_recurrente()
elif opcion == "3":
    borrar_cliente()
else:
    print("Opción no válida.")