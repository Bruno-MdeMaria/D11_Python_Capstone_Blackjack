import random
from art import logo
import os

#iniciar = input("Bem vindo! Gostaria de jogar uma partida de Backjack? Digite 'S' ou 'N'").lower()



def mao_carta1():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta_recebida = random.choice(cartas)
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
            print(f"Seu adversário e você tem um Blackjack = {jogador1}. Empatou!!")
        elif soma_cpu == 0:
            print(f"Seu Adverário tem um Blackjack{cpu}. Você perdeu!")
        elif soma_jogador1 > 21:
            print(f"Suas cartas são: {jogador1} e a soma delas é {soma_jogador1}. Você perdeu!")
        elif soma_cpu > 21:
            print(f"Seu adverssário tem {cpu} e a soma delas é {soma_cpu}. Você ganhou!")
        elif soma_cpu == soma_jogador1:
            print(f"Suas cartas são: {jogador1} e a soma delas é {soma_jogador1} o mesmo de seu adversário {cpu}. Empatou!")
        
            

cpu = []
jogador1 = []

for _ in range(2): #passa o código duas vezes;
    cpu.append(mao_carta1())
    jogador1.append(mao_carta1())
print(cpu)
print(jogador1)

soma_jogador1 = soma_mao(jogador1)
soma_cpu = soma_mao(cpu)

print(f"Você recebeu as cartas: {jogador1}\nA soma de suas cartas é {soma_jogador1}.\n")
print(f"A primeira das duas cartas do seu adversário é {cpu[0]}.\n")

compare()

nova = input("Digite 'S' se você quer uma nova carta ou 'N' para passar:\n ").lower()
if nova == "s":
    jogador1.append(mao_carta1())
