class TelaAkinator:
    def perguntar(self, pergunta):
        print(20 * '*')
        resposta = input(f"{pergunta}?[s/n] ")
        return resposta

    def perguntar_se_e_o_animal(self, animal):
        print(20 * '*')
        resposta = input(f"Você pensou {animal}?[s/n] ")
        return resposta

    def fim(self):
        print(20 * '*')
        print('========== Fim de Jogo ==========')
    
    def recolhe_novo_animal(self):
        print(20 * '*')
        resposta = input("Qual o animal que você pensou? ")
        return resposta
    
    def recolhe_nova_pergunta(self):
        print(20 * '*')
        resposta = input("O que difere o animal que você pensou do animal indicado (OBS: fale a caracteristica que o difere ex: voa)? ")
        return resposta
