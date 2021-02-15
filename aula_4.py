numero = int(input(('Entre com um número: ')))


for numero in range(101):
    div = 0
    for x in range(1, numero+1):
        resto = numero % x
        #print( resto)
        if resto == 0:
            div += 1

    if div == 2:
        print("Numero {} é Primo".format(numero))
    else:
        print("Número {} não é primo".format(numero))