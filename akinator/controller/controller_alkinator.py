class ControllerAkinator:
    def __init__(self):
        self.__controller_principal = None
        self.__alkinator = None
        self.__tela_alkinator = None

    @property
    def controller_principal(self):
        return self.__controller_principal

    @property
    def alkinator(self):
        return self.__alkinator

    @property
    def tela_alkinator(self):
        return self.__tela_alkinator
    
    def jogar(self):
        self.tela_alkinator.pensar_em_um_animal()
        while True:
            pergunta = self.alkinator
