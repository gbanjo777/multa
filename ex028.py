import random
from time import sleep
print('Acerte o número que estou pensando!')
input('Pressione Enter para começar...')  # aguarda o usuario apertar Enter

aleatorio = random.randint(0, 5)  # gera o número aleatório
acertou = False  # variável pra controlar o loop

while not acertou:  # enquanto o usuário não acertar
    resposta = input('Qual número você acha que eu pensei? ').strip().lower()
    print('PROCESSANDO...')
    sleep(3)

    if resposta == str(aleatorio):  # se acertar, sai do loop
        print('Você ganhou!')
        acertou = True
    else:
        print('Errado! Tente novamente.')