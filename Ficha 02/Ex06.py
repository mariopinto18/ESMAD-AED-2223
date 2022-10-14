""" 
Simulador de esforço cardíaco
Nas mulheres FCM = 226 - idade.
Nos homens FCM=  220 - idade
 """

genero = input("\n\n\n\tGénero(M/F): ")
idade = int(input("\n\n\tIdade: "))
if genero.upper() == "F":
    fcm = 226-idade
else:
    fcm = 220-idade
print("\n\t\t\tFCM= {0} bpm" .format(fcm))

