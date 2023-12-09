const URL = "http://127.0.0.1:5000/";
// const URL = "https://maxifb.pythonanywhere.com/";


fetch(URL + 'productos')
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            // si hubo un error, lanzar explicitamente una excepcion
            // para ser "catcheada" mas adelante
            throw new Error('Error al obtener los productos.');
        }
    })
    .then(function (data) {
        let tablaProductos = document.getElementById('tablaProductos');

        for (let producto of data) {
            let fila = document.createElement('tr');
            fila.innerHTML = '<td>' + producto.codigo + '</td>' +
                '<td>' + producto.descripcion + '</td>' +
                '<td align="right">' + producto.cantidad + '</td>' +
                '<td align="right">' + producto.precio + '</td>' +
                // Corrige la URL de la imagen
                '<td><img src="./static/css/imagenes/' + producto.imagen_url + '" alt="Imagen del producto" style="width: 100px;"></td>';
 +
                '<td align="right">' + producto.proveedor + '</td>';
                // '<td><img src=https://www.pythonanywhere.com/user/maxifb/files/home/maxifb/mysite/img/' + producto.imagen_url + ' alt="Imagen del producto" style="width: 100px;"></td>' + '<td align="right">' + producto.proveedor + '</td>';
            
            //Una vez que se crea la fila con el contenido del producto, se agrega la
            //tabla utilizando el metodo appendchild del elemento tablaProductos.
            tablaProductos.appendChild(fila);
        }
    })
    .catch(function (error) {
        alert('Error al obtener los productos.');
        console.error('Error:', error);
    });
