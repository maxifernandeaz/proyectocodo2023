//const URL = "http://127.0.0.1:5000/";
const URL = "https://maxifb.pythonanywhere.com/";

const app = Vue.createApp({
    data() {
        return {
            codigo: '',
            descripcion: '',
            cantidad: '',
            precio: '',
            proveedor: '',
            imagen_url: '',
            imagenSeleccionada: null,  // Agregamos esta línea para definir la propiedad imagenSeleccionada
            imagenUrlTemp: null,
            mostrarDatosProducto: false,
        };
    },

    methods: {
        obtenerProducto() {
            fetch(URL + 'productos/' + this.codigo)
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        throw new Error('Error al obtener los datos del producto.');
                    }
                })

                .then(data => {
                    this.descripcion = data.descripcion;
                    this.cantidad = data.cantidad;
                    this.precio = data.precio;
                    this.proveedor = data.proveedor;
                    this.imagen_url = data.imagen_url;
                    this.mostrarDatosProducto = true;
                })
                .catch(error => {
                    console.log(error);
                    alert('Código no encontrado.');
                });
        },
        seleccionarImagen(event) {
            const file = event.target.files[0];
            this.imagenSeleccionada = file;
            this.imagenUrlTemp = URL.createObjectURL(file); // Crea una URL temporal para la vista previa
        },
        guardarCambios() {
            const formData = new FormData();
            formData.append('codigo', this.codigo);
            formData.append('descripcion', this.descripcion);
            formData.append('cantidad', this.cantidad);
            formData.append('proveedor', this.proveedor);
            formData.append('precio', this.precio);
            if (this.imagenSeleccionada) {
                formData.append('imagen', this.imagenSeleccionada, this.imagenSeleccionada.name);
            }

            // Utilizamos fetch para realizar una solicitud PUT a la API y guardar los cambios.
            fetch(URL + 'productos/' + this.codigo, {
                method: 'PUT',
                body: formData,
                mode: 'cors'  // Agrega este encabezado
            })
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error('Error al guardar los cambios del producto.');
                    }
                })
                .then(data => {
                    alert('Producto actualizado correctamente.');
                    this.limpiarFormulario();
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al actualizar el producto.');
                });
        },

        limpiarFormulario() {
            this.codigo = '';
            this.descripcion = '';
            this.cantidad = '';
            this.precio = '';
            this.imagen_url = '';
            this.imagenSeleccionada = null;
            this.imagenUrlTemp = null;
            this.mostrarDatosProducto = false;
        }
    }
});

app.mount('#app');


