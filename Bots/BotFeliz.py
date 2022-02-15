from Bots.Bot import Bot
from Bots.Comando import Comando


class BotFeliz(Bot):
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__comandos = [
            Comando('Oláa!!', 'Oi! Que dia lindo, não é mesmo?!'),
            Comando('Como você está? :)', 'Estou maravilhosamente feliz!!'),
            Comando('Pode me ajudar?', 'Claro que posso! Será um prazer!'),
            Comando('Tchau', 'Até mais, tenha um bom dia! ')
        ]
        self.__comando_erro = 'Digite um comando válido para eu conseguir te responder!'

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def comando_erro(self):
        return self.__comando_erro

    def apresentacao(self):
        return f'Meu nome é {self.__nome}! Prazer em conhece-lo!'

    def boas_vindas(self):
        return f'Que bom que você me escolheu!'

    def despedida(self):
        return f'Que pena que você já vai embora, até a próxima!'
