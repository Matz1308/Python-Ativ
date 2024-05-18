# Boas Vindas
print('Bem-vindo a loja Matheus Santos')

# Captura o valor unitário
valor_unitario = float(input('Entre com o valor do produto: '))

# Captura a quantidade
quantidade = int(input('Entre com a quantidade do produto: '))

# Calcula o valor total
valor_total = valor_unitario * quantidade

# Criação da variavel pra porcentagem de desconto e do valor final
desconto = 0
valor_final = 0

# Validação das condicionais do valor de desconto
if (valor_total >= 2500 and valor_total < 6000):
    desconto = 0.04

elif (valor_total >= 6000 and valor_total < 10000):
    desconto = 0.07

elif (valor_total >= 10000):
    desconto = 0.11

# cálculo do valor líquido
valor_final = valor_total - (valor_total * desconto)

# Exibir o valor sem desconto
print(f'O valor SEM desconto: {valor_total:.2f}')

# Se tiver um desconto, sera exibido o desconto e o valor líquido.
if (desconto > 0):
    print(f'O valor COM desconto de {(desconto * 100):.0f}%: {valor_final:.2f}')
else:
    print('Não houve desconto nesta compra')