#Clase que representa un documento a imprimir
class Documento:
    def __init__(self, nombre, usuario, paginas):   #Nombre del documento, usuario y num de pag
        self.nombre = nombre      
        self.usuario = usuario    
        self.paginas = paginas    

#Clase Nodo para la cola de impresión
class Nodo:
    def __init__(self, documento):   
        self.documento = documento    #Contiene un objeto Documento
        self.siguiente = None         #Apunta al siguiente 