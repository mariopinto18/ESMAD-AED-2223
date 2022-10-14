#Converte segundos em horas, muinutos e segundos

tempo= int(input("Indique o tempo em segundos:"))

horas= int(tempo/3600)   # converte em horas
tempo= tempo - horas*3600       # subtrai as horas ao tempo inicial

minutos = int(tempo/60)  # converte em minutos
tempo = tempo - minutos*60       # subtrai os minutos ao tempo disponível, sobrando os segundos


print("{0} horas, {1} minutos, {2} segundos".format(horas, minutos, tempo) )
