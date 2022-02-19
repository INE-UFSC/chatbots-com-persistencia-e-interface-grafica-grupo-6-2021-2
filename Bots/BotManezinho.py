from Bots.Bot import Bot
from Bots.Comando import Comando


class BotManezinho(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = [
            Comando("Ô meu querido, quesh saber quantas praias existem na nossa linda ilha da magia?",
                    "A nossa belíssima ilha conta com incríveis 42 praias!"),
            Comando("Essa é complicada, Avaí ou Figueira?",
                    "Furacão ou Leão? Essa é difícil hein!"),
            Comando("Mofas com a pomba na balaia?",
                    "Ô meu querido, isso significa que a pessoa não vai alcançar o seu objetivo, tendesse?"),
            Comando("O que é bucica?",
                    "Bucica é como a gente chama as nossas cadelinhas aqui da ilha!")
        ]
        self.__comando_erro = "Uhhh seu tanso! Não é assim não, pô!"

    @property
    def comandos(self):
        return self.__comandos

    @property
    def comando_erro(self):
        return self.__comando_erro

    def apresentacao(self):
        return f"Ó-lhó-lhó, me chamo {self.__nome}. Quex conversar comigo?"

    def boas_vindas(self):
        return "Me excolhesse mesmo, és um baita, feio!"

    def despedida(self):
        return "Valeu pelo papo, nego, dazumbanho! Agora segue reto toda vida que eu vou me ajojar aqui"
