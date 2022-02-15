import PySimpleGUI as sg
import SistemaChatBotController
# View do padrão MVC


class SistemaChatBotView():
    def __init__(self, controlador, bot):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window(
            "Sistema Chat Bot", self.__container, font=("Helvetica", 14))
        self.__bot = bot

    def tela_chatbot(self):
        sg.theme('Dark Brown 1')

        self.__container = [
            [sg.Text('')],
            # botões com os comandos do BOT
            for comando in self.__bot.comandos:
                [sg.Button(comando.comando)]
            # no controller: ele detecta o comando pelo comando.comando e me passa a resposta via pega_resposta no mostra_resultado
            # area de resposta do bot
            [sg.Text('', key='resposta', size=(50, 1))]
        ]

        self.__window = sg.Window(
            "Sistema Chat Bot", self.__container, font=("Helvetica", 14))

    def mostra_resultado(self, resposta):
        self.__window.Element('resposta').Update(resposta)

    def limpa_lacuna(self, key):
        self.__window.Element(key).Update('')

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
