class Fraccion():
    __numerador = 0
    __denominador = 0


    def __init__(self, numerador = 0, denominador = 0):
        self.__numerador = int(numerador)
        self.__denominador = int(denominador)

    def setNumerador(self, numerador):
        self.__numerador = numerador

    def setDenominador(self, denominador):
        self.__denominador = denominador

    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador

    def crearFraccion(self, otraFraccion1):  
        if isinstance(otraFraccion1,Fraccion)==False:
            otraFraccion1 = Fraccion(otraFraccion1 , 1)
        return otraFraccion1

    
    def simplifica(self):
        numera=self.getNumerador()
        denomi=self.getDenominador()
        while numera % denomi != 0:
            mViejo = numera
            nViejo = denomi
            numera = nViejo
            denomi = mViejo % nViejo
        unaFraccion=Fraccion(self.getNumerador()//denomi,self.getDenominador()//denomi)
        return unaFraccion 

    def __str__(self):
        return str(f"{self.getNumerador()}/{self.getDenominador()}")

    def __add__ (self, otraFraccion):
        otraFraccion = self.crearFraccion(otraFraccion)
        numerador = (self.__numerador * otraFraccion.getDenominador()) + (otraFraccion.getNumerador() * self.__denominador)
        denominador = (self.__denominador * otraFraccion.getDenominador())
        return Fraccion(numerador, denominador)

    def __sub__ (self, otraFraccion):
        otraFraccion = self.crearFraccion(otraFraccion)
        numerador = (self.__numerador * otraFraccion.getDenominador()) - (otraFraccion.getNumerador() * self.__denominador)
        denominador = (self.__denominador * otraFraccion.getDenominador())
        return Fraccion(numerador, denominador)

 
    def __mul__ (self, otraFraccion):
        otraFraccion = self.crearFraccion(otraFraccion)
        numerador = self.__numerador * otraFraccion.getNumerador()
        denominador = (self.__denominador * otraFraccion.getDenominador())
        return Fraccion(numerador, denominador)

 
    def __truediv__(self, otraFraccion):
        otraFraccion = self.crearFraccion(otraFraccion)
        numerador = (self.__numerador * otraFraccion.getDenominador())
        denominador = (self.__denominador * otraFraccion.getNumerador())
        return Fraccion(numerador, denominador)





