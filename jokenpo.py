# https://dojopuzzles.com/problems/jokenpo/
from random import randint
from time import sleep

#começando o jogo
itens = ('Pedra', 'papel', 'tesoura')
maquina = randint(0, 2)

print('''Escola uma opção
[0] pedra
[1] papel
[2] tesoura''')

player = int(input('Qual voce ira escolher'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
print('-=' * 11)

#escolha dos jogadores
print(f'maquina jogou: {itens[maquina]}')
print(f'player jogou: {itens[player]}')
print('-=' * 11)

#estrutura dos resultados

if maquina == 0: # maquina escolheu pedra
    if player == 0:
        print('Jogo empatado')

    elif player == 1:
        print('Voce venceu!')

    elif player == 2:
        print('Voce perdeu para a maquina')

    else:
        print('Jogada invalida!')

elif maquina == 1: # maquina escolheu papel
    if player == 0:
        print('Voce venceu')

    elif player == 1:
        print('Empatou')

    elif player == 2:
        print('voce ganhou')
    else:
        print('Jogada invalida!')

elif maquina == 2: #maquina jogou tesoura
    if player == 0:
        print('voce venceu')

    elif player == 1:
        print('Empatou')

    elif player == 2:
        print('voce ganhou')
    else:
        print('Jogada invalida!')
