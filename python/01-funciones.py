def agregar_productos(codigo, descripcion, cantidad, precio, imagen, proveedor):
    
    if consultar_productos(codigo):
        return False
    
    nuevo_producto = { # Diccionario de datos
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor,
    }
    productos.append(nuevo_producto)
    return True

def consultar_productos(codigo):
    for producto in productos:
        if producto['codigo'] == codigo: # si es igual el producto existe
            return producto
    return False

# modificamos producto
def modificar_producto(codigo, nueva_descripcion, nueva_cantidad,
nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True
        return False
    
# funcion que tiene como objetivo mostrar un listado de productos
def listar_procuctos():
    print("-"*50)
    for producto in productos:
        print(f'Código.....: {producto["codigo"]}')
        print(f'Descripcion: {producto["descripcion"]}')
        print(f'Cantidad...: {producto["cantidad"]}')
        print(f'Precio.....: {producto["precio"]}')
        print(f'Imagen.....: {producto["imagen"]}')
        print(f'Proveedor..: {producto["proveedor"]}')
        print("-"*50)
        
#Función para eliminar producto específico de la lista de productos       
def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True
    return False



           
#---------------------------------------------------
#programa principal

# Definimos una lista (contendra diccionarios)
productos = []
# Agregamos productos
agregar_productos(1, 'Barras', 10, 5500, 'barra.jpg', 101)
agregar_productos(2, 'Discos', 13, 9500, 'discos.jpg', 101)
agregar_productos(3, 'Mancuernas', 15, 8000, 'mancuernas.jpg', 101)
agregar_productos(4, 'Bancos', 3, 15400, 'bancos.jpg', 102)
agregar_productos(5, 'EXtras', 3, 12450, 'extras.jpg', 102)
agregar_productos(6, 'Lockers', 4, 19500, 'lockers.jpg', 103)
agregar_productos(7, 'Soporte para mancuerdas', 12, 8700, 'soportemanc.jpg', 104)
agregar_productos(8, 'Soporte para discos y barras', 4, 14600, 'soportediscos.jpg', 104)

# consultamos un producto con su codigo:
cod_prod = int(input("Ingrese el codigo del producto: "))
producto = consultar_productos(cod_prod)
print(f'Resultado: {producto}')
if producto:
    print(f'Producto encontrado: {producto["codigo"]} - {producto["descripcion"]}')
else:
    print(f'Producto {cod_prod} no encontrado.')
    

# Listamos todos los productos
print("*********** LISTA DE PRODUCTOS ***********")
listar_procuctos()





   
