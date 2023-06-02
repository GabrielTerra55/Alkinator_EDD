from akinator.model.no import No


class ArvoreAkinator:
    def __init__(self):
        self.__raiz = None

    def inserir(self, valor):
        if self.__raiz is None:
            self.__raiz = No(valor)
        else:
            self.inserir_recursivamente(self.__raiz, valor)

    def inserir_recursivamente(self, no_atual, valor):
        if no_atual.pergunta is True:
            if valor is True and no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self.inserir_recursivamente(no_atual, valor)
