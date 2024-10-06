"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'David'.__iter__()  # iter('David') -> Iter é objeto que sabe entregar um valor por vez.
# O método __next__() entrega o próximo valor do iter.
print(texto.__next__())  # D  
print(texto.__next__())  # a
print(texto.__next__())  # v
print(texto.__next__())  # i
print(texto.__next__(), end='\n\n')  # d
# print(texto.__next__())  # Exception StopIteration

texto_2 = 'David'  # Iterável
iterador = texto_2.__iter__()  # Iterador

# for letra in texto
while True:
    try:
        print(iterador.__next__())
    except StopIteration:
        break
