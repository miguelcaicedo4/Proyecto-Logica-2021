import random

class objetoCodificacion3D :
    def __init__ (self,Nf,Nc,COL,chrInit) :
        self.Nf = Nf
        self.Nc = Nc
        self.COL = COL
        self.chrInit = chrInit

    def codifica(self,f,c,col) :
        v1 = self.Nc * f + c
        return self.COL * v1 + col

    def decodifica(self,codigo):
        col = codigo % self.COL
        v1 = int(codigo / self.COL)
        c = v1 % self.Nc
        f = int(v1 / self.Nc)
        return f, c, col
    
    def P(self,f,c,col) :
        codigo = self.codifica(f,c,col)
        return chr(self.chrInit + codigo)
    
    def Pinv(self,codigo) :
        v = ord(codigo)-self.chrInit
        return self.decodifica(v)

Nfilas = 10
Ncolumnas = 10
Colores = ['Blanco' ,'Negro']


ResFila = []
ResColumna = []

def parametrosFila():
    ResFila.append(random.randint(0,10))
    if ResFila[0] < 8:
        ResFila.append(random.randint(0,ResFila[0]))
        if ResFila[0] + ResFila[1] > 10:
            del ResFila[:]
            parametrosFila()

def parametrosColumna():
    ResColumna.append(random.randint(0,10))
    if ResColumna[0] < 8:
        ResColumna.append(random.randint(0,ResColumna[0]))
        if ResColumna[0] + ResColumna[1] > 10:
            del ResColumna[:]
            parametrosColumna()






parametrosColumna()
parametrosFila()
print("Estos son los parametros columna")
print(ResColumna)
print("Estos son los parametros fila")
print(ResFila)





