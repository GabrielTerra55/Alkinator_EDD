import sys
from controller_akinator import ControllerAkinator
from tela_principal import TelaPrincipal


class ControllerPrincipal:
    def __init__(self):
        self.__controller_akinator = ControllerAkinator(self)
        self.__tela_principal = TelaPrincipal()

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
        self.tela_principal.mostra_msg('Programa Encerrado.')
        sys.exit(1)

    def inicializa_game(self):
        """
        Inicializa a partida de tictactoe

        Returns:
            Não retorna nada
        """
        self.__controller_akinator.jogar()

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
            opcao_escolhida = self.tela_principal.menu()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
