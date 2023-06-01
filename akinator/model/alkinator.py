from akinator.model.no import No

class ArvoreBAlkinator:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.__inserir_recursivamente(self.raiz, valor)

    def __inserir_recursivamente(self, no_atual, valor):
        if no_atual.valor > valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self.__inserir_recursivamente(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self.__inserir_recursivamente(no_atual.direita, valor)

    def excluir(self, valor):
        self.raiz = self.__excluir_recursivamente(self.raiz, valor)

    def __excluir_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self.__excluir_recursivamente(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self.__excluir_recursivamente(no_atual.direita, valor)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            else:
                menor_valor = self.__encontrar_menor_valor(no_atual.direita)
                no_atual.valor = menor_valor.valor
                no_atual.direita = self.__excluir_recursivamente(no_atual.direita, menor_valor.valor)

        return no_atual

    def __encontrar_menor_valor(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual