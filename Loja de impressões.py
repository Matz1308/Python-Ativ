# Declaração da função escolha_servico
def escolha_servico() -> float:
    # Inicio do loop
    while True:
        # Montagem das opções desejadas
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização - R$ 1,10')
        print('ICO - Impressão Colorida - R$ 1,00')
        print('IPB - Impressão Preto e Branco - R$ 0,40')
        print('FOT - Fotocópia - R$ 0,20')

        print('\n')
        # Peço para escolher a opção
        servico = str(input('Escolha >> '))

        # Avalio a opção selecionada e retorno o valor do serviço por página
        try:
            if (servico.lower() == 'dig'):
                return 1.1
            
            elif (servico.lower() == 'ico'):
                return 1
            
            elif (servico.lower() == 'ipb'):
                return 0.4
                    
            elif (servico.lower() == 'fot'):
                return 0.2
        
            else:
                # Se não selecionado uma opção correta, aviso ao usuário
                print('\n')
                print('Escolha inválida, entre com o tipo de serviço novamente')
        except ValueError:
            # Se, por acaso, o usuário digitar um valor fora do padrão
            print('Insira um valor texto válido')    
        
        print('\n')

# Declaro a função num_pagina
def num_pagina() -> int:
    # Inicio do loop
    while True:
        try:
            # Pergunto a quantidade de páginas
            paginas = int(input('Entre com o número de páginas: '))

            # Avalio se está dentro do range aceitavel (mais que zero e menos que 20 mil)
            if 0 < paginas < 20000:
                # Retorno o valor de páginas digitada
                return paginas
            else:
                # Exibo um erro se não estiver no range
                print('Não aceitamos tantas páginas de uma vez (máximo 20 mil páginas)')
        except ValueError:
            # Se inserir um texto, exibo uma mensagem de erro
            print('Insira um valor numérico válido')
        
        print('\n')
        print('Por favor, entre com o número de páginas novamente')
        

# Declaração da função servico_extra
def servico_extra() -> int:
    while True:
        # Montagem das opções na tela para o usuário
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação Simples - R$ 15,00')
        print('2 - Encadernação Capa Dura - R$ 40,00')
        print('0 - Não desejo mais nada')

        # Solicito a opção ao usuário e retorno o valor do serviço extra
        try:
            opcao = int(input('>> '))

            if (opcao == 1):
                return 15

            elif (opcao == 2):
                return 40
            
            elif (opcao == 0):
                return 0

            else:
                # Se selecionado uma opção incorreta, exibo um erro
                print('Digite um opção válida')

        except ValueError:
            # Se digitado um valor que não seja numérico, exibo um erro
            print('Insira um valor numérico válido')
            
        print('\n')

    
# Função principal
def main():
    # Boas Vindas
    print('Bem vindo a Copiadora do Matheus Santos')
    print('\n')

    # Retorna o valor da função escolha_servico - retorno o valor do serviço selecionado.
    servico = escolha_servico()
    print('\n')
    # Retorna o valor da função num_pagina - retorno o número de páginas
    paginas = num_pagina()

    # Criação da variável de desconto
    desconto = float(0)

    # Seleciona a porcentagem de desconto baseado na quantidade de paginas escolhidas
    if (paginas >= 20 and paginas < 200):
        desconto = 0.15
    elif (paginas >= 200 and paginas < 2000):
        desconto = 0.2
    elif (paginas >= 2000 and paginas < 20000):
        desconto = 0.25

    print('\n')

    # Retorna o valor da função servico_extra - retorno o valor do serviço extra selecionado
    extra = servico_extra()

    print('\n')

    # Faço o calculo da soma do serviço por página, mais o serviço extra.
    soma = ((servico * paginas) + extra)
    print(f'Total: R$ {soma:.2f} (Serviço: R$ {servico:.2f} * {paginas} Páginas + Extra R$ {extra:.2f})')

    # Se tiver desconto
    if (desconto > 0):
        # Faço o calculo do valor líquido e mostro ele, do desconto e do valor de desconto
        total = soma - (soma * desconto)
        print(f'Desconto de {(desconto * 100):.0f}% aplicado, valor de desconto de R$ {(soma * desconto):.2f}')
        print(f'Valor a Pagar: R$ {total:.2f}')


# Executa tudo
main()