class Pila:
    def __init__(self):
        self.val=[]

    def esVacia(self):
        if len(self.val)==0:
            return True
        else:
            return False
    def eliminar(self):
        if self.esVacia():
            return None
        else:
            return self.val.pop()
    def mostrar(self):
        print(self.val)
    def adicionar(self, dato):
        self.val.append(dato)
    def vaciar(self,b):
        while not b.esVacia():
            self.adicionar(b.eliminar())

