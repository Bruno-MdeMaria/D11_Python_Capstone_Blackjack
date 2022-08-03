import random
from art import logo
import os

#iniciar = input("Bem vindo! Gostaria de jogar uma partida de Backjack? Digite 'S' ou 'N'").lower()

cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def mao_carta():
    carta_recebida = random.choices(cartas, k= 2)
    return carta_recebida

def soma_mao():
    int = []
    for carta in mao_carta():
        int = (int(carta))
    return int
     


cpu = mao_carta()
jogador = soma_mao()
print(f"Você recebeu as cartas: {jogador}\n Sua pontuação atual é {jogador[0]+[1]}")
print(f"O seu adversário recebeu a carta {cpu[0]} e mais uma carta oculta\n")


