A =int(input('Me diga o tamanho de 3 retas e direi se formam ou não um triângulo: '))
B = int(input('Me diga o tamanho da segunda em metros: '))
C = int(input('Me diga o tamanho da terceira em metros: '))
if A < B + C and B < A + C and C < A + B:
    print('Os lados formam um triângulo! ')
else:
    print('Não formam um triângulo.')