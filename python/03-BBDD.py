import mysql.connector


class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS productos (codigo INT,
                            descripcion VARCHAR(255) NOT NULL,
                            cantidad INT(4) NOT NULL,
                            precio DECIMAL(10, 2) NOT NULL,
                            imagen_url VARCHAR(255),
                            proveedor INT(2))""")
        self.conn.commit()
        
    def agregar_productos(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
    
    # verificamos si ya existe un producto con el mismo código
       self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
       producto_existe = self.cursor.fetchone()
       if producto_existe:
        return False
    
    # si no existe, agregamos el nuevo producto a la tabla
       sql = f"INSERT INTO productos (codigo, descripcion, cantidad, precio, imagen_url, proveedor) VALUES ({codigo}, '{descripcion}', {cantidad}, {precio}, '{imagen}', {proveedor})"
       self.cursor.execute(sql)
       self.conn.commit()
       return True
    
    def consultar_producto(self, codigo):
        # consultamos un producto a partir de su codigo
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = f"UPDATE productos SET descripcion = '{nueva_descripcion}', cantidad = {nueva_cantidad}, precio = {nuevo_precio}, imagen_url = '{nueva_imagen}', proveedor = {nuevo_proveedor} WHERE CODIGO = {codigo}"
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su códigoproducto = self.consultar_productos(codigo)
        producto = self.consultar_producto(codigo)
        if producto:
            print("-"*50)
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 50)
        else:
            print("Producto no encontrado.")
            
    def listar_productos(self):
        # Mostramos en pantalla un listado de todos los productos en la tabla
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        print("-" * 50)
        for producto in productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 50)
            
    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

# ---------------------------------------------------------------
# Programa principal

catalogo = Catalogo(host="localhost", user="root", password="", database="miapp")

catalogo.agregar_productos(1, 'Barras', 10, 5500, 'barra.jpg', 101)
catalogo.agregar_productos(2, 'Discos', 13, 9500, 'discos.jpg', 101)
catalogo.agregar_productos(3, 'Mancuernas', 15, 8000, 'mancuernas.jpg', 101)
catalogo.agregar_productos(4, 'Bancos', 3, 15400, 'bancos.jpg', 102)
catalogo.agregar_productos(5, 'EXtras', 3, 12450, 'extras.jpg', 102)
catalogo.agregar_productos(6, 'Lockers', 4, 19500, 'lockers.jpg', 103)
catalogo.agregar_productos(7, 'Soporte para mancuerdas', 12, 8700, 'soportemanc.jpg', 104)
catalogo.agregar_productos(8, 'Soporte para discos y barras', 4, 14600, 'soportediscos.jpg', 104) 

# cod_prod = int(input("Ingrese el codigo del producto: "))
# producto = catalogo.consultar_producto(cod_prod)

# if producto:
#     print(f'Producto encontrado: {producto["codigo"]} - {producto["descripcion"]}')
# else:
#     print(f'Producto {cod_prod} no encontrado.')
    
# catalogo.mostrar_producto(2)
# catalogo.modificar_producto(2, 'Discos 10 Kg', 9, 10500, 'discos.jpg', 101)
# catalogo.mostrar_producto(2)

catalogo.listar_productos()

