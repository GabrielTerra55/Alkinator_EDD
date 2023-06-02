from akinator.model.no import No

class ArvoreAlkinator:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.raiz = self.__inserir_recursivamente(self.raiz, valor)

    def __inserir_recursivamente(self, no_atual, valor):
        pass
