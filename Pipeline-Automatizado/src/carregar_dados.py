import pandas as pd
import logging

def carregar_dados(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        logging.info(f"Dados carregados de {caminho_arquivo}")
        return dados
    except Exception as erro:
        logging.error(f"Erro ao carregar dados: {erro}")
        return None
