def tratar_valores_ausentes(dados, estrategia="media"):
    if estrategia == "media":
        # Preenche valores ausentes apenas em colunas numéricas
        dados_numericos = dados.select_dtypes(include=['number'])
        return dados.fillna(dados_numericos.mean())
    elif estrategia == "mediana":
        # Preenche valores ausentes apenas em colunas numéricas
        dados_numericos = dados.select_dtypes(include=['number'])
        return dados.fillna(dados_numericos.median())
    elif estrategia == "remover":
        return dados.dropna()
    else:
        raise ValueError(f"Estratégia desconhecida: {estrategia}")