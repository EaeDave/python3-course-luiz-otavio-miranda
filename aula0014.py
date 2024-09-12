a = 'A'
b = 'B'
c = 1.1
formato = 'a={}, b={}, c={:.2f}'.format(a, b, c)  # Método format()
formato_invertido = 'a={2:.2f}, b={1}, c={0}'.format(a, b, c)  # É possível alterar a posição indicando o index

print(formato)
print(formato_invertido)