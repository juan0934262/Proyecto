class Product:
    def __init__(self, Nombre, Contraseña):
        self.Nombre = Nombre
        self.Password = Contraseña
        
    def toDBCollection(self):
        return{
            'name': self.Nombre,
            'password': self.Password,
            }