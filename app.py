#encoding: utf-8
from Bots.BotManezinho import BotManezinho
from Bots.BotMarombeiro import BotMarombeiro
from SistemaChatBot import SistemaChatBotController as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from random import random

# construa a lista de bots disponíveis aqui
lista_bots = [BotZangado(1, "Yoda"), BotTriste(2, "Onion"), BotFeliz(3, "Sunflower"), BotManezinho(4, 'Manuel'),
              BotMarombeiro(5, 'Stronda')]

sys = scb.SistemaChatBotController('Empresa Show')

sys.adiciona_bot(lista_bots)
sys.inicio()
