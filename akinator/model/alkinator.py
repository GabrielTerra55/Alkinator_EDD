from akinator.model.no import No
'''from akinator.model.animal import Animal
from akinator.model.pergunta import Pergunta'''


class ArvoreAkinator:
    def __init__(self):
        self.__raiz = None

    def inserir(self, valor):
        if self.__raiz is None:
            self.__raiz = No(valor)
        else:
            self.inserir_recursivamente(self.__raiz, valor)


    def inserir_pergunta_e_animais(self, no_direcao, pergunta, animal_novo):
        if isinstance(no_direcao, No):
            valor = no_direcao.valor  #recebe o animal que estava presente no nó
            no_direcao = pergunta
            no_direcao.pergunta = True
            no_direcao.esquerda = valor
            no_direcao.direita = animal_novo
            return no_direcao
    
            
            
            '''if valor is True:
                if no_atual.direita is None:
                    no_atual.direita = Animal(valor)
                else:
                    self.inserir_recursivamente(no_atual, valor)
            if valor is False:
                if no_atual.esquerda is None:
                    no_atual.esquerda = No(valor)
                else:
                    self.inserir_recursivamente(no_atual, valor)'''

    def inserir_animal(self, no_atual, nome):
        if isinstance(no_atual, Pergunta):
            if valor is True:
                if no_atual.direita is None:
                    no_atual.direita = Animal(nome)
                else:
                    self.inserir_recursivamente(no_atual, nome)
            if valor is False:
                if no_atual.esquerda is None:
                    no_atual.esquerda = No(nome)
                else:
                    self.inserir_recursivamente(no_atual, nome)
