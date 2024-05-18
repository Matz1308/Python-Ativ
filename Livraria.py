id_global = int(0)
lista_livro = []

def exibir_livro(livro: dict):
    print(f"Id: {livro['id']}")
    print(f"Nome: {livro['nome']}")
    print(f"Autor: {livro['autor']}")
    print(f"Editora: {livro['editora']}")
    print('\n')

def cadastrar_livro(id: int):
    print('\n')
    print('--- CADASTRAR LIVRO ---')
    print('\n')
    novo_livro = {
        'id': id,
        'nome': str(''),
        'autor': str(''),
        'editora': str(''),
    }
    
    while True:
        nome = input('Nome do Livro: ')

        if (nome and nome != ''):
            novo_livro['nome'] = nome
        else:
            print('Insira um nome válido')
            continue

        autor = input('Autor do Livro: ')

        if (autor and autor != ''):
            novo_livro['autor'] = autor
        else:
            print('Insira um autor válido')
            continue

        editora = input('Editora do Livro: ')

        if (autor and autor != ''):
            novo_livro['editora'] = editora
        else:
            print('Insira uma editora válida')
            continue
        
        print('\n')
        print('Novo livro cadastrado!')
        print('\n')
        exibir_livro(novo_livro)

        global id_global
        id_global += 1

        return novo_livro

def consultar_livro():
    while True:
        print('--- CONSULTAR LIVRO(S) ---')
        print('\n')
        print('Escolha a opção desejada:')
        print('1 - Todos os Livros Disponíveis')
        print('2 - Consultar Livro por ID')
        print('3 - Consultar Livro por Autor')
        print('4 - Retornar')
        print('\n')

        try:
            opcao = int(input('>> '))

            if (4 >= opcao >= 1):
                print('\n')

                if (opcao == 1):
                    print('--- TODOS ---')
                    for i in range(0, len(lista_livro), 1):
                        exibir_livro(lista_livro[i])
                    
                    print('---------------------')
                    continue
                        
                elif (opcao == 2):
                    try:
                        index = int(input('Digite o id do Livro: '))
                        livro = next(filter(lambda livro: int(livro['id']) == index, lista_livro))

                        if (livro):
                            exibir_livro(livro)

                        else:
                            print('Não foi encontrado informação a respeito deste livro')

                    except ValueError:
                        print('Digite um valor numérico válido')

                    except IndexError:
                        print('Não foi encontrado um livro com esse id')
                        print('\n')

                    continue

                elif (opcao == 3):
                    autor_search = input('Digite o autor do(s) livro(s): ')

                    print(f'--- BUSCA POR AUTOR {autor_search} ---')

                    lista_filtrada = list(filter(lambda livro: str(livro['autor']).lower() == autor_search.lower(), lista_livro))

                    if (len(lista_filtrada) > 0):
                        for i in range(0, len(lista_filtrada), 1):
                            livro = lista_filtrada[i]
                            if(str(livro['autor']).lower() == autor_search.lower()):
                                exibir_livro(lista_filtrada[i])

                    else:
                        print('Não foi encontrado livros deste(a) autor(a)')


                    print('---------------------')
                    continue

                elif (opcao == 4):
                    break

            else:
                print('Digite uma opção válida.')
                print('\n')
                continue
        
        except ValueError:
            print('Digite um número válido para acessar as opções')
            continue


def remover_livro():
    if(len(lista_livro) == 0):
        print('\n')
        print('Não há livros para serem removidos')
        print('\n')
        return

    while True:
        print('--- REMOVER LIVRO ---')
        print('\n')
        try:
            index = int(input('Digite o id do Livro a ser removido: '))
            livro_index = next((i for i, livro in enumerate(lista_livro) if livro["id"] == index), None)
            print(livro_index)

            if (lista_livro[livro_index]):
                del lista_livro[livro_index]
                print('Livro removido com sucesso!')
                print('\n')
                break
            else:
                print('Não foi encontrado um livro com esse id')
                print('\n')

        except IndexError:
            print('Não foi encontrado um livro com esse id')
            print('\n')

        except ValueError:
            print('Digite um valor numérico válido')
            print('\n')

        except:
            print('Não foi encontrado um livro com esse id')
            print('\n')
    
        

def main():

    while True:
        print('Bem-vindo a Livraria do Matheus Santos')
        print('\n')
        print(f'Atualmente temos {len(lista_livro)} livro(s) em nossa livraria')
        print('\n')
        print('---------------------------------')
        print('-------- MENU PRINCIPAL ---------')
        print('---------------------------------')
        print('\n')
        print('Escolha a opção desejada:')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Remover Livro')
        print('4 - Sair')
        print('\n')

        try:
            opcao = int(input('>> '))

            if (4 >= opcao >= 1):
                
                if (opcao == 1):
                    lista_livro.append(cadastrar_livro(id_global))
                
                elif (opcao == 2):
                    consultar_livro()

                elif (opcao == 3):
                    remover_livro()

                elif (opcao == 4):
                    print('\n')
                    print('---------------------------------')
                    print('----------- Até mais!! ----------')
                    print('---------------------------------')
                    break

                continue
            else:
                print('Digite uma opção válida.')
                print('\n')
                continue
        
        except ValueError:
            print('Digite um número válido para acessar as opções')
            continue

main()
