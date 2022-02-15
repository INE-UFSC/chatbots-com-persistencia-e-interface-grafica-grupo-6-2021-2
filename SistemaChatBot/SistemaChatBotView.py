import PySimpleGUI as sg
from SistemaChatBot.BaseView import BaseView
# import SistemaChatBotController
# View do padrão MVC


class SistemaChatBotView(BaseView):
    def __init__(self, controlador, bot):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window(
            "Sistema Chat Bot", self.__container, font=("Helvetica", 14))
        self.__bot = bot

    def tela_chatbot(self):
        sg.theme('Dark Brown 1')
        for comando in self.__bot.comandos:
            self.__container.append([sg.Button(comando.comando)])

        self.__container.append([sg.Text('', key='resposta', size=(50, 1))])

        self.__container.append([sg.Button('Exportar'), sg.Button('Importar')])

        self.update_layout(self.__container)

    def mostra_resultado(self, resposta):
        self.__window.Element('resposta').Update(resposta)

    def limpa_lacuna(self, key):
        self.__window.Element(key).Update('')

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
