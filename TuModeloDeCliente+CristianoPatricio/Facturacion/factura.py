

class crear_factura:
    def __init__ (self,num_fac , total):
        self.num_fac = num_fac
        self.total = total 
        
        
    def __str__(self):
        return f"Factura nro {self.num_fac} - total USD: {self.total}"
    
