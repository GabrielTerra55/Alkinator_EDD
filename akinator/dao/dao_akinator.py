from dao.dao import Dao
from model.alkinator import ArvoreAkinator

class ArvoreAkinatorDao(Dao):
    def __init__(self):
        super().__init__('ArvoreAkinator.pkl')

    def add(self,key, arvore_akinator: ArvoreAkinator):
        super().add(key, arvore_akinator)
    #(funcionario.cracha, funcionario)
    def get(self, key):
        super().get(key)

    def remove(self, key):
        super().remove(key)
