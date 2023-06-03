from akinator.model.no import No


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
            no_direcao.valor = pergunta
            no_direcao.pergunta = True
            no_direcao.esquerda = valor
            no_direcao.direita = animal_novo
            return 
