from random import randint
from time import sleep
import sys
import os

item = ('Pedra','Papel','Tesoura')
computer = randint(0,2)

#Reiniciar o programa novamente após as condicionais exibirem o resultado
#assim dando a impressão de jogar varias vezes 
def restart_program():
    item = ('Pedra','Papel','Tesoura')
    computer = randint(0,2)
    print ('\n\n*******𝙋𝙚𝙙𝙧𝙖, 𝙋𝙖𝙥𝙚𝙡 𝙚 𝙏𝙚𝙨𝙤𝙪𝙧𝙖*******\n\n')
    print('''Suas opções são:
                [0] ***Pedra*** 
                [1] ***Papel***
                [2] ***Tesoura***''')
    player=int(input('Qual sua jogada:  '))  
    print(f'O Computador jogou: {item[computer]}\n')
    print(f'O Jogador jogou: {item[player]}\n')
    print('-=' * 11)
    print('JO')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Pô')
    sleep(2)
    print('-=' * 11)

    if player == 0 and computer == 0:
            print('Empate!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 0 and computer == 1:
            print('O computador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 0 and computer == 2:
            print('O Jogador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program() 
    elif player == 1 and computer == 0:
            print('O Jogador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 1 and computer == 1:
            print('Empate!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 1 and computer == 2:
            print('O computador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 2 and computer == 0:
            print('O computador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 2 and computer == 1:
            print('O Jogador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    elif player == 2 and computer == 2:
            print('Empate!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
    else: 
            print('Opção Errada!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()       


print('________________')
print ('\n\n*******𝙋𝙚𝙙𝙧𝙖, 𝙋𝙖𝙥𝙚𝙡 𝙚 𝙏𝙚𝙨𝙤𝙪𝙧𝙖*******\n\n')

#Apresentação e input das opções apresentadas para a escolha do jogador 
print('''Suas opções são:
                [0] ***Pedra*** 
                [1] ***Papel***
                [2] ***Tesoura***''')
player=int(input('Qual sua jogada:  '))


#Utilizei o sleep para criar um intervalo de 1 a 2 segundos para ter um tempo de jogo entre as palavras
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('Pô')
sleep(2)
print('-=' * 11)

#Mensagens nas condições resolvidas do jogo

print(f'O Computador jogou: {item[computer]}\n')
print(f'O Jogador jogou: {item[player]}\n')
print('-=' * 11)


#Estruturas condicionais para o jogo 
if player == 0 and computer == 0:
            print('Empate!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 0 and computer == 1:
            print('O computador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 0 and computer == 2:
            print('O Jogador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program() 
elif player == 1 and computer == 0:
            print('O Jogador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 1 and computer == 1:
            print('Empate!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 1 and computer == 2:
            print('O computador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 2 and computer == 0:
            print('O computador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 2 and computer == 1:
            print('O Jogador ganhou!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
elif player == 2 and computer == 2:
            print('Empate!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()
else: 
            print('Opção Errada!\n','-='*11)
            print('\n\n Fim do jogo! \n Começando novamente!\n\n')
            sleep(6)
            restart_program()       



