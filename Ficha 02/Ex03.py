# Simulador de ideal

genero = input("Género(M/F): ")
altura = int(input("Altura(cm): "))

if genero.lower() != "m" and genero.lower() != "f":
    print("Não inseriu um género válido")
elif genero.lower() == "m":       # upper - converte para maiusculas
    k = 4                         # lower - converte para minusculas
else: 
    k = 2

if genero.lower() == "m" or genero.lower()== "f":
    pesoIdeal = (altura - 100) - (altura - 150) / k
    print("O Peso Ideal é {:.2f} Kg" .format(pesoIdeal))

