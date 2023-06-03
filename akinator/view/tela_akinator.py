class TelaAkinator:
    def perguntar(self, pergunta):
        print(20 * '*')
        resposta = input(f"{pergunta}?[s/n] ")
        print(20 * '*')
        return resposta

    def perguntar_se_e_o_animal(self, animal):
        print(20 * '*')
        resposta = input(f"você pensou {animal}?[s/n] ")
        print(20 * '*')
        return resposta

    def fim(self):
        print(20 * '*')
        print('========== Fim de Jogo ==========')
        print(20 * '*')
    
    def recolhe_novo_animal(self):
        print(20 * '*')
        resposta = input("qual o animal que você pensou?[s/n]")
        print(20 * '*')
        return resposta
    
    def recolhe_nova_pergunta(self):
        print(20 * '*')
        resposta = input(" o que difere o animal que você pensou do animal indicado? ")
        print(20 * '*')
        return resposta