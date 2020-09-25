print('Iniciando nova operação matématica')
print('Qual é o primeiro número de deseja calcular?')
primeiro_numero=input()
print('Qual é a operação?\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Resto da Divisão')
operacao=int(input())
print('Qual é o segundo número de deseja calcular?')
segundo_numero=input()

if operacao==1:
    print(f'Operação:{primeiro_numero} + {segundo_numero} = {float(primeiro_numero)+float(segundo_numero)}')
elif operacao==2:
    print(f'Operação:{primeiro_numero} - {segundo_numero} = {float(primeiro_numero) - float(segundo_numero)}')
elif operacao==3:
    print(f'Operação:{primeiro_numero} * {segundo_numero} = {float(primeiro_numero) * float(segundo_numero)}')
elif operacao==4:
    print(f'Operação:{primeiro_numero} / {segundo_numero} = {float(primeiro_numero) / float(segundo_numero)}')
elif operacao==5:
    print(f'Operação:{primeiro_numero} % {segundo_numero} = {float(primeiro_numero) % float(segundo_numero)}')
else:
    print('Operação não encontrada')