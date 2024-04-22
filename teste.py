
import pandas as pd

# Define os nomes das colunas e os intervalos de posição dos dados no arquivo .txt
colunas = ['Nome', 'Data', 'Alt'] # Nome das colunas
posicoes = [(0, 6), (7, 9), (10, 21)] #Define os intervalos de posição das colunas

# Função para ler o arquivo .txt
def ler_arquivo_txt(caminho_arquivo, colunas, posicoes):
    # Cria um dicionário para armazenar os dados das colunas
    dados = {}
    for coluna, posicao in zip (colunas, posicoes):
        inicio, fim = posicao
        dados[coluna] = [slice_linha(inicio, fim, linha) for linha in open(caminho_arquivo)]

        # Converte o dicionário para um DataFrame
        df = pd.DataFrame(dados)
        return df
    
# Fatiar linha de acordo com a posição do arquivo
def slice_linha(inicio, fim, linha):
    return linha[inicio:fim].strip()

# Caminho do arquivo .txt
caminho_arquivo_txt = ''
# Chamar a função para ler o arquivo
df = ler_arquivo_txt(caminho_arquivo_txt, colunas, posicoes)
# Caminho para salvar o aquivo no Excel
caminho_arquivo_excel = ''
# Salva o DataFrame como um arquivo Excel
df.to_excel(caminho_arquivo_excel, index=False)
