from ArbolBinario import ABinario
from Nodo import Nodo
from PIla import Pila
class ABNormal(ABinario):
    def __init__(self):
        super().__init__()

    def llenar(self):
        r = Nodo()
        print('Ingrese el dato de la raiz')
        dato = int(input())
        r.setDato(dato)
        super().setR(r)
        nivel = Pila()
        su = Pila()
        nivel.adicionar(r)
        while not nivel.esVacia():
            while not nivel.esVacia():
                x = nivel.eliminar()
                res = int(input('Desea descendiente izquierdo de ' + str(x.getDato()) + ' Si=1  No<> 1 ?'))
                if res == 1:
                    w = Nodo()
                    print('Introduzca el dato izquierdo')
                    dato = int(input())
                    w.setDato(dato)
                    x.setIzq(w)
                    su.adicionar(x.getIzq())
                res = int(input('Desea descendiente derecho de ' + str(x.getDato()) + ' Si=1  No<> 1 ?'))
                if res == 1:
                    w = Nodo()
                    print('Introduzca el dato derecho')
                    dato = int(input())
                    w.setDato(dato)
                    x.setDer(w)
                    su.adicionar(x.getDer())
            nivel.vaciar(su)

    def m_nivel(self):
        super().m_nivel()

    def enorder(self,a):
        super().enorder(a)

    def posorden(self,a):
        super().posorden(a)
    def preorder(self,a):
        super().preorder(a)

    def alturaArbol(self):
        return super().alturaArbol()

