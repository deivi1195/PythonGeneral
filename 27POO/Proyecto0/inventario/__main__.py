import datetime
import os
import pickle
from modelos.inventario import Inventario
from modelos.producto import Producto
from modelos.venta import Venta


def mostrar_menu():
    """
    Muestra el menu de las operaciones disponibles.
    """
    print('1. Registrar Producto')
    print('2. Vender un Productos')
    print('3. Buscar un Producto por su Codigo')
    print('4. Cambiar Disponibilidad de un Producto')
    print('5. Productos vendidos en un rango de fecha')
    print('6. Top 5 de los Productos mas Vendidos')
    print('7. Top 5 de los Productos menos Vendidos')
    print('0. Salir')

#Funcion auxiliar
def capturar_entero(mensaje):
    """
    Captura un numero entero. valida el ingreso de datos
    
    Parameters:
    mensaje: texto personalizado a mostrar para la captura de un numero.
    
    Returns:
    Numero entero resultado de la captura.
    """
    while True:
        try:
            numero = int(input(f'{mensaje}: '))
            
            return numero
        except ValueError:
            print('ERROR: Debe digitar un numero entero.')
            
        print()

#Funcion auxiliar
def capturar_real(mensaje):
    """
    Captura un numero real. valida el ingreso de datos
    
    Parameters:
    mensaje: texto personalizado a mostrar para la captura de un numero.
    
    Returns:
    Numero real resultado de la captura.
    """
    while True:
        try:
            numero = float(input(f'{mensaje}: '))
            
            return numero
        except ValueError:
            print('ERROR: Debe digitar un numero real.')
            
        print()

#Funcion auxiliar        
def capturar_cadena(mensaje):
    """
    Captura una cadena de caracteres. valida el ingreso de datos
    
    Parameters:
    mensaje: texto personalizado a mostrar para la captura de una cadena de caracteres.
    
    Returns:
    cadena de caracteres resultado de la captura.
    """
    while True:
        
        # Strip() retorna una cadena con los espacios en blanco iniciales y finales eliminados
        cadena = input(f'{mensaje}: ').strip()
        
        # si un numero distinto de 0 es semanticamente True
        # 3 por lo tanto si la longitud de la cadena es diferente a 0 es True
        # entonces como es True procede a retortan "cadena"
        if len(cadena):                     
            return cadena
        else:
            print('MENSAJE: Debe digitar una cadena de caracteres con texto.')
        
            
        print()

def listar_productos(productos):
    """
    Por cada producto mostramos el id y el nombre, recordando que son diccionarios
    """
    for p in productos:
        print(f"{p.codigo} - {p.nombre}")

def continuar():
    """
    Muestra mensaje de continuacion en la consola
    """
    print()
    print('Presione ENTER para continuar...', end='')
    input()
    print()
    
def cargar_inventario():
    while True:
        print('Desea cargar los datos del inventario y las ventas desde el archivo `inventario.pickle`?')
        print('1. Si')
        print('2. No')
        opcion = capturar_entero('Digite la opcion')
        
        if opcion == 1 or opcion == 2:
            break
        
    if opcion == 1:
        with open('inventario/inventario.pickle', 'rb') as f:
            inventario = pickle.load(f)
            return inventario
        
    return None

def guardar_datos(inventario):
    while True:
        print('Desea guardar los datos de productos y ventas en el archivo `inventario.pickle`?')
        print('1. Si')
        print('2. No')
        opcion = capturar_entero('Digite la opcion')
        
        if opcion == 1 or opcion == 2:
            break
        
    if opcion == 1:
        #Guardar los datos en el archivo `inventario.pickle`
        with open('inventario/inventario.pickle', 'wb') as f:
            
            
            pickle.dump(inventario, f)
        
        
        return True
    else:
        return False
    

