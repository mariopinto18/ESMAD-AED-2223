"""
Imprime os primeiros n termos da 
sequência de Fibanacci
"""
ntermos = int(input("\n\n\n\t\t\t Nº de termos a imprimir:"))

if ntermos >= 1:        # trata 1º termo da sequencia
        termos = "0"
if ntermos >= 2:        # trata 2º termo da sequencia
        termos = termos + ", 1"
penultimo = 0
ultimo = 1
for i in range(3, ntermos+1):   # para todos a partir do 3º termo
    novo = penultimo+ultimo     # cada termo resulta da soma dos 2 anteriores
    termos = termos + ", " + str(novo)   # vai contactar os termos numa variavel de texto
                                         # para facilitar a impressão do resultado
    penultimo = ultimo
    ultimo = novo
print("\t\t\t Primeiros {0} termos da sequência de Fibonacci: {1}"  .format(ntermos, termos))


