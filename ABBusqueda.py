from Nodo import  Nodo
from PIla import  Pila
from ArbolBinario import ABinario

class ABBusqueda(ABinario):
    def __init__(self):
        super().__init__()

    def llenar(self):
        print('Ingrese Numero de elementos')
        n=int(input())
        print('Ingrese la raiz del arbol ')
        dr=int(input())
        x=Nodo(dr)
        super().setR(x)
        for i in range(n-1):
            dato=int(input('Ingrese un dato entero..'))
            x=Nodo(dato)
            y=super().getR()
            sw=0
            while sw==0:
                dx=int(x.getDato())
                dy=int(y.getDato())
                if dx<dy:
                    if y.getIzq()==None:
                        y.setIzq(x)
                        sw=1
                    else:
                        y=y.getIzq()
                else:
                    if y.getDer()==None:
                        y.setDer(x)
                        sw=1
                    else:
                        y=y.getDer()

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
    def insertar(self,y,ra):
        dar=int(ra.getDato())
        dy=int(y.getDato())
        if dy<dar:
            if ra.getIzq()==None:
                ra.setIzq(y)
            else:
                self.insertar(y,ra.getIzq())
        else:
            if ra.getDer() == None:
                ra.setDer(y)
            else:
                self.insertar(y,ra.getDer())

