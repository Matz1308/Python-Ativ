# Boas vindas
print('Bem-vindo a Loja de sorvetes do Matheus Santos')
print('--------------------------------------------')
print('---------------Cardápio---------------------')
print('---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---')
print('---|    P    |   R$  9.00   | R$ 11.00  |---')
print('---|    M    |   R$ 14.00   | R$ 16.00  |---')
print('---|    G    |   R$ 18.00   | R$ 20.00  |---')
print('--------------------------------------------')

# Criação da variável soma
soma_valor = 0

# Criação da var para strings que se repetem.
tamanho_desejado_str = 'Entre com o tamanho desejado (P/M/G)'
tamanho_invalido_str = 'Tamanho inválido. Tente novamente'

# Inicio do loop
while True:
    print('\n')
    # Pergunto qual o sabor desejado
    produto = input('Entre com o sabor desejado (CP/AC): ')

    # Avalio se foi digitado cupuaçu
    if (produto.lower() == 'cp'):
        # Pergunto o tamanho desejado e faço a soma do valor
        tamanho = input(f'{tamanho_desejado_str}: ')
        if (tamanho.lower() == 'p'):
            soma_valor += 9

        elif (tamanho.lower() == 'm'):
            soma_valor += 14

        elif (tamanho.lower() == 'g'):
            soma_valor += 18

        else:
            # Se for inserido um tamanho inválido, eu exibo a mensagem de erro
            print(tamanho_invalido_str)
            continue

        # Exibo qual produto e tamanho foi adicionado
        print(f'Cupuaçu {tamanho.upper()} adicionado')

    # Avalio se foi digitado açaí
    elif (produto.lower() == 'ac'):
        # Pergunto o tamanho desejado e somo o valor
        tamanho = input(f'{tamanho_desejado_str}: ')

        if (tamanho.lower() == 'p'):
            soma_valor += 11

        elif (tamanho.lower() == 'm'):
            soma_valor += 16

        elif (tamanho.lower() == 'g'):
            soma_valor += 20

        else:
            # Se for inserido um tamanho inválido, eu exibo a mensagem de erro
            print(tamanho_invalido_str)
            continue

        # Exibo qual produto e tamanho foi adicionado
        print(f'Açai {tamanho.upper()} adicionado')

    else:
        # Se for inserido um produto inválido, eu exibo a mensagem de erro
        print('Sabor inválido. Tente novamente')
        continue

    print('\n')
    # Pergunto se deseja adicionar mais
    continuar = input('Deseja mais alguma coisa? (S/N): ')

    if (continuar.lower() == 's'):
        # Continua
        continue
    else:
        # Finaliza
        break
        
# Finalizo o algoritmo exibindo o valor a ser pago
print('\n')
print(f'O valor total a ser pago: R$ {soma_valor:.2f}')