# A função print() imprime algo na tela.
print(12, 34)  # Por padrão, a cada argumento passado, é separado por espaço vazio no output.
print(56, 78 , sep='-')  #  Aqui foi passado um argumento nomeado que escolhe o separador.

# \rn\rn -> CRLF
# \n -> LF

print('Não houve quebra', end=' ',)  # O parâmetro "end=" recebe como argumento o que acontecerá no final.
print('de linha')