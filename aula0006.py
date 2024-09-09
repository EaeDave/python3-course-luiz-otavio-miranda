# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print('1', type('1'))  # str
print(int('1'), type(int('1')))  # int

print(bool(''))  # str vazia é considerada False
print(bool(' '))  # um espaço vazio é considerado True
print(str(11) + 'b')  # typecasting de int para str