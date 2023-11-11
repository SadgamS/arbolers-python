from Nodo import Nodo
from PIla import Pila


class ABinario(object):
    def __init__(self):
        self.raiz = None
    def getR(self):
        return self.raiz
    def setR(self,r):
        self.raiz=r
    def esVacia(self):
        if self.raiz is None:
            return True
        return False

    def m_nivel(self): #muestra los datos por nivel
        nivel=Pila()
        su=Pila()
        nivel.adicionar(self.raiz)
        while not nivel.esVacia():
            while not  nivel.esVacia():
                x=nivel.eliminar()
                print(str(x.getDato())+'\t',end="")
                if x.getIzq()!=None:
                    su.adicionar(x.getIzq())
                if x.getDer()!=None:
                    su.adicionar(x.getDer())
            nivel.vaciar(su)
            print()

    def enorder(self,a):
        if a == None:
            return None
        else:
            self.enorder(a.getIzq())
            print(a.getDato(),end=" ")
            self.enorder(a.getDer())

    def preorder(self,a):
        if a == None:
            return None
        else:
            print(a.getDato(),end=" ")
            self.preorder(a.getIzq())
            self.preorder(a.getDer())
    def posorden(self,a):
        if a == None:
            return None
        else:
            self.posorden(a.getIzq())
            self.posorden(a.getDer())
            print(a.getDato(),end=" ")



    def alturaArbol(self):
        alt=0
        nivel=Pila()
        su=Pila()
        nivel.adicionar(self.raiz)
        while not nivel.esVacia():
            while not nivel.esVacia():
                x=nivel.eliminar()
                if x.getIzq()!= None:
                    su.adicionar(x.getIzq())
                if x.getDer()!= None:
                    su.adicionar(x.getDer())
            nivel.vaciar(su)
            alt = alt+1
        return alt







