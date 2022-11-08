
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def maior_faturacao(l_fact):
    """
     return the month of higher value 
    """
    maior = max(l_fact)
    pos = l_fact.index(maior)
    mes = meses[pos]
    return mes

def menor_faturacao(l_fact):
       # Função que devolve o mes de menor faturacao
    menor = min(l_fact)
    pos = l_fact.index(menor)
    mes = meses[pos]
    return mes

def media_faturacao(l_fact):
       # Função que devolve a media de faturacao mensal
    return sum(l_fact) / len(l_fact)



# Inicio do programa-----
l_fact = []
for i in range(12):         # ciclo para ler a faturação dos 12 meses
    while True:       # ciclo para validar a inserção de valores válidos
        try:
            valor = int(input("Faturação do mês {0} : " .format(meses[i])))
        except ValueError:
            print("O valor inserido é inválido. Pf tente novamente!")
        else:
            l_fact.append(valor)                # Acrescenta à lista de faturacao
            break
mes_maior = maior_faturacao(l_fact)
mes_menor = menor_faturacao(l_fact)
media = media_faturacao(l_fact)

print("\n Mês de maior faturação  :", mes_maior)
print("\nMês de menor faturação  :", mes_menor)
print("\n Valor médio de faturação {:.2f}:" .format(media))


