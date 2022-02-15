#encoding: utf-8
from Bots.BotManezinho import BotManezinho
from Bots.BotMarombeiro import BotMarombeiro
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz

# construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Onion"), BotFeliz("Sunflower"), BotManezinho('Manuel'),
              BotMarombeiro('Stronda')]
sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
