# lê um texto e imprime número de vogais e de espaços
texto = input("Indique um texto:")

vogais=0
comp = len(texto)
for i in range(0,comp):
    if texto[i].lower() == "a" or texto[i].lower() == "e" or texto[i].lower() == "i" or texto[i].lower() == "o" or texto[i].lower() == "u":
        vogais+=1

# contar espaços
espacos= texto.count(" ")

print("Nº de caracteres:", len(texto))
print("Nº de vogais    :", vogais)
print("Nº de espaços   :", espacos)

input()