class TelaPrincipal:
    def mostra_msg(self, msg):
        print(msg)

    def menu(self):
        print('----- Bem vindo ao Akinator! -----')
        print('1. Começar')
        print('0. Encerrar')
        while True:
            try:
                escolha = int(input('Escolha a opção: '))
                return escolha
            except ValueError:
                print('Valor inválido!')
