from abc import ABC

class No(ABC):
    def __init__(self, valor):
        self.__valor = valor
        self.__esquerda = None
        self.__direita = None
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def esquerda(self):
        return self.__esquerda
    
    @property
    def direita(self):
        return self.__direita
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @esquerda.setter
    def esquerda(self, esquerda):
        self.__esquerda = esquerda
    
    @direita.setter
    def direita(self, direita):
        self.__direita = direita
