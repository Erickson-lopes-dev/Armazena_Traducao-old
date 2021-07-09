from csv import *
import os


class ArmazenaTraducao_csv:
    # construtor
    def __init__(self, nome):
        # variável com nome do arquivo
        self.nome_arquivo = nome
        # variável com o caminho do arquivo de onde o programa esteja sendo executado
        self.path_arquivo = os.path.join(os.getcwd(), self.nome_arquivo)
        # função que verifica a existência do arquivo, caso não exista ele cria
        self.arquivo_con()
        # interface do sistema
        self.interface()

    def interface(self):
        while True:

            os.system('cls')
            print('1 - Procurar por uma palavra.\n'
                  '2 - Exibir todas as palavras\n'
                  '3 - Adicionar uma palavra.\n'
                  '0 - Sair:')
            opc = input('Digite sua opção: ')

            if opc == '0':
                break

            elif opc == '1':
                palavra = input('Digite sua pesquisa (Palavra em inglês):')
                self.pesquisar_palavra(palavra)

            elif opc == '2':
                self.exibir_tudo()

            elif opc == '3':
                palavra = input('Digite a Palavra em inglês: ')
                traducao = input('Digite sua tradução em português')
                self.adicionar_traducao(palavra, traducao)
            else:
                print('Opção inválida!\n')

            opc = input('Deseja voltar ao menu? [S/N]: ')
            if opc.upper() == 'S':
                continue
            elif opc.upper() == 'N':
                break

    def arquivo_con(self):
        if not os.path.exists(self.path_arquivo):
            print('Criando arquivo inesistente')

            try:
                with open(self.path_arquivo, 'w', encoding='utf-8') as arquivo_csv:
                    colunas = ['Palavra', 'Tradução']
                    escreve = DictWriter(arquivo_csv,
                                         fieldnames=colunas,
                                         delimiter=',',
                                         lineterminator='\n')
                    escreve.writeheader()
            except Exception as err:
                print(err)

    def adicionar_traducao(self, palavra, traducao):
        with open(self.path_arquivo, 'a', encoding='utf-8') as arquivo_csv:
            escrever = writer(arquivo_csv,
                              delimiter=',',
                              lineterminator='\n')

            escrever.writerow([palavra, traducao])

    def exibir_tudo(self):
        with open(self.path_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = reader(arquivo_csv, delimiter=',')

            for linha in leitor:
                print(linha)

    def pesquisar_palavra(self, palavra):
        with open(self.path_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = reader(arquivo_csv, delimiter=',')

            for linha in leitor:
                if palavra.upper() in linha[0].upper():
                    print(linha)


if __name__ == '__main__':
    csv = ArmazenaTraducao_csv('arquivo.csv')
