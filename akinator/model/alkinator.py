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

    def inserir_pergunta_e_animais(self, no_direcao, pergunta, animal_novo):
        if isinstance(no_direcao, No):
            valor = no_direcao.valor
            no_direcao.valor = pergunta
            no_direcao.pergunta = True
            no_direcao.esquerda = No(valor)
            no_direcao.direita = No(animal_novo)
            return
