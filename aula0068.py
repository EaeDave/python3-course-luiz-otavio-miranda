"""
Escopo de funções em Python
Escopo significa o local odne aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

nome = 'David'  # o valor de nome é 'David'
variavel_global = 600

def escopo():
    global variavel_global
    variavel_global = 300
    x = 1  # Essa variável está no escopo da função
    nome = 'Rodrigues'  # aqui o valor de nome é 'Rodrigues'


    def outra_funcao():
        y = 5  # Essa variável está no escopo interno de outra função
        print(y)
        print(nome)
        print(variavel_global)


    print(x)
    outra_funcao()

# print(x)  Nesse caso não seria possível acessar o valor de x, pois aqui já está
# no escopo do módulo "aula0068.py"

escopo()  # Aqui o nome é referente ao escopo a função
print(nome)  # Aqui o nome é referente ao escopo do módulo