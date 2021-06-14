from Fraccion import Fraccion
from tkinter import *
from tkinter import ttk
from functools import partial
import tkinter as tk

class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)


        '''modificaciones visuales'''

        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=3, row=7, sticky=W)    
        ttk.Button(mainframe, text='DEL', command=self.borrarPanel2).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerNUMERO, "/")).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, text='REAL', command=partial(self.ponerOPERADOR,'REAL')).grid(column=3, row=8, sticky=W)
      
        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            numerador, denominador = valor.split('/')
            fraccion = Fraccion(int(numerador), int(denominador))
            self.__fraccionPrimera = fraccion
            self.__panel.set(numero)
            
    def borrarPanel(self):
        self.__panel.set('')

    def resolverOperacion(self, fraccion1, operacion, fraccion2):
        resultado = ''
        if operacion=='+':
            resultado=fraccion1+fraccion2
        else:
            if operacion=='-':
                resultado=fraccion1-fraccion2
            else:
                if operacion=='*':
                    resultado=fraccion1*fraccion2
                else:
                    if operacion=='%':
                        resultado=fraccion1/fraccion2
        if isinstance(resultado,Fraccion):
          resultado = resultado.simplifica()

        self.__panel.set(str(resultado))


    def ponerOPERADOR(self, op):
        if op == '=':
            operacion = self.__operador.get()
            valor = self.__panel.get()
            num, den = valor.split('/')
            fraccion2 = Fraccion(int(num), int(den))
            self.__fraccionSegunda = fraccion2
            self.resolverOperacion(self.__fraccionPrimera, operacion, self.__fraccionSegunda)
            self.__operador.set('')
            self.__operadorAux=None
        elif op=='REAL':
            self.__operador.set('Real')
            valor = self.__panel.get()
            numerador, denominador = valor.split('/')
            real=float(numerador)/float(denominador)
            self.__panel.set(float(real))  

    
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion = self.__operador.get()
                self.__fraccionSegunda = int(self.__panel.get())
                self.resolverOperacion(self.__fraccionPrimera, operacion, self.__fraccionSegunda)
                self.__operador.set(op)
                self.__operadorAux=op
   
  
    def borrarPanel2(self):
        self.__panel.set('')
        self.__operador.set('')
        self.__operadorAux=None