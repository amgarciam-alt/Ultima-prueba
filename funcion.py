def leer_opcion():
    while True:
        try:
            opcion = int(input('Ingrese una opcion 1-6:'))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print('Debe seleccionar una opcion valida')
        except ValueError:
            print('Debe ingresar un numero entero')

def stock_categoria(categoria, productos,ventas):
    totalstock = 0
    for codigo, datos in productos.items():

        if datos[1].lower() == categoria.lower():
            totalstock += ventas[codigo][1]
    print(f'El total de stock disponible es {totalstock}')

def busqueda_precio(precio_min, precio_max, productos, ventas):

    resultados = []

    for codigo, datos_ventas in ventas.items():
        precio = datos_ventas[0]
        stock = datos_ventas[1]

        if precio_min <= precio <= precio_max and stock != 0:
            nombre_producto = productos[codigo][0]
            resultados.append(f'{nombre_producto}--{codigo}')
    if len(resultados) == 0:
        print('No hay productos en ese rango de precios')
    else:
        resultados_ordenado = sorted(resultados)
        print(f'Los productos encontrados son {resultados_ordenado}')

def buscar_codigo(codigo, ventas):
    return codigo in ventas

def actualizar_precio(codigo, nuevo_precio, ventas):

    if buscar_codigo(codigo, ventas):
        ventas[codigo][0] = nuevo_precio
        return True
    else:
        return False

def validar_codigonuevo(codigo, producto):
    if codigo.strip() == '':
        return False
    if codigo in producto:
        return False
    return True

def validar_texto(texto):
    return texto.strip() != ''

def validar_enteropositivo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor >0
    except ValueError:
        return False

def validar_negativo(valor_texto):
    try:
        valor = int(valor_texto)
        return valor >=0
    except ValueError:
        return False

def validar_tamañotexto(tamaño_texto):
    return tamaño_texto in ('chico', 'mediano', 'grande')

def validar_temporada(respuesta):
    return respuesta in ('s', 'n')

def agregar_producto(codigo, nombre_producto, categoria, tamaño, tipo_leche, temporada, precio, stock_disponible, productos, ventas):
    if codigo in productos:
        return False

    productos[codigo] = [nombre_producto, categoria, tamaño, tipo_leche, temporada]

    ventas[codigo] = [precio, stock_disponible]

    return True

def eliminar_producto(codigo, productos, ventas):

    if buscar_codigo(codigo, ventas):
        del productos[codigo]
        del ventas[codigo]
        return True
    else:
        return False

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

productos = {
    'P1': ['Shake Shake', 'Bebida', 'mediano', 'entera', False],
    'P2': ['Starbuck cofee', 'cafe', 'chico', 'descreamada',True],
    'P3': ['wasa te', 'te', 'grande', 'sin lactosa', False],
    'P4': ['Shake batido', 'cafe', 'mediano', 'entera', True],
    'P5': ['jugo de te', 'te', 'chico', 'descreamada', False],

}

ventas = {
    'P1':[1000, 15],
    'P2':[5000, 0],
    'P3':[10000, 25],
    'P4':[300, 150],
    'P5':[7000, 50],
}
    


while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input('Ingrese la categoria a consultar:')
        stock_categoria(categoria, productos, ventas)
    
    elif opcion == 2:
        precio_min = None
        precio_max = None
        while precio_min is None or precio_max is None:
            try:
                precio_min = int(input('Ingrese el precio minimo'))
                precio_max = int(input('Ingrese el precio maximo'))
            except ValueError:
                print('Debe ingresar un numero entero')
                precio_min = None
                precio_max = None
        busqueda_precio(precio_min, precio_max, productos, ventas)
    
    elif opcion == 3:
        repetir = 's'
        while repetir == 's':
            codigo = input('Ingrese el codigo del producto a actualizar').upper()

            nuevoprecio = False
            while not nuevoprecio:
                nuevopreciotexto = input('Ingrese el nuevo precio')
                if validar_enteropositivo(nuevopreciotexto):
                    nuevoprecioreal = int(nuevopreciotexto)
                    nuevoprecio = True
                else:
                    print('Debe ingresar un precio en numero positivo')
            
            if actualizar_precio(codigo, nuevoprecioreal, ventas):
                print('Precio actualizado')
            else:
                print('El codigo no existe')
            repetir = input('Desea actualizar otro producto? s/n').lower()
    
    elif opcion == 4:
        codigo = input('Ingrese el codigo del producto').upper()

        if not validar_codigonuevo(codigo, productos):
            print('El codigo ya existe o es invalido')
        else:
            nombre_producto = input('Ingrese el nombre del producto')
            if not validar_texto(nombre_producto):
                print('El nombre no puede estar vacio')
            else:
                categoria = input('Ingrese la categoria del producto')
                if not validar_texto(categoria):
                    print('La categoria no puede estar vacia')
                
                else:
                    tamaño = input('Ingrese el tamaño del producto chico/mediano/grande').lower()
                    if not validar_tamañotexto(tamaño):
                        print('Tamaño invalido, debe ser chico/mediano/grande')
                    
                    else:
                        tipoleche = input('Ingrese el tipo de leche del producto')
                        if not validar_texto(tipoleche):
                            print('El tipo de leche no puede estar vacio')
                        
                        else:
                            temporadares = input('El producto es de temporada? s/n').lower()
                            if not validar_temporada(temporadares):
                                print('Respuesta invalida, debe ser s/n')
                            else:
                                preciotexto = input('Ingrese el precio del producto')
                                if not validar_enteropositivo(preciotexto):
                                    print('El precio debe ser un numero positivo')
                                else:
                                    stocktexto = input('Ingrese el stock del producto')
                                    if not validar_negativo(stocktexto):
                                        print('El stock debe ser mayor o igual a 0')
                                    else:
                                        es_temporada = (temporadares == 's')
                                        precio = int(preciotexto)
                                        stock = int(stocktexto)

                                        if agregar_producto(codigo, nombre_producto, categoria, tamaño, tipoleche, temporadares, precio, stock, productos, ventas):
                                            print('Producto agregado')
                                        else:
                                            print('El producto ya existe')

    elif opcion == 5:
        codigo = input('Ingrese el codigo del producto a eliminar').upper()

        if eliminar_producto(codigo, productos,ventas):
            print('Producto eliminado')
        else:
            print('El codigo no existe')
    
    elif opcion == 6:
        print('Saliendo del programa')
        break
       
