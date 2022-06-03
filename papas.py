import statistics

lista = [ 3670, 3800, 3950, 3700, 4000, 4100, 4000, 3930, 3840, 3790, 3650]

maximo = max(lista)
minimo = min(lista)
mediana = statistics.median(lista)
media = statistics.mean(lista)
moda = statistics.mode(lista)
print(moda)
print(minimo)
print(maximo)
print(media)
print(mediana)

