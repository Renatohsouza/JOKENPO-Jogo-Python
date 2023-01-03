from random import choice
from time import sleep
from emoji import emojize

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'lilas':'\033[35m'}

linhas = ('-='*20)

print(f'{" Seja bem vindo jogador! ":^40}')
print(f'{" Vamos jogar JOKENPO! ":^40}')
sleep(1)
print(linhas)

nome = str(input(f"{(cores['ciano'])}Qual o seu nome jogador? {cores['limpa']}")).strip().capitalize()
print(linhas)

print(f'{"- INSTRUÇÕES -":^40}')
print(linhas)
print(f'{"ESCOLHA ENTRE:":^40}')
print(emojize(f'{"[:facepunch:]-Pedra [:hand:]-Papel [:v: ]-Tesoura!":^40}', language='alias')) 
print(linhas)
sleep(1)

itens = ['Pedra','Papel','Tesoura']
computador = choice(itens)

jogador = str(input(f"{(cores['ciano'])}Faça sua escolha {nome}: {cores['limpa']} ")).strip().capitalize()
print(linhas)

if jogador == 'Pedra' or jogador == 'Papel' or jogador == 'Tesoura':

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print(linhas)
    print(' ')
    print(f'- Computador jogou: {computador}') # Nesta parte, será inserido emojis nas escolhas de jogador/computador
    print(f'- {nome} jogou: {jogador}')
    print(' ')
    print(linhas)

    if computador == 'Pedra': 
            if jogador == 'Pedra':
                print(emojize(f"{cores['amarelo']}EMPATAMOS!{cores['limpa']} :sleepy:", language='alias'))
            elif jogador == 'Papel':
                print(emojize(f"{cores['verde']}VOCÊ VENCEU {nome}!{cores['limpa']} :trophy:", language='alias'))
            elif jogador == 'Tesoura':
                print(emojize(f"{cores['vermelho']}VOCÊ PERDEU!{cores['limpa']} :smiling_imp:", language='alias'))
    elif computador == 'Papel':
            if jogador == 'Pedra':
                print(emojize(f"{cores['vermelho']}VOCÊ PERDEU!{cores['limpa']} :smiling_imp:", language='alias'))
            elif jogador == 'Papel':
                print(emojize(f"{cores['amarelo']}EMPATAMOS!{cores['limpa']} :sleepy:", language='alias'))
            elif jogador == 'Tesoura':
                print(emojize(f"{cores['verde']}VOCÊ VENCEU {nome}!{cores['limpa']} :trophy:", language='alias'))
    elif computador == 'Tesoura':
        if jogador == 'Pedra':
            print(emojize(f"{cores['verde']}VOCÊ VENCEU {nome}!{cores['limpa']} :trophy:", language='alias'))
        elif jogador == 'Papel':
            print(emojize(f"{cores['vermelho']}VOCÊ PERDEU!{cores['limpa']} :smiling_imp:", language='alias'))
        elif jogador == 'Tesoura':
            print(emojize(f"{cores['amarelo']}EMPATAMOS!{cores['limpa']} :sleepy:", language='alias'))
else:
    print(emojize(f"{cores['lilas']}:x: OPÇÃO INVÁLIDA! TENTE NOVAMENTE! :x:{cores['limpa']}", language='alias'))
print(linhas)
