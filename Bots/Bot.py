
from abc import ABC, abstractmethod
import random as random
from Bots.Comando import Comando


class Bot(ABC):

    def __init__(self, nome: str):
        self.__id = random.randint(0, 900)
        self.__nome = nome
        self.__comandos = []
        self.__comando_erro = "Não consigo responder essa pergunta"

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    @property
    def comando_erro(self):
        return self.__comando_erro

    @comando_erro.setter
    def comando_erro(self, comando_erro: str):
        self.__comando_erro = comando_erro

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos

    def adicionar_comando(self, comando: str, resposta: str):
        self.__comandos.append(Comando(comando, resposta))

    def remove_comando(self, index):
        self.__comandos.pop(index)

    def mostra_comandos(self):
        for index, comando in enumerate(self.comandos):
            print(f'{index} - {comando.comando}')

    def executa_comando(self, cmd):
        print('     --> Eu te respondo: ', end='')
        try:
            cmd = int(cmd)
            try:
                print(self.comandos[cmd].pegar_resposta())
            except LookupError:
                print(self.comando_erro)
        except (ValueError, TypeError):
            print(self.comando_erro)

    @abstractmethod
    def boas_vindas():
        pass

    @abstractmethod
    def despedida():
        pass

    @abstractmethod
    def apresentacao():
        pass
