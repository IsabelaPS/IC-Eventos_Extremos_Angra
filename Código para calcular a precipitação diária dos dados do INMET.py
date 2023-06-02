# Código para pegar os dados de precipitação do INMET (que são horários) e transformar em dados de precipitação diários.


import pandas as pd

# Carregar o arquivo Excel
tabela_excel = pd.read_excel('INMET_ANGRA_DOS_REIS_2023.xlsx')

# Eliminar datas repetidas e selecionar apenas a primeira coluna
primeira_coluna = tabela_excel.iloc[:, 0].drop_duplicates()

# Criar um novo DataFrame para armazenar os resultados
resultado = pd.DataFrame(columns=['Data', 'Soma'])

# Iterar sobre as datas únicas
for data in primeira_coluna:
    # Obter as 24 linhas correspondentes à data
    linhas = tabela_excel[tabela_excel.iloc[:, 0] == data].iloc[:24, 2]
    
    # Somar os dados das 24 linhas
    soma = linhas.sum()
    
    # Adicionar a data e a soma ao DataFrame resultado
    resultado = pd.concat([resultado, pd.DataFrame({'Data': [data], 'Soma': [soma]})], ignore_index=True)

# Salvar o DataFrame em um novo arquivo Excel
resultado.to_excel('INMET_ANGRA_DOS_REIS_2023_Python.xlsx', index=False)
