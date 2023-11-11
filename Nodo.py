class Nodo:
    def __init__(self, dato=None):
        self.dato=dato
        self.izq=None
        self.der=None

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato=dato

    def getIzq(self):
        return self.izq

    def setIzq(self, izq):
        self.izq =izq

    def getDer(self):
        return self.der

    def setDer(self, der):
        self.der = der


