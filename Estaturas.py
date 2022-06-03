import statistics

lista = [ 1.70, 1.71, 1.50, 1.60, 1.46, 1.50, 1.70, 1.70, 1.60, 1.79,1.70, 1.47 ]

maximo = max(lista)
minimo = min(lista)
mediana = statistics.median(lista)
media = statistics.mean(lista)
moda = statistics.mode(lista)
print(f'la moda es : {moda}')
print(f'el minimo es {minimo}')
print(f'la maxima es {maximo}')
print(f'la media es {media}')
print(f'la mediana es {mediana}')
