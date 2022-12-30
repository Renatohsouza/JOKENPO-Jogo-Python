from random import choice
from time import sleep
from emoji import emojize

# -> INSERIR CORES <-

print(f'{" Seja bem vindo jogador! ":=^40}')
print(f'{" Vamos jogar JOKENPO! ":=^40}')
sleep(1)
print('-='*20)

nome = str(input('Qual o seu nome jogador? ')).strip().capitalize()
print('-='*20)

print(f'{"- INSTRUÇÕES -":^40}')
print('-='*20)
print(f'{"ESCOLHA ENTRE:":^40}')
print(emojize(f'{"[:facepunch:]-Pedra [:hand:]-Papel [:v: ]-Tesoura!":^40}', language='alias')) #emoji
print('-='*20)
sleep(1)

itens = ['Pedra','Papel','Tesoura']
computador = choice(itens)

jogador = str(input(f'Faça sua escolha {nome}: ')).strip().capitalize()
print('-='*20)

if jogador == 'Pedra' or jogador == 'Papel' or jogador == 'Tesoura':

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print('-='*20)
    print(' ')
    print(f'- Computador jogou: {computador}') # Nesta parte, procurar possibilidades de inserir emojis nas escolhas de jogador/computador
    print(f'- {nome} jogou: {jogador}')
    print(' ')
    print('-='*20)

    if computador == 'Pedra': 
            if jogador == 'Pedra':
                print(emojize("EMPATAMOS! :sleepy:", language='alias'))
            elif jogador == 'Papel':
                print(emojize(f"VOCÊ VENCEU {nome}! :trophy:", language='alias'))
            elif jogador == 'Tesoura':
                print(emojize("VOCÊ PERDEU! :smiling_imp:", language='alias'))
    elif computador == 'Papel':
            if jogador == 'Pedra':
                print(emojize("VOCÊ PERDEU! :smiling_imp:", language='alias'))
            elif jogador == 'Papel':
                print(emojize("EMPATAMOS! :sleepy:", language='alias'))
            elif jogador == 'Tesoura':
                print(emojize(f"VOCÊ VENCEU {nome}! :trophy:", language='alias'))
    elif computador == 'Tesoura':
        if jogador == 'Pedra':
            print(emojize(f"VOCÊ VENCEU {nome}! :trophy:", language='alias'))
        elif jogador == 'Papel':
            print(emojize("VOCÊ PERDEU! :smiling_imp:", language='alias'))
        elif jogador == 'Tesoura':
            print(emojize("EMPATAMOS! :sleepy:", language='alias'))
else:
    print(emojize(":x: OPÇÃO INVÁLIDA! TENTE NOVAMENTE! :x:", language='alias'))
print('-='*20)
