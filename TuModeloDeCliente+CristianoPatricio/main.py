# importamos todo lo que vamos a utilizar en la compra 
from Cliente.cliente import Cliente
from Producto.Producto import Producto
from Facturacion.factura import crear_factura

def main():
    # Crearmos productos que el cliente va a comprar
    producto1 = Producto("Laptop", 1000)
    producto2 = Producto("Teclado", 50)
    producto3 = Producto("Mouse", 30)

    # Crear un cliente
    cliente1 = Cliente ("Patricio","Cristiano","29479919", "patricioecristiano@gmail.com")

    # Agregar productos al carrito del cliente
    cliente1.agregar_producto(producto1)
    cliente1.agregar_producto(producto2)
    cliente1.agregar_producto(producto3)
        
    # Sumamoas el total de la compra
    total = sum(producto.precio for producto in cliente1.carrito)
        
    # Crear factura para el cliente
    num_fac = "23-123" 
    factura = crear_factura(num_fac, total)
        
        
    # Mostrar información del cliente y su carrito 
    print("************************************")
    print(f"Cliente:\n{cliente1}")
    print("************************************")
    print(factura)
    print("************************************")
    print("COMPRAS DEL CLIENTE")  
    for producto in cliente1.carrito:
        print(producto)
    print("************************************")    
    print("TOTAL DE LA COMPRA: USD ",total )
    print("************************************")
    
if __name__ == "__main__":
    main()


"""def main():
    # Crearmos productos que el cliente va a comprar
    producto1 = Producto("Laptop", 1000)
    producto2 = Producto("Teclado", 50)
    producto3 = Producto("Mouse", 30)

    # Crear un cliente
    cliente1 = Cliente ("Patricio","Cristiano","29479919", "patricioecristiano@gmail.com")

    # Agregar productos al carrito del cliente
    cliente1.agregar_producto(producto1)
    cliente1.agregar_producto(producto2)
    cliente1.agregar_producto(producto3)
        
    # Sumamoas el total de la compra
    total = sum(producto.precio for producto in cliente1.carrito)
        
    # Crear factura para el cliente
    num_fac = "23-123" 
    factura = crear_factura(num_fac, total)
        
        
    # Mostrar información del cliente y su carrito 
    print("************************************")
    print(f"Cliente:\n{cliente1}")
    print("************************************")
    print(factura)
    print("************************************")
    print("COMPRAS DEL CLIENTE")  
    for producto in cliente1.carrito:
        print(producto)
    print("************************************")    
    print("TOTAL DE LA COMPRA: USD ",total )
    print("************************************")
    
if __name__ == "__main__":
    main()"""