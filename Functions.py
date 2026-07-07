import BD

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def stock_plataforma(plataforma, juegos, inventario):
    plataforma = plataforma.lower()
    total_stock = 0
    
    for codigo, datos_juego in juegos.items():
        if datos_juego[1].lower() == plataforma:
            stock = inventario[codigo][1]
            total_stock += stock
    
    print(f"El total de stock disponibles es: {total_stock}")

def busqueda_precio(p_min, p_max, juegos, inventario):
    resultados = []
    
    for codigo, precio_stock in inventario.items():
        precio = precio_stock[0]
        stock = precio_stock[1]
        
        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            resultados.append(f"{titulo}--{codigo}")
    
    resultados.sort()
    
    if resultados:
        print(f"Los juegos encontrados son: {resultados}")
    else:
        print("No hay juegos en ese rango de precios.")

def buscar_codigo(codigo, inventario):
    return codigo.upper() in inventario


def actualizar_precio(codigo, nuevo_precio, inventario):
    codigo = codigo.upper()
    if buscar_codigo(codigo, inventario):
        inventario[codigo][0] = nuevo_precio
        return True
    return False


def validar_codigo(codigo, juegos, inventario):
    if not codigo or codigo.strip() == "":
        return False
    return codigo.upper() not in juegos


def validar_titulo(titulo):
    return titulo and titulo.strip() != ""


def validar_plataforma(plataforma):
    return plataforma and plataforma.strip() != ""


def validar_genero(genero):
    return genero and genero.strip() != ""


def validar_clasificacion(clasificacion):
    return clasificacion in ['E', 'T', 'M']


def validar_multiplayer(respuesta):
    return respuesta.lower() in ['s', 'n']


def validar_editor(editor):
    return editor and editor.strip() != ""


def validar_precio(precio):
    return precio > 0


def validar_stock(stock):
    return stock >= 0


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    codigo = codigo.upper()
    
    if codigo in juegos:
        return False
    
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo] = [precio, stock]
    return True


def eliminar_juego(codigo, juegos, inventario):
    codigo = codigo.upper()
    
    if not buscar_codigo(codigo, inventario):
        return False
    
    del juegos[codigo]
    del inventario[codigo]
    return True
        
