import random
from art import logo
import os



def mao_carta1():
    cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    carta_recebida = random.choice(cartas)
    return carta_recebida

#Dica 6: Crie uma função chamada calculate_score() que receba uma Lista de cartões como entrada
#e retorna a pontuação.
#Procure a função sum() para ajudá-lo a fazer isso.

#Dica 7: Dentro de calculate_score() verifique se há um blackjack (uma mão com apenas 2 cartas: ás + 10) e retorne 0 em vez da pontuação real. 0 representará um blackjack em nosso jogo.
def soma_mao(cartas):
    if sum(cartas) == 21 and len(cartas)==2:
        return 0
#Dica 8: Dentro de calculate_score() verifique se há um 11 (ás). Se a pontuação já for superior a 21, remova o 11 e substitua-o por 1. Pode ser necessário procurar append() e remove().    
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)
  
#Dica 13: Crie uma função chamada compare() e passe o user_score e computer_score. Se o computador e o usuário tiverem a mesma pontuação, é um empate. Se o computador tiver um blackjack (0), o usuário perde. Se o usuário tiver um blackjack (0), então o usuário ganha. Se o user_score for superior a 21, o usuário perde. Se o computer_score for superior a 21, o computador perde. Se nenhuma das opções acima, então o jogador com a maior pontuação ganha.
def compare(soma_jogador1, soma_cpu):
        if soma_jogador1 > 21 and soma_cpu > 21:
            return "Você perdeu!😭"
        if soma_cpu == soma_jogador1:
            return "Empatou!🙃"
        elif soma_cpu == 0:
            return "Você perdeu!😱"
        elif soma_jogador1 == 0:
            return "Parabéns você ganhou!!😎"
        elif soma_jogador1 > 21:
            return "Você perdeu!😤"
        elif soma_cpu > 21:
            return "Você ganhou!😁"
        elif soma_jogador1 > soma_cpu:
            return "Você ganhou!😃"
        else: 
            return "Você perdeu!😤"
        

#Dica 5: Dê ao usuário e ao computador 2 cartas cada usando deal_card()


def play_game():
    
    
    print(logo)

    cpu = []
    jogador1 = []
    fim_jogo = False

    for _ in range(2): #passa o código duas vezes;
        cpu.append(mao_carta1())
        jogador1.append(mao_carta1())
   



    #Dica 11: A pontuação deverá ser verificada novamente a cada nova carta retirada e as verificações da Dica 9 precisam ser repetidas até o fim do jogo.
   
    while not fim_jogo:
        soma_jogador1 = soma_mao(jogador1)
        soma_cpu = soma_mao(cpu)

        print(f"\nA primeira das duas cartas do seu adversário é {cpu[0]}.\n")
        print(f"\nVocê recebeu as cartas: {jogador1}\nA soma de suas cartas é {soma_jogador1}.\n")

        if soma_jogador1 == 0 or soma_cpu == 0 or soma_jogador1 > 21:
            fim_jogo = True
        else:
            nova = input("\nDigite 'S' se você quer uma nova carta ou 'N' para passar a vez:\n").lower()
            if nova == "s":
                jogador1.append(mao_carta1())
            else:
                fim_jogo = True

    while soma_cpu != 0 and soma_cpu < 17:
        cpu.append(mao_carta1())
        soma_cpu = soma_mao(cpu)
    print(f"\nSuas cartas são: {jogador1} e a soma delas é {soma_jogador1}.\n")
    print(f"\nAs cartas do seu adversário são: {cpu} e a soma delas é {soma_cpu}.\n")
    print(compare(soma_jogador1, soma_cpu))

while input("\nVocê deseja jogar uma partida de Blackjack? Digite 'S' ou 'N':\n").lower() == "s": #recebe a pergunta ejá compara a resposta como verdadeira para continuar o loop ou não.
    os.system("cls")
    play_game()

