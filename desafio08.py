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
#no caso abaixo, há a substituição da banana por 'abacaxi' e 'abacate'
frutas[1:2] = ['abacaxi','abacate']
print(frutas)
#ADICIONADO UM OBJETO EM UM ÍNDICE ESPECÍFICO
#INSERT -> frutas.insert(index,object)
frutas.insert(2,'Maracujá')
print(frutas)