nome = 'David Rodrigues'
altura = 1.70
peso = 70
imc = ...

# David Rodrigues tem 1.70 de altura,
# pesa 70 quilos e seu IMC é
# 24.22...

imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'  # f-string
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
