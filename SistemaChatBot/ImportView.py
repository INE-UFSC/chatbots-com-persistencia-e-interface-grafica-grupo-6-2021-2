import PySimpleGUI as sg
from SistemaChatBot.BaseView import BaseView

# View do padrão MVC


class ImportView(BaseView):
    def __init__(self, controlador):
        super().__init__("Importação de chatbots", controlador)

    def tela(self):
        self.__container = [[sg.InputText(key="caminho_import"), sg.FileBrowse(file_types=(("*.pkl"),))],
                            [sg.Button("importar")]]

        self.update_layout(self.__container)
