class ControllerAkinator:
    def __init__(self, ctrl_princial):
        self.__controller_principal = ctrl_princial
        self.__akinator = None
        self.__tela_akinator = None

    @property
    def controller_principal(self):
        return self.__controller_principal

    @property
    def akinator(self):
        return self.__akinator

    @property
    def tela_akinator(self):
        return self.__tela_akinator

    def perguntar(self, no): 
        if no.pergunta:
            pergunta = no.valor
            questionamento = self.tela_akinator.perguntar(pergunta) 
            if questionamento == 's':
                self.perguntar(no.direita) 
            elif questionamento == 'n':
                self.perguntar(no.esquerda)
            else:
                raise Exception("resposta inválida")
        else:
            return no # tem que retornar o no anterio

    def jogar(self):
        no_animal = self.perguntar(self.akinator.raiz)
        animal = no_animal.valor
        questionamento = self.tela_akinator.perguntar_se_e_o_animal(animal) 
        if questionamento == 's':
            self.tela_akinator.fim() 
            return
        novo_animal = self.tela_akinator.recolhe_novo_animal() 
        nova_pergunta = self.tela_akinator.recolhe_nova_pergunta() 
        self.akinator.inserir_pergunta_e_animais(no_animal, nova_pergunta, novo_animal)
        self.jogar()
