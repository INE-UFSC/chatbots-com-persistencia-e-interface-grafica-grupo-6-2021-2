import PySimpleGUI as sg
from SistemaChatBot.BaseView import BaseView
# import SistemaChatBotController
# View do padrão MVC


class SistemaChatBotView(BaseView):
    def __init__(self, controlador, bot):
        self.__controlador = controlador
        self.__bot = bot
        self.__container = []
        self.__title = f'Sistema Chat Bot: {self.__bot.nome}'
        self.__window = sg.Window(
            self.__title, self.__container, font=("Helvetica", 14))

    def tela(self):
        sg.theme('Dark Brown 1')
        self.__container = []
        for comando in self.__bot.comandos:
            self.__container.append([sg.Button(comando.comando)])

        self.__container.append([sg.Text('', key='resposta', size=(50, 1))])

        self.__container.append([sg.Button('Exportar'), sg.Button('Importar')])

        self.update_layout(self.__container)

    def mostra_resultado(self, resposta):
        self.__window.Element('resposta').Update(resposta)

    def limpa_lacuna(self, key):
        self.__window.Element(key).Update('')
