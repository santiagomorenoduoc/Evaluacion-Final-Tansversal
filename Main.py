import Functions
import BD

# Los diccionarios se crean en el programa principal
juegos = BD.juegos
inventario = BD.inventario

print("========== BIENVENIDO A GAMEHUB ==========")
print("Sistema de gestión de catálogo de videojuegos\n")

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")
    
    opcion = Functions.leer_opcion()
    
    if opcion == 1:
        plataforma = input("Ingrese plataforma a consultar: ")
        Functions.stock_plataforma(plataforma, juegos, inventario)
    
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        
        Functions.busqueda_precio(p_min, p_max, juegos, inventario)
    
    elif opcion == 3:
        while True:
            codigo = input("Ingrese código del juego: ")
            
            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    break
                except ValueError:
                    print("Debe ingresar un valor entero")
            
            if Functions.actualizar_precio(codigo, nuevo_precio, inventario):
                print("Precio actualizado")
            else:
                print("El código no existe")
            
            respuesta = input("¿Desea actualizar otro precio (s/n)?: ").lower()
            if respuesta != 's':
                break
    
    elif opcion == 4:
        codigo = input("Ingrese código del juego: ")
        if not Functions.validar_codigo(codigo, juegos, inventario):
            print("El código ya existe")
            continue
        
        titulo = input("Ingrese título: ")
        if not Functions.validar_titulo(titulo):
            print("El título no es válido")
            continue
        
        plataforma = input("Ingrese plataforma: ")
        if not Functions.validar_plataforma(plataforma):
            print("La plataforma no es válida")
            continue
        
        genero = input("Ingrese género: ")
        if not Functions.validar_genero(genero):
            print("El género no es válido")
            continue
        
        clasificacion = input("Ingrese clasificación: ").upper()
        if not Functions.validar_clasificacion(clasificacion):
            print("La clasificación debe ser exactamente 'E', 'T' o 'M'")
            continue
        
        multiplayer_input = input("¿Es multiplayer? (s/n): ").lower()
        if not Functions.validar_multiplayer(multiplayer_input):
            print("Debe ingresar 's' o 'n'")
            continue
        multiplayer = multiplayer_input == 's'
        
        editor = input("Ingrese editor: ")
        if not Functions.validar_editor(editor):
            print("El editor no es válido")
            continue
        
        while True:
            try:
                precio = int(input("Ingrese precio: "))
                if not Functions.validar_precio(precio):
                    print("El precio debe ser mayor a cero")
                    continue
                break
            except ValueError:
                print("El precio debe ser un entero")
        
        while True:
            try:
                stock = int(input("Ingrese stock: "))
                if not Functions.validar_stock(stock):
                    print("El stock debe ser mayor o igual a cero")
                    continue
                break
            except ValueError:
                print("El stock debe ser un entero")
        
        if Functions.agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
            print("Juego agregado")
        else:
            print("El código ya existe")
    
    elif opcion == 5:
        codigo = input("Ingrese código del juego: ")
        
        if Functions.eliminar_juego(codigo, juegos, inventario):
            print("Juego eliminado")
        else:
            print("El código no existe")
    
    elif opcion == 6:
        print("Programa finalizado.")
        break