import sys
from akinator.controller import controller_alkinator
class ControllerPrincipal:
    def __init__(self):
        self.__controller_alkinator = None
        self.__tela_principal = None

    @property
    def controller_arvore_b(self):
        return self.__controller_arvore_b

    @property
    def tela_principal(self):
        return self.__tela_principal

    def encerra_sistema(self):
        """
        Encerra o sistema

        Returns:
            Não retorna nada
        """
        self.tela_principal.sistema_encerrado()
        sys.exit(1)

    def inicializa_game(self):
        """
        Inicializa a partida de tictactoe

        Returns:
            Não retorna nada
        """
        self.__controller_tictactoe.disputar()

    def inicializa_controller_principal(self):
        """
        Inicia o menu de opções para o usuario

        Returns:
            funções definidas pelo usuario
        """
        lista_opcoes = {
            1: self.inicializa_game,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.tela_principal.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
