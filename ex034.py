salario = float(input('Me diga seu salário: '))
if salario>1250:
    salario_atual = (salario*10)/100+salario
    print(f'Seu salário atual é {salario_atual} ')
else:
    salario_atual2 = (salario*15)/100+salario
    print(f'Seu salário atual é {salario_atual2}')