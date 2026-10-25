import pandas as pd
import glob
import os

# 1. Defina o caminho onde estão os arquivos CSV baixados
# Como você usa Linux (Pop!_OS), o caminho será algo como '/home/usuario/Downloads/tce_dados/*.csv'
caminho_arquivos = './licitacoes/*.csv'
arquivos = glob.glob(caminho_arquivos)

# Lista para armazenar os DataFrames de cada mês
lista_df = []

# 2. Ler e concatenar todos os arquivos dos meses (Agosto a Dezembro)
for arquivo in arquivos:
    print(f"Lendo: {os.path.basename(arquivo)}")
    try:
        # TCE-SP costuma usar separador ';' e encoding 'latin1' ou 'cp1252'
        df_mes = pd.read_csv(arquivo, sep=';', encoding='latin1', low_memory=False)
        lista_df.append(df_mes)
    except Exception as e:
        print(f"Erro ao ler {arquivo}: {e}")

# Concatena todos os meses em um único DataFrame
df_completo = pd.concat(lista_df, ignore_index=True)
print(f"\nTotal de registros antes do filtro: {len(df_completo)}")

# 3. Identifique o nome correto da coluna de Órgão/Entidade
# Descomente a linha abaixo na primeira execução para ver o nome exato da coluna no seu CSV
# print(df_completo.columns.tolist())

coluna_orgao = 'Entidade' # Substitua pelo nome exato que aparecer no seu arquivo (ex: 'Nome da Entidade', 'Unidade Gestora')

# 4. Criar o filtro com palavras-chave relacionadas à educação (case-insensitive)
# O '|' funciona como o operador lógico OR
palavras_chave = 'EDUCACAO|EDUCAÇÃO|ENSINO|ESCOLA|FDE|FUNDEB|UNIVERSIDADE|FACULDADE|COLEGIO|COLÉGIO'

# Filtra mantendo apenas as linhas onde a coluna do órgão contém alguma das palavras-chave
# na=False evita erros com linhas vazias
df_educacao = df_completo[df_completo[coluna_orgao].str.contains(palavras_chave, case=False, na=False, regex=True)]

print(f"Total de registros após o filtro (apenas Educação): {len(df_educacao)}")

# 5. Salvar o novo conjunto de dados limpo
arquivo_saida = 'licitacoes_educacao_ago_dez.csv'
df_educacao.to_csv(arquivo_saida, sep=';', encoding='utf-8', index=False)
print(f"\nArquivo salvo com sucesso: {arquivo_saida}")