class Cliente:
    def __init__(self, nombre, apellido, documento, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.correo = correo
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDocumento: {self.documento}\nCorreo: {self.correo}"
        