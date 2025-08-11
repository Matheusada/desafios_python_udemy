frutas = ['maça', 'banana', 'manga', 'uva']
print(frutas)
frutas[1] = 'Morango'
print(frutas)

#MÉTODOS (EXTENSÕES)
frutas.append('abacaxi')
print(frutas)

#CONTEÚDOS
#alterando 2 itens ao mesmo tempo
frutas[1:3] = ['abacaxi','abacate']
print(frutas)
#PARTICULARIDADES => frutas[1:3] de 1 até 3, mas sem 
# incluir o 3