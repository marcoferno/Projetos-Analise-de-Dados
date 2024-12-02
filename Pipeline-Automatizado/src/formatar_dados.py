def formatar_colunas(dados):
    dados.columns = [coluna.strip().lower().replace(" ", "_") for coluna in dados.columns]
    return dados
