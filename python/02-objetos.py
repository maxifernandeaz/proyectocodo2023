class Catalogo:
    productos = [] # Variable de clase
    
    def agregar_productos(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        
        if self.consultar_productos(codigo):
            return False
    
        nuevo_producto = { # Diccionario de datos
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor,
            }
        self.productos.append(nuevo_producto)
        return True
    
    def consultar_productos(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo: # si es igual el producto existe
                return producto
        return False
    
    def listar_procuctos(self):
        print()
        print("-"*50)
        for producto in self.productos:
            print(f'Código.....: {producto["codigo"]}')
            print(f'Descripcion: {producto["descripcion"]}')
            print(f'Cantidad...: {producto["cantidad"]}')
            print(f'Precio.....: {producto["precio"]}')
            print(f'Imagen.....: {producto["imagen"]}')
            print(f'Proveedor..: {producto["proveedor"]}')
            print("-"*50)
            
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
            return True
        return False 
    
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
            return False     
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_productos(codigo)
        if producto:
            print("-"*50)
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 50)
        else:
            print("Producto no encontrado.")
            
    
        
    
catalogo = Catalogo()
# Agregamos productos
catalogo.agregar_productos(1, 'Barras', 10, 5500, 'barra.jpg', 101)
catalogo.agregar_productos(2, 'Discos', 13, 9500, 'discos.jpg', 101)
catalogo.agregar_productos(3, 'Mancuernas', 15, 8000, 'mancuernas.jpg', 101)
catalogo.agregar_productos(4, 'Bancos', 3, 15400, 'bancos.jpg', 102)
catalogo.agregar_productos(5, 'EXtras', 3, 12450, 'extras.jpg', 102)
catalogo.agregar_productos(6, 'Lockers', 4, 19500, 'lockers.jpg', 103)
catalogo.agregar_productos(7, 'Soporte para mancuerdas', 12, 8700, 'soportemanc.jpg', 104)
catalogo.agregar_productos(8, 'Soporte para discos y barras', 4, 14600, 'soportediscos.jpg', 104)    
    
catalogo.listar_procuctos()   

catalogo.mostrar_producto(2)

 
