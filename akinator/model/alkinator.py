from akinator.model.no import No

class ArvoreBAlkinator:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.raiz = self.__inserir_recursivamente(self.raiz, valor)

    def __inserir_recursivamente(self, no_atual, valor):
        if no_atual.valor > valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                no_atual.esquerda = self.__inserir_recursivamente(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                no_atual.direita = self.__inserir_recursivamente(no_atual.direita, valor)
        
        if self.__is_cheio(no_atual):
            return self.__split(no_atual)
        
        return no_atual

    def excluir(self, valor):
        if self.raiz is None:
            return
        
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
                sucessor = self.__encontrar_menor_valor(no_atual.direita)
                no_atual.valor = sucessor.valor
                no_atual.direita = self.__excluir_recursivamente(no_atual.direita, sucessor.valor)

        if self.__is_desbalanceado(no_atual):
            return self.__merge(no_atual)
        
        return no_atual
    
    def __split(self, no):
        filho_esquerda = No(no.esquerda.valor)
        filho_direita = No(no.direita.valor)
        
        if no.esquerda.esquerda is not None:
            filho_esquerda.esquerda = no.esquerda.esquerda
            filho_direita.esquerda = no.esquerda.direita
        else:
            filho_esquerda.esquerda = no.direita.esquerda
            filho_direita.esquerda = no.direita.direita
        
        no.valor = no.direita.valor
        no.esquerda = filho_esquerda
        no.direita = filho_direita
        
        return no

    def __merge(self, no):
        if no.esquerda is None or no.direita is None:
            return no
        
        if no.esquerda.esquerda is None and no.direita.esquerda is None:
            no.valor = no.esquerda.valor
            no.esquerda = None
            no.direita = None
        else:
            if no.esquerda.esquerda is None:
                no.valor = no.direita.esquerda.valor
                no.esquerda = None
                no.direita.esquerda = None
            else:
                no.valor = no.esquerda.esquerda.valor
                no.direita = None
                no.esquerda.esquerda = None
        
        return no

    def __is_cheio(self, no):
        return no.esquerda is not None and no.direita is not None
    
    def __is_desbalanceado(self, no):
        return no.esquerda is not None and no.direita is not None and (no.esquerda.esquerda is not None or no.direita.esquerda is not None)

    def __encontrar_menor_valor(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual