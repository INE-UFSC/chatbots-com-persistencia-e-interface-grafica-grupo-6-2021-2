

import PySimpleGUI as sg
import BaseView

# View do padrão MVC


class ExportView (BaseView):
    def __init__(self, controlador):
        super().__init__("Exportação de chatbot", controlador)

    def tela(self):
        linha0 = [sg.Text('Digite o nome do arquivo que quer salvar:')]
        linha1 = [sg.InputText('', key='caminho_export')]
        linha2 = [sg.Button('Exportar')]

        self.__container = [linha0, linha1, linha2]
        self.update_layout(self.__container)
