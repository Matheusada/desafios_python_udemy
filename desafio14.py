print('\nContagem com o break')
n = 1 
while n <=10:
    print(n)
    n +=1
    if n == 6:
        break

print('\nContagem com o continue')
j =1
while j <= 10:
    print(j)
    j += 1
    if j ==5:
        j += 1
    else:
        continue

# UTILIZANDO O FOR - break
for numero in range(1,11):
    if numero > 5:
        break
    print(numero)

#UTILIZANDO O FOR - continue
for numero in range(1,11):
    if numero ==5:
        continue # continue o loop
    print(numero)

