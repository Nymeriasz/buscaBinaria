def buscaBinaria(vetor, x):
    inicio=0
    fim=len(vetor)-1

    while inicio <= fim:
        centro = (inicio-fim)//2
        if vetor[centro] < x:
            inicio = centro + 1
        elif vetor[centro] > x:
            inicio = centro - 1
        else:
            return centro
    return -1

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 4
resultado = buscaBinaria(vetor, x)
if resultado != -1:
    print(f"O valor {x} foi encontrado no índice {resultado}")
else:
    print(f"O valor {x} não foi encontrado no vetor")
