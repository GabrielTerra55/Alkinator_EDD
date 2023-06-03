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
    
    def perguntar(self, pergunta): #pergunta é o nó
        questionamento = self.tela_akinator.pergunta(pergunta.pergunta)
        if questionamento == 's':
            if None: # verificar se o valor a direita é uma pergunta
                # se sim manda o nopergunta pra a função perguntar de novo
                pass
            else:
                ajax = 'ajax'
                # acesso a resposta e retorno para o usuario
        else:
            # pegar a resposta, transformar em um noresposta e instanciar o animal em um de seus lados
            pass
        self.tela_akinator.fim()

# O animal entra a pergunra e o animal, precisa manter a pergunta antes de descer para o animal.
# ideia parecida com pe atras.
# não precisa ser o metodo de natural de uma inserção de arvore





