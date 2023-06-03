from model.no import No


class ArvoreAkinator:
    def __init__(self):
        self.__raiz = None
    
    @property
    def raiz(self):
        return self.__raiz
    
    @raiz.setter
    def raiz(self, raiz):
        self.__raiz = raiz

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
            no_direcao.direita = No(animal_novo)
            return 
        raise Exception("Burro")
