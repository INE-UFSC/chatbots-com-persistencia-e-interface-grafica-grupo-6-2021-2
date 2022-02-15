from multiprocessing import set_forkserver_preload
from Bots.Bot import Bot
from random import random
from Dao.SistemaChatBotDAO import SistemaChatBotDAO
from SistemaChatBotView import SistemaChatBotView


class SistemaChatBotController:
    def __init__(self, nomeEmpresa):
        self.__id = random()
        self.__empresa = nomeEmpresa
        self.__lista_bots = SistemaChatBotDAO().get_list()
        # self.adiciona_bot(lista_bots)
        self.__bot = None
        self.__sistema_chat_bot_DAO = SistemaChatBotDAO()
        self.__sistema_chat_bot_view = SistemaChatBotView(self)

    @property
    def id(self):
        return self.__id

    @property
    def bot(self):
        return self.__bot

    @bot.setter
    def bot(self, bot):
        self.__bot = bot

    @property
    def lista_bots(self):
        return self.__lista_bots

    @lista_bots.setter
    def lista_bots(self, lista):
        self.__lista_bots = lista

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, nome):
        self.__empresa = nome

    def adiciona_bot(self, bots):
        for x in bots:
            if isinstance(x, Bot):
                self.__sistema_chat_bot_DAO.add(x)
            else:
                print(f'{x} não é um bot conhecido')

    def boas_vindas(self):
        print(f'Bem-vindo ao sistema da empresa {self.__empresa}')

    def mostra_menu(self):
        print("Os bots disponíveis são: ")
        count = 0
        try:
            for chave, bot in self.__sistema_chat_bot_DAO.get_all():
                print(chave, bot)
                bot.apresentacao()
        except IndexError:
            print('Não há nenhum bot disponivel')

    def escolhe_bot(self):
        nome = input('Digite o nome do bot escolhido: ')
        try:
            nome = isinstance(nome, str)
            self.__bot = self.__sistema_chat_bot_DAO.find(nome)
        except ValueError:
            print("Por favor digite o nome do bot")
            self.escolhe_bot()
        except IndexError:
            print('Escolha um numero válido')
            self.escolhe_bot()

    def mostra_comandos_bot(self):
        self.bot.mostra_comandos()

    def le_envia_comando(self):
        escolha = input(
            'Digite o comando desejado (ou -1 para fechar o programa): ')
        if escolha == '-1':
            return 0
        else:
            self.bot.executa_comando(escolha)
            return 1

    def inicio(self):
        self.boas_vindas()
        print()
        self.mostra_menu()
        print()
        self.escolhe_bot()
        print(f'--> {self.bot.nome} diz: {self.bot.boas_vindas()}')
        while True:
            print()
            self.mostra_comandos_bot()
            print()
            escolha = self.le_envia_comando()
            if escolha == 0:
                print()
                print(f'--> {self.bot.nome} diz: {self.bot.despedida()}')
                print()
                break
