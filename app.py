#encoding: utf-8
from Bots.BotManezinho import BotManezinho
from Bots.BotMarombeiro import BotMarombeiro
from SistemaChatBot import SistemaChatBotController as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from random import random

# construa a lista de bots disponíveis aqui
lista_bots = [BotZangado(random(), "Yoda"), BotTriste(random(), "Onion"), BotFeliz(random(), "Sunflower"), BotManezinho(random(), 'Manuel'),
              BotMarombeiro(random(), 'Stronda')]

sys = scb.SistemaChatBotController('Empresa show').adiciona_bot(lista_bots)

sys.inicio()
