import PySimpleGUI as sg
from abc import ABC, abstractmethod

# View do padrão MVC


class BaseView(ABC):
    def __init__(self, title, controlador):
        self.__controlador = controlador
        self.__title = title
        self.__container = []
        self.__window = None

    @abstractmethod
    def tela(self):
        pass

    @property
    def window(self):
        return self.__window

    @property
    def container(self):
        return self.__container

    @window.setter
    def window(self, window):
        self.__window = window

    @container.setter
    def container(self, container):
        self.__container = container

    def update_layout(self, layout):
        self.__window = sg.Window(self.__title, layout, font=('Helvetica', 14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
