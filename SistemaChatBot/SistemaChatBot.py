from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        self.adiciona_bot(lista_bots)
        self.__bot = None

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
                self.__lista_bots.append(x)
            else:
                print(f'{x} não é um bot conhecido')

    def boas_vindas(self):
        print(f'Bem-vindo ao sistema da empresa {self.__empresa}')

    def mostra_menu(self):
        print("Os bots disponíveis são: ")
        count = 0
        try:
            for x in self.lista_bots:
                apresentacao = x.apresentacao()
                print(
                    f"{count} - Bot: {x.nome} - Mensagem de apresentação: {apresentacao}")
                count += 1
        except IndexError:
            print('Não há nenhum bot disponivel')

    def escolhe_bot(self):
        escolha = input('Digite o numero do bot escolhido: ')
        try:
            escolha = int(escolha)
            self.__bot = self.__lista_bots[escolha]
        except ValueError:
            print("Por favor digite um número")
            self.escolhe_bot()
        except IndexError:
            print('Escolha um numero válido')
            self.escolhe_bot()

    def mostra_comandos_bot(self):
        bot = self.__bot
        bot.mostra_comandos()

    def le_envia_comando(self):
        escolha = input(
            'Digite o comando desejado (ou -1 para fechar o programa): ')
        if escolha == '-1':
            return 0
        else:
            self.__bot.executa_comando(escolha)
            return 1

    def inicio(self):
        self.boas_vindas()
        print()
        self.mostra_menu()
        print()
        self.escolhe_bot()
        print(f'--> {self.__bot.nome} diz: {self.__bot.boas_vindas()}')
        while True:
            print()
            self.mostra_comandos_bot()
            print()
            escolha = self.le_envia_comando()
            if escolha == 0:
                print()
                print(f'--> {self.__bot.nome} diz: {self.__bot.despedida()}')
                print()
                break
