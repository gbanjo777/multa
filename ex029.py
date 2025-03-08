velocidade = int(input('Me diga a velocidade de um carro: '))
velocidade_limite = 80
if velocidade > velocidade_limite:
    print('você foi multado! receberá R$7,00 por quilometro excedido')
    multa = (velocidade-80)*7
    print(f'Sua multa foi de {multa} reais.')
else:
    print('Continue prezando por sua vida. ')
