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
            return no.valor
        
    def jogar(self):
        animal = self.perguntar(self.akinator.raiz)
        self.tela_akinator.perguntar_se_e_o_animal()
        
        self.tela_akinator.fim()

# O animal entra a pergunra e o animal, precisa manter a pergunta antes de descer para o animal.
# ideia parecida com pe atras.
# não precisa ser o metodo de natural de uma inserção de arvore





