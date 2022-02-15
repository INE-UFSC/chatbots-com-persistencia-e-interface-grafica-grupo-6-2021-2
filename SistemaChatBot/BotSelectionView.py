import PySimpleGUI as sg
from SistemaChatBot.BaseView import BaseView


class BotSelectionView(BaseView):
    def __init__(self, controlador, lista_bots):
        super().__init__("Seleção de Bot", controlador)
        self.__lista_bots = lista_bots

    def tela(self):
        sg.theme('Dark Brown 1')
        self.container = []
        bots = []

        self.container.append([sg.Text('Selecione o seu Bot:')])

        for bot in self.__lista_bots:
            bots.append(sg.Button(bot.nome))
        
        self.container.append(bots)

        self.update_layout(self.container)