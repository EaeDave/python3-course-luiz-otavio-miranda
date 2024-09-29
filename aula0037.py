"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 30:
        continue  # Essa etapa vai ser pulada

    if contador > 10 and contador <= 20:
        continue

    
    print(contador)


    if contador == 40:
        break