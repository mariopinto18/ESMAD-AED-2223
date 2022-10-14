
# Calcula o IMC (Índice de Massa Corporal), dado o peso e a altura

peso = float(input("Peso (kg):"))
altura =float(input("Altura(m):"))

#Calcula o índice de massa corporal, IMC
imc = peso/(pow(altura,2))

print("IMC = {:.2f}" .format(imc))

input()