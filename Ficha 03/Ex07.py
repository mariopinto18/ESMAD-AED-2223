# Ler um numero e verificar se é primo

numero = int(input("Numero:"))

primo = True
for i in range(2, numero):  # o divisor varia entre 2 e o numero-1
    resto = numero % i
    if resto == 0:          # quando encontro um resto 0 => não é primo
        primo = False
        break

if primo==True:
    print("O numero", numero, "é primo")
else:
  print("O numero", numero, "não é primo")

