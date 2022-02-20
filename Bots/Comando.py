from random import randint


class Comando:

    def __init__(self, comando: str, resposta: str):
        self.__comando = comando
        self.__resposta = resposta
        
    def __iter__(self):
        yield from {
            "comando": self.comando,
            "resposta": self.resposta,
        }.items()

    @property
    def comando(self):
        return self.__comando

    @comando.setter
    def comando(self, comando: str):
        self.__comando = comando

    @property
    def resposta(self):
        return self.__resposta

    @resposta.setter
    def resposta(self, resposta: str):
        self.__resposta = resposta

    def adicionar_resposta(self, resposta: str):
        self.resposta.append(resposta)

    def remove_resposta(self, index):
        self.resposta.pop(index)

    def mostrar_respostas(self):
        for index, x in enumerate(self.resposta):
            print(f'{index} - {x}')

    def pegar_resposta(self):
        random = randint(0, len(self.resposta)-1)
        return self.resposta[random]
