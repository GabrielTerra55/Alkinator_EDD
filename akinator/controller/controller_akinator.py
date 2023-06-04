from model.no import No
from model.alkinator  import ArvoreAkinator
from view.tela_akinator import TelaAkinator
from dao.dao_akinator import ArvoreAkinatorDao

class ControllerAkinator:
    def __init__(self, ctrl_princial):
        self.__controller_principal = ctrl_princial
        self.__akinator = ArvoreAkinator()
        self.__tela_akinator = TelaAkinator()
        self.__nos = ArvoreAkinatorDao()

    @property
    def controller_principal(self):
        return self.__controller_principal

    @property
    def akinator(self):
        return self.__akinator

    @property
    def tela_akinator(self):
        return self.__tela_akinator

    @property
    def nos(self):
        return self.__nos

    def perguntar(self, no): 
        if no.pergunta:
            pergunta = no.valor
            questionamento = self.tela_akinator.perguntar(pergunta) 
            if questionamento == 's':
                return self.perguntar(no.direita)
            elif questionamento == 'n':
                return self.perguntar(no.esquerda)
            else:
                raise Exception("resposta inválida")
        else:
            return no 

    def jogar(self):
        if len(self.nos.get_all()) == 0:
            self.criar_primeiro_valor()
        nos = self.nos.get_all()
        for i in nos:
            if isinstance(i, No):
                if i.raiz is True:
                    self.akinator.raiz = i
        no_animal = self.perguntar(self.akinator.raiz)
        animal = no_animal.valor
        questionamento = self.tela_akinator.perguntar_se_e_o_animal(animal) 

        if questionamento == 's':
            self.tela_akinator.fim() 
            return
        
        novo_animal = self.tela_akinator.recolhe_novo_animal() 
        nova_pergunta = self.tela_akinator.recolhe_nova_pergunta() 
        self.akinator.inserir_pergunta_e_animais(no_animal, nova_pergunta, novo_animal)
        self.nos.add(novo_animal, novo_animal)
        self.nos.add(nova_pergunta, nova_pergunta)
        self.jogar()
        self.nos.save()

    def criar_primeiro_valor(self):
        no_baleia = No('Baleia')
        no_baleia.raiz = True
        self.akinator.raiz = no_baleia
        self.nos.add(no_baleia, no_baleia)
