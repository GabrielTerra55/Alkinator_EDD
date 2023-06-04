from model.no import No
from model.alkinator  import ArvoreAkinator
from view.tela_akinator import TelaAkinator

from dao.dao_akinator import ArvoreAkinatorDao
class ControllerAkinator:
    def __init__(self, ctrl_princial):
        self.__controller_principal = ctrl_princial
        self.__akinator = ArvoreAkinatorDao()
        self.__tela_akinator = TelaAkinator()

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
                 return self.perguntar(no.direita) 
            elif questionamento == 'n':
                return self.perguntar(no.esquerda) #estourando aqui
            else:
                raise Exception("resposta inválida")
        else:
            return no

    def jogar(self):

        self.confere_se_vazio()
        teste = self.akinator.get_all()
        teste = list(teste)
        no_animal = self.perguntar(teste[0])
        animal = no_animal.valor
        questionamento = self.tela_akinator.perguntar_se_e_o_animal(animal) 

        if questionamento == 's':
            self.tela_akinator.fim() 
            return
        
        novo_animal = self.tela_akinator.recolhe_novo_animal() 
        nova_pergunta = self.tela_akinator.recolhe_nova_pergunta() 
        ArvoreAkinator.inserir_pergunta_e_animais(no_animal, nova_pergunta, novo_animal)
        self.jogar()

    def confere_se_vazio(self):
        raiz = self.akinator.get_all()
        if not raiz:
            self.criar_primeiro_valor()


    def criar_primeiro_valor(self):
        no_baleia = No('Baleia')
        #self.akinator.get_all().  = no_baleia
        self.akinator.add(0, no_baleia)