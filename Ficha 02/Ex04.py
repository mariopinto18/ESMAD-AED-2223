# Simulador de IMC


peso   = float(input("Indique o seu peso(Kg) : "))
altura = float(input("Indique a sua altura(m): "))

imc= peso / altura**2
print("IMC= {:.2f}" .format(imc))

if imc < 18.5:
    print("Abaixo do Peso")
elif imc <= 24.9:
    print("Saudável")
elif imc <= 29.9:
    print("Sobrepeso")
elif imc <= 34.9:
    print("Obesidade Grau I")
elif imc <= 39.9:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")


input()