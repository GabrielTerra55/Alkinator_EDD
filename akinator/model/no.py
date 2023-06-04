class No:
    def __init__(self, valor):
        self.__valor = valor
        self.__esquerda = None
        self.__direita = None
        self.__pergunta = False
        self.__raiz = False
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def esquerda(self):
        return self.__esquerda
    
    @property
    def direita(self):
        return self.__direita
    
    @property
    def pergunta(self):
        return self.__pergunta

    @property
    def raiz(self):
        return self.__raiz
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @esquerda.setter
    def esquerda(self, esquerda):
        self.__esquerda = esquerda
    
    @direita.setter
    def direita(self, direita):
        self.__direita = direita
    
    @pergunta.setter
    def pergunta(self, pergunta):
        self.__pergunta = pergunta

    @raiz.setter
    def raiz(self, raiz):
        self.__raiz = raiz
