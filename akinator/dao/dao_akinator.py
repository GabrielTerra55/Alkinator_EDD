from dao.dao import Dao
from model.no import No

class ArvoreAkinatorDao(Dao):
    def __init__(self):
        super().__init__('ArvoreAkinator.pkl')

    def add(self, key, no: No):
        super().add(key, no)

    def get(self, key):
        super().get(key)

    def remove(self, key):
        super().remove(key)

    def save(self):
        super().save()
