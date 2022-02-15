from DAO import DAO
from SistemaChatBot.SistemaChatBot import SistemaChatBot

class SistemaChatBotDAO(DAO):
    def __init__(self, datasource = 'sistema_chat_bot.pkl'):
        super().__init__(datasource)

    def add(self, sistemaChatBot: SistemaChatBot):
        if ((SistemaChatBot is not None)
                and (isinstance(sistemaChatBot.id, int))
                and (isinstance(sistemaChatBot, SistemaChatBot))):
            return super().add(sistemaChatBot.id, sistemaChatBot)
   
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def find(self, nome: str):
        for chave, cliente in super().get_all():
            if cliente.nome == nome:
                return chave
        raise KeyError

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)