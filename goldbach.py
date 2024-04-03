while True:
    numero = int(input("Informe um número inteiro que seja par e maior que dois, ou Digite 0 para encerrar o programa: "))

    if numero == 0:
        print("Programa Encerrado.")
        break
    
    if numero % 2 != 0:
        print("Número Invalido, por favor digite um numero PAR ")
    elif numero <= 2:
        print("Numero Invalido, certifique-se de que o numero seja MAIOR que dois")
        
    else:
        encontrado = False #Quando for true, vai sair do looping.
        for i in range(2, numero):
            print(f'Verificando combinação: {i} + {numero - i}')
            menor_primo = True
            maior_primo = True

            for a in range(2, i):
                if i % a ==0:
                    menor_primo = False
                    break

            for x in range(2, numero -i):
                if (numero - i) % x == 0:
                    maior_primo = False
                    break

            if menor_primo and maior_primo: #no fim do loop, se menor primo e maior primo se manterem true, eles vão receber as variaveis abaixo
                menor_primo = i
                maior_primo = numero -i
                encontrado = True
                break
        if encontrado:
            print(f"A Soma de dois números primos que resulta em {numero} é de {menor_primo} + {maior_primo}")
        else:
            print(f"Não foi possivel encontrar dois números primos cujo a soma seja igual a {numero}")