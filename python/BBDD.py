import mysql.connector

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT(4) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(2))''')
        self.conn.commit()

    def agregar_producto(self, codigo, descripcion, cantidad, precio,
    imagen, proveedor):
        # Verificamos si ya existe un producto con el mismo código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo ={codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
            return False
        # Si no existe, agregamos el nuevo producto a la tabla
        sql = f"INSERT INTO productos \
    (codigo, descripcion, cantidad, precio, imagen_url,proveedor) \
    VALUES \
    ({codigo}, '{descripcion}', {cantidad}, {precio},'{imagen}', {proveedor})"
        self.cursor.execute(sql)
        self.conn.commit()
        return True

# Programa principal
catalogo = Catalogo(host='localhost', user='root', password='',
database='miapp')
