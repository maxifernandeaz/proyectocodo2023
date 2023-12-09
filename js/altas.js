const URL = "http://127.0.0.1:5000/";
// const URL = "https://maxifb.pythonanywhere.com/";

// Capturamos el evento de envío del formulario
document.getElementById('formulario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitamos que se envíe el formulario
    var formData = new FormData();
    formData.append('codigo', document.getElementById('codigo').value);
    formData.append('descripcion', document.getElementById('descripcion').value);
    formData.append('cantidad', document.getElementById('cantidad').value);
    formData.append('precio', document.getElementById('precio').value);
    formData.append('imagen', document.getElementById('imagenProducto').files[0]);
    formData.append('proveedor', document.getElementById('proveedorProducto').value);
    // Realizamos la solicitud POST al servidor
    fetch(URL + 'productos', {
        method: 'POST',
        body: formData // Aquí enviamos formData en lugar de JSON
    })
        // Después de realizar la solicitud POST, se utiliza el método then() para manejar la respuesta del servidor.
    .then(function (response) {
        if (response.ok) {
            return response.json(); // Aquí esperamos la respuesta JSON
        } else {
            // Si hubo un error, lanzar explícitamente una excepción
            // para ser "catcheada" más adelante
            throw new Error('Error al agregar el producto.');
        }
    })
        // Manejamos la respuesta JSON en este paso
    .then(function () {
            // En caso de éxito, mostramos el mensaje de alerta con el mensaje del servidor
        alert('Producto agregado correctamente');
    })
    .catch(function (error) {
            // En caso de error
        alert('Error al agregar el producto.');
        console.error('Error:', error);
    })
    .finally(function () {
            // Limpiar el formulario en ambos casos (éxito o error)
        document.getElementById('codigo').value = "";
        document.getElementById('descripcion').value = "";
        document.getElementById('cantidad').value = "";
        document.getElementById('precio').value = "";
        document.getElementById('imagenProducto').value = "";
        document.getElementById('proveedorProducto').value = "";
        });
});

