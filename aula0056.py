"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '    Olha só que    , coisa interessante      '

lista_palavras = frase.split()  # Retorna uma lista, o separador é o espaço em branco
lista_frases = frase.split(',')  # Retorna a lista com o separador ','
print(lista_palavras)
print(lista_frases)

for palavra in lista_palavras:
    print(palavra)

print()

lista_frases_corrigida = []
for i, frase in enumerate(lista_frases):
    lista_frases_corrigida.append(lista_frases[i].strip())  # O método .strip() remove espaços em brancos


print(lista_frases_corrigida)

frases_unidas = '-'.join(lista_frases_corrigida)
print(frases_unidas)