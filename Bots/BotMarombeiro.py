from Bots.Bot import Bot
from Bots.Comando import Comando


class BotMarombeiro(Bot):
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__comandos = [
            Comando("Eai frango",
                    "Frango é tu rapaz, tem nem 40 de braço, ta doido!?!"),
            Comando("Me passa um treino?",
                    "3x10 supino\n3x10 barra fixa\n3x10 rosca direta\n3x10 tríceps testa\n(perna não precisa)"),
            Comando(
                "Conselho", "Quer ficar grande? Tem que comer e treinar todo dia!")
        ]
        self.__comando_erro = "Ah isso eu não sei..."

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def comando_erro(self):
        return self.__comando_erro

    def apresentacao(self):
        return "Treino e dieta eu não furo, tá ligado?"

    def boas_vindas(self):
        return "HORA DO SHOW P****!"

    def despedida(self):
        return "Valeu mermão, até a próxima."
