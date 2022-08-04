from ast import Return
import random
from art import logo
import os

#iniciar = input("Bem vindo! Gostaria de jogar uma partida de Backjack? Digite 'S' ou 'N'").lower()

cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def mao_carta1():
    carta_recebida = random.choices(cartas, k= 2)
    return carta_recebida

def soma_mao(cartas):
    if sum(cartas) == 21 and len(cartas)==2:
        return 0
    elif sum(cartas) > 21 and cartas == 11:
        cartas.remove(11)
        cartas.append(1)
        return sum(cartas)
    return sum(cartas)

def compare():
        if soma_jogador1 == 0:
            print(f"Você tem um Blackjack{jogador1}. Parabéns você ganhou!!")
        elif soma_jogador1 == 0 and soma_cpu == 0:
            print(f"Seu adversário e você tem a mesma pontuação = {soma_jogador1}. Empatou!!")
        elif soma_cpu == 0:
            print(f"Você recebeu as cartas: {jogador1}\nSua pontuação atual é {soma_jogador1}.")
            print(f"Seu Adverário tem um Blackjack{mao_carta1}. Você perdeu!")
        elif soma_jogador1 == 21:
            print(f"Suas cartas são {jogador1} e a soma delas é {soma_jogador1}. Parabens você venceu!")
        elif soma_cpu == 21:
            print(f"Seu adverssário recebeu as cartas {cpu} e a soma delas é {soma_cpu}. Você perdeu!")
            
        else:
            print(f"Você recebeu as cartas: {jogador1}\nSua pontuação atual é {soma_jogador1}.")
            print(f"A primeira das duas cartas do seu adversário é {cpu[0]}.")

cpu = mao_carta1()
jogador1 = mao_carta1()
soma_jogador1 = soma_mao(jogador1)
soma_cpu = soma_mao(cpu)
compare()


