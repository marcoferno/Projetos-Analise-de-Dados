import numpy as np

def detectar_outliers(dados, limite=1.5):
    colunas_numericas = dados.select_dtypes(include=[np.number])
    for coluna in colunas_numericas.columns:
        q1, q3 = np.percentile(dados[coluna].dropna(), [25, 75])
        iqr = q3 - q1
        limite_inferior = q1 - limite * iqr
        limite_superior = q3 + limite * iqr
        dados = dados[(dados[coluna] >= limite_inferior) & (dados[coluna] <= limite_superior)]
    return dados