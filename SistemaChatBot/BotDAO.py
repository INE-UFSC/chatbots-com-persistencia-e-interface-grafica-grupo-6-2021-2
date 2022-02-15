from DAO import DAO
from Bots.Bot import Bot

class BotDAO(DAO):
    def __init__(self, datasource = 'bots.pkl'):
        super().__init__(datasource)

    def add(self, bot: Bot):
        if ((bot is not None)
                and (isinstance(bot.id, int))
                and (isinstance(bot, Bot))):
            return super().add(bot.id, bot)
   
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