import PySimpleGUI as sg

# View do padrão MVC


class SistemaChatBotView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window(
            "Sistema Chat Bot", self.__container, font=("Helvetica", 14))

    def tela_consulta(self):
        sg.theme('Dark Brown 1')

        self.__container = [
            [sg.Text('')],
            [sg.Text('', size=(10, 1)), sg.InputText('', key='')],
            [sg.Text('', size=(10, 1)), sg.InputText('', key='codigo')],
            [sg.Button(''), sg.Button(''), sg.Button('')],
            [sg.Text('', key='status', size=(50, 1))]
        ]

        self.__window = sg.Window(
            "Sistema Chat Bot", self.__container, font=("Helvetica", 14))

    def mostra_resultado(self, resultado):
        self.__window.Element('status').Update(resultado)

    def limpa_lacuna(self, key):
        self.__window.Element(key).Update('')

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
