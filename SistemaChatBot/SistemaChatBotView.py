import PySimpleGUI as sg
from SistemaChatBot.BaseView import BaseView
# View do padrão MVC


class SistemaChatBotView(BaseView):
    def __init__(self, controlador, bot):
        super().__init__("Sistema Chat Bot", controlador)
        self.__bot = bot

    def tela(self):
        sg.theme('Dark Brown 1')
        self.container = []
        self.container.append([sg.Text(f'{self.__bot.nome} diz:')])
        self.container.append(
            [sg.Multiline(self.__bot.boas_vindas(), key='resposta', size=(50, 2), disabled=True)])

        self.container.append([sg.Text('Perguntas:')])

        for comando in self.__bot.comandos:
            self.container.append([sg.Button(comando.comando)])

        self.container.append(
            [sg.Button('Voltar')])
        self.update_layout(self.container)

    def mostra_resultado(self, resposta):
        self.window.Element('resposta').Update(resposta)

    def limpa_lacuna(self, key):
        self.window.Element(key).Update('')
