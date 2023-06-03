class ControllerAkinator:
    def __init__(self):
        self.__controller_principal = None
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
            questionamento = self.tela_akinator.pergunta(no.valor)
            if questionamento == 's':
                self.perguntar(no.direita) 
                   
            elif questionamento == 'n':
                self.perguntar(no.esquerda)
            
            else:
                raise Exception("resposta inválida")
        else:
            return no
        
    def jogar(self):
        no_animal = self.perguntar(self.akinator.raiz)
        questionamento = self.tela_akinator.perguntar_se_e_o_animal(no_animal.valor)
        if questionamento == 's':
            self.tela_akinator.fim()
        novo_animal = self.tela_akinator.recolhe_novo_animal()
        nova_pergunta = self.tela_akinator.recolhe_nova_pergunta()
        self.akinator.inserir_pergunta_e_animais(no_animal.esqueda, nova_pergunta, novo_animal)
        self.jogar()

        

# O animal entra a pergunra e o animal, precisa manter a pergunta antes de descer para o animal.
# ideia parecida com pe atras.
# não precisa ser o metodo de natural de uma inserção de arvore





