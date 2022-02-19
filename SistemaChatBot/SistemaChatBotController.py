from Bots.Bot import Bot
from random import random
from SistemaChatBot.BotDAO import BotDAO
from SistemaChatBot.SistemaChatBotView import SistemaChatBotView
from SistemaChatBot.ImportView import ImportView
from SistemaChatBot.ExportView import ExportView
from SistemaChatBot.BotSelectionView import BotSelectionView
import PySimpleGUI as sg

from Bots.BotManezinho import BotManezinho
from Bots.BotMarombeiro import BotMarombeiro
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz


class SistemaChatBotController:
    def __init__(self, nomeEmpresa):
        self.__id = random()
        self.__empresa = nomeEmpresa
        self.__sistema_chat_bot_DAO = BotDAO()
        self.__lista_bots = self.__verifica_existencia_picke()
        self.__bot = None
        self.__sistema_chat_bot_view = SistemaChatBotView(self, self.__bot)
        self.__telaExport = ExportView(self)
        self.__telaImport = ImportView(self)
        self.__telaBotSelection = BotSelectionView(self, self.__lista_bots)
        self.__telaAtual = self.__telaBotSelection

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

    def __verifica_existencia_picke(self):
        lista_bots_atual = self.__sistema_chat_bot_DAO.get_list()

        if not lista_bots_atual:
            nova_lista_bots = [BotZangado("Yoda"), BotTriste("Onion"),
                               BotFeliz("Sunflower"), BotManezinho("Manuel"), 
                               BotMarombeiro("Stronda")]
            for bot in nova_lista_bots:
                self.adiciona_bot(bot)
            return nova_lista_bots
        else:
            return lista_bots_atual

    def adiciona_bot(self, bot: Bot):
        if isinstance(bot, Bot):
            self.__sistema_chat_bot_DAO.add(bot)

    def boas_vindas(self):
        return (f'Bem-vindo ao sistema da empresa {self.__empresa}')

    def mostra_menu(self):
        print("Os bots disponíveis são: ")
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
        self.__telaAtual.tela()

        # Loop de eventos
        rodando = True
        export_active = False
        import_active = False
        bot_selected = False
        resultado = ''
        while rodando:
            if export_active:
                export_active = self.handle_export()
            elif import_active:
                import_active = self.handle_import()
            else:
                event, values = self.__telaAtual.le_eventos()

                # event, values = self.__telaBotSelection.le_eventos()

                if event == sg.WIN_CLOSED:
                    self.__telaAtual.fim()
                    break
                else:
                    try:
                        if event == 'Exportar':
                            self.__telaExport.tela()
                            export_active = True
                        elif event == 'Importar':
                            self.__telaImport.tela()
                            import_active = True
                        else:
                            if bot_selected:
                                for comando in self.__bot.comandos:
                                    if event == comando.comando:
                                        resultado = comando.resposta
                                        print(resultado)

                            for bot in self.__lista_bots:
                                if event == bot.nome:
                                    self.__bot = bot
                                    self.__sistema_chat_bot_view = SistemaChatBotView(
                                        self, self.__bot)
                                    print(bot, bot.nome)
                                    self.__telaAtual.fim()
                                    self.__telaAtual = self.__sistema_chat_bot_view
                                    self.__telaAtual.tela()
                        if event == 'Voltar':
                            self.__telaAtual.fim()
                            self.__telaAtual = self.__telaBotSelection
                            self.__telaAtual.tela()

                    except ValueError:
                        resultado = 'Código deve ser um número inteiro!'
                    except KeyError:
                        resultado = 'Valor não cadastrado!'
                    except NameError:
                        resultado = 'Digite ao menos um campo!'

                if resultado != '':
                    dados = str(resultado)
                    self.__sistema_chat_bot_view.mostra_resultado(dados)
                    self.__sistema_chat_bot_view.limpa_dados()

    def handle_export(self):
        event_exp, values_exp = self.__telaExport.le_eventos()

        export_active = True

        if event_exp == sg.WIN_CLOSED:
            self.__telaExport.fim()
            export_active = False
        elif event_exp == 'Exportar':
            path = values_exp['caminho_export']
            self.__sistema_chat_bot_DAO.set_data_source(path)
            self.__telaExport.fim()
            export_active = False

        return export_active

    def handle_import(self):
        event_exp, values_exp = self.__telaImport.le_eventos()

        import_active = True

        if event_exp == sg.WIN_CLOSED:
            self.__telaImport.fim()
            import_active = False
        elif event_exp == 'importar':
            path = values_exp['caminho_import']
            self.__sistema_chat_bot_DAO.import_source(path)
            self.__telaImport.fim()
            import_active = False

        return import_active
