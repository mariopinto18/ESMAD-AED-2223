# Exercicio 7
print("\t\t\t\tPlanetas")
print("\t\t\t\t1 - Mercúrio")
print("\t\t\t\t2 - Venus")
print("\t\t\t\t3 - Marte")
print("\t\t\t\t4 - Júpiter")
print("\t\t\t\t5 - Saturno")
print("\t\t\t\t6 - Urano")

peso = float(input("\n\n\tIndique o seu peso:"))
planeta = int(input("\n\n\tCódigo do planeta:"))

if planeta ==1:
    gravidade= 0.37
elif planeta ==2:
    gravidade= 0.88
elif planeta == 3:
    gravidade= 0.38
elif planeta == 4:
    gravidade= 2.64
elif planeta ==5:
    gravidade= 1.15
else:
    gravidade= 1.17
pesoPlaneta = peso*gravidade
print("\n\tO seu peso de {:.2f} kg, no planeta {:.0f} seria {:.2f}" .format(peso, planeta, pesoPlaneta))