def main():
    """
    Punto de entrada a la aplicacion
    """ 
    
    inventario = Inventario()
    
    # si existe el archivo = os.path.isfile('inventario.pickle')
    if os.path.isfile('inventario/inventario.pickle'):
        resultado = cargar_inventario()
        
        if resultado:
            inventario.productos = resultado['productos']
            inventario.ventas = resultado['ventas']
    
    #  en este while se cicla las opciones del menu
    while True:
        # en este while se cicla la respuesta si es un valor diferente a un numero entero.
        while True:
            try:
                mostrar_menu()            
                opcion = int(input('Digite la opcion: '))
                if 0 <= opcion <= 7:
                    break
                else:
                    print()
                    print('MENSAJE: Debe digitar un numero mayor o igual a cero y menor o igual a 7.')
            except ValueError as e:
                print()
                print('ERROR: Debe digitar un numero entero valido.')
            
            continuar()  
            
        print()
                
        #si el usuario teclea la opcion 0 se acaba el ciclo while osea el programa.
        if opcion == 0:
            break
        
        # egistrando un nuevo producto
        elif opcion == 1:
            #capturando el ID del prooducto.
            while True:
                codigo_producto = capturar_entero('Digite el ID del nuevo producto')

                if codigo_producto > 0:
                    producto = inventario.buscar_producto(codigo_producto)
                
                    if producto is None:
                        break
                    else:
                        print()
                        print('MENSAJE: Ya existe con el ID digitado.')
                else:
                    print()
                    print('MENSAJE: El ID del producto debe ser un numero mayor a cero.')
                    
                continuar()
                            
            #capturando el nombre del producto.
            # Ya el la funcion capturar cadena se valida
            nombre_producto = capturar_cadena('Digite el nombre del nuevo producto')
            
            #capturando el precio del producto.
            # hay que validar que el numero sea mayor a cero. la funcion capturar_real, solo valida que la captura de un numero real sea positivo o negativo
            
            while True:
                precio_producto = capturar_real('Digite el precio del nuevo producto')

                if precio_producto > 0:
                    break
                else:
                    print()
                    print('MENSAJE: Debe digitar un precio positivo para el producto.')
                
                continuar()
            
            #capturando la cantidad del producto.
            while True:
                cantidad_producto = capturar_entero('Digite la cantidad del nuevo producto')

                if cantidad_producto > 0:
                    break
                else:
                    print()
                    print('MENSAJE: debe digitar una cantidad positiva para el producto.')
                    
                continuar()
                    
            # Especificar si el producto esta disponible o no.
            while True:
                print('1. Disponible')
                print('2. NO Disponible')
                disponible = capturar_entero('Digite la opcion para la disponibilidad del producto')
                
                if disponible == 1 or disponible == 2:
                    # si digitan 1 entonces se cumple lo de abajo y es True
                    # si digitan 2 entonces lo de abajo no se cumple entonces es False
                    disponible = disponible == 1
                    break
                else:
                    print()
                    print(f'MENSAJE: La opcion {disponible} no esta disponible. Seleccione 1 o 2.')
                
                continuar()
            
            #Tenemos un diccionario que refleja los datos de un producto
            nuevo_producto = Producto(codigo_producto, nombre_producto, precio_producto, cantidad_producto, disponible)
            
            inventario.registrar_producto(nuevo_producto)
            
            print()
            print('MENSAJE: El producto se ha creado de forma sastisfactoria.')
            
            
        
        # Realizar una venta
        if opcion == 2:
            # si existe longitud en productos, entonces se ejecuta el if de abajo
            if len(inventario.productos):
                # este while es para verificar que el numero que digite el usuario este en el rango de los productos existentes.
                while True:
                    # generar un listado de los id de los productos
                    # se crea una funcion auxiliar listar_productos()
                    # listra producto me pide el ID y el producto
                    listar_productos(inventario.productos)
                    # aqui se captura el ID
                    id_producto = capturar_entero('Digite el ID del producto')
                    
                    # el producto del ID que el usuario escribio
                    producto = inventario.buscar_producto(codigo_producto)
                    
                    # si esxiste un producto con ese ID terminamos con el ciclo
                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                        
                # bucle while para volver a pedir capturar el numero de la cantidad en caso de que digite un valor que no corresponde
                while True:
                    # Solicitando la cantidad del producto
                    cantidad_producto = capturar_entero('Digite la cantidad que desea vender')
                    # Validando que la cantidad del producto sea mayor a cero
                    if cantidad_producto > 0:
                        # Validando que la cantidad del producto sea menor o igual a lo que esta en el "inventario"
                        if cantidad_producto <= producto.cantidad:
                            break
                        else:
                            print()
                            print(f'No esxiste cantidad suficiente para la venta. solo hay {producto.cantidad} unidades.')
                    else:
                        print()
                        print('MENSAJE: debe digitar una cantidad positiva para el producto.')
                    
                    continuar()
                
                # aqui se capturan las caracteristicas del producto que se vendera
                nueva_venta = Venta(codigo_producto, cantidad_producto, producto.precio * cantidad_producto)
                
                # aqui se realiza la venta, se a;ade a lista ventas con los datos de nueva_venta
                inventario.realizar_venta(nueva_venta)
                
                print('Total: $%.2f' % (nueva_venta.total_sin_iva * 1.19))
                
                print()
                print('MENSAJE: La venta se ha realizado de forma satisfactoria.')
            else:
                print()
                print('MENSAJE: Aun no ha registrado productos.')  
        
        # buscar un producto por su codigo
        elif opcion == 3:
            # si existe longitud en productos, entonces se ejecuta el while de abajo
            if len(inventario.productos):
                # este while es para verificar que el numero que digite el usuario este en el rango de los productos existentes.
                while True:
                    # generar un listado de los id de los productos
                    # se crea una funcion auxiliar listar_productos()
                    # listra producto me pide el ID y el producto
                    listar_productos(inventario.productos)
                    # aqui se captura el ID
                    codigo_producto = capturar_entero('Digite el ID del producto')
                    
                    # el producto del ID que el usuario escribio
                    producto = inventario.buscar_producto(codigo_producto)
                    
                    # si esxiste un producto con ese ID terminamos con el ciclo
                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                        
                    continuar()
                
                print()       
                # crea una funcion en el archivo inventario_funciones ya que esta ligada mas a funciones de inventario por lo tanto no se crea como auxiliar
                # se muestran los datos del producto.
                inventario.mostrar_datos_producto(producto)                           
            else:
                print()
                print('MENSAJE: Aun no ha registrado productos.')
                
        # Cambiar la disponibilidad de un producto.          
        elif opcion == 4:
            # si existe longitud en productos, entonces se ejecuta el if de abajo
            if len(inventario.productos):
                # este while es para verificar que el numero que digite el usuario este en el rango de los productos existentes.
                while True:
                    # generar un listado de los id de los productos
                    # se crea una funcion auxiliar listar_productos()
                    # listra producto me pide el ID y el producto
                    listar_productos(inventario.productos)
                    # aqui se captura el ID
                    id_producto = capturar_entero('Digite el ID del producto')
                    
                    # el producto del ID que el usuario escribio
                    producto = inventario.buscar_producto(codigo_producto)
                    
                    # si esxiste un producto con ese ID terminamos con el ciclo
                    if producto:
                        break
                    else:
                        print()
                        print('MENSAJE: Debe escribir un ID de producto existente.')
                        
                    continuar()
                
                # funcion para cambiar estado del producto
                inventario.cambiar_estado_producto(producto)
                # y luego se muestran los datos del producto.
                inventario.mostrar_datos_producto(producto)                           
            else:
                print()
                print('MENSAJE: Aun no ha registrado productos.')
        
        # Productos vendidos en un rango de fecha
        elif opcion == 5:
            # si existe longitud en productos, entonces se ejecuta el if de abajo
            if len(inventario.productos):
                # si hay ventas en la lista de ventas
                if len(inventario.ventas):                    
                # solemanete se termina el ciclo cuando se ingrese una fecha valida
                    while True:
                        try:
                            fecha_inicio = capturar_cadena('Digite la fecha de inicio (AAAA-MM-DD)')
                            #despues de capturar el str de fecha debemos convertilo a un objeto datetime
                            fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
                            break
                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha valida con el formato AAAA-MM-DD') 
                            
                        print()
                    
                    while True:
                        try:
                            fecha_final = capturar_cadena('Digite la fecha final (AAAA-MM-DD)')
                            #despues de capturar el str de fecha debemos convertilo a un objeto datetime
                            fecha_final = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')
                            break
                        except ValueError:
                            print()
                            print('ERROR: Debe digitar una fecha valida con el formato AAAA-MM-DD') 
                            
                        print()
                    
                    # ventas_rango es tipo list()  
                    ventas_rango = inventario.ventas_rango_fechas(fecha_inicio, fecha_final)
                    
                    if len(ventas_rango):
                        #creamos una funcion en inventerio_funciones mostrar_datos_ventas()
                        for v in ventas_rango:
                            inventario.mostrar_datos_ventas(v)
                            print()                    
                    else:
                        print()
                        print('MENSAJE: No hay ventas para el rango seleccionado')
                else:
                    print()
                    print('MENSAJE: Aun no ha efectuado ninguna venta.')                
            else:
                print()
                print('MENSAJE: Aun no ha registrado productos.')
        
        # Top 5 de los Productos mas Vendidos
        elif opcion == 6:
            # si existe longitud en productos, entonces se ejecuta el if de abajo
            if len(inventario.productos):
                # si hay ventas en la lista de ventas
                if len(inventario.ventas):             
                    productos_vendidos = inventario.top_5_mas_vendidos()
                    #con este print se muestra la tupla que se genrera de [(id del producto, cantidad vendida)]
                    #print(productos_vendidos)
                    
                    print('Top 5 de los productos mas vendidos')
                    for p in productos_vendidos:
                        inventario.mostrar_datos_venta_producto(p)  
                        print()                
                else:
                    print()
                    print('MENSAJE: Aun no ha efectuado ninguna venta.')                
            else:
                print()
                print('MENSAJE: Aun no ha registrado productos.')
        
        # Top 5 de los Productos menos Vendidos        
        elif opcion == 7:
             # si existe longitud en productos, entonces se ejecuta el if de abajo
            if len(inventario.productos):
                # si hay ventas en la lista de ventas
                if len(inventario.ventas):             
                    productos_vendidos = inventario.top_5_menos_vendidos()
                    
                    print('Top 5 de los productos menos vendidos')
                    for p in productos_vendidos:
                        inventario.mostrar_datos_venta_producto(p)  
                        print()              
                else:
                    print()
                    print('MENSAJE: Aun no ha efectuado ninguna venta.')                
            else:
                print()
                print('MENSAJE: Aun no ha registrado productos.')
            
        continuar()    
            
        
    print()
    
    if len(inventario.productos):
        
        if guardar_datos(inventario):
            print('Los datos del inventario (productos y ventas) se han guardado en disco')
        else:
            print('Ha omitido almacenar los datos en disco.')
            
    
    print()      
    print('El programa ha finalizado.')
    print()    
        
        
        

if __name__ == '__main__':
    main()










