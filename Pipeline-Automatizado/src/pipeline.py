import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
from src.carregar_dados import carregar_dados
from src.tratar_ausentes import tratar_valores_ausentes
from src.formatar_dados import formatar_colunas
from src.detectar_outliers import detectar_outliers

logging.basicConfig(filename='logs/limpeza_dados.log', level=logging.INFO)

def main():
    # Configuração dos caminhos
    caminho_entrada = "data/bruto/Lucro Real.csv"
    caminho_saida = "data/processado/dados_limpos.csv"

    # Carregar os dados
    dados = carregar_dados(caminho_entrada)
    if dados is None:
        print("Erro ao carregar os dados. Verifique o log.")
        return

    # Tratar valores ausentes
    dados = tratar_valores_ausentes(dados, estrategia="media")

    # Formatar colunas
    dados = formatar_colunas(dados)

    # Detectar e tratar outliers
    dados = detectar_outliers(dados)

    # Salvar dados limpos
    dados.to_csv(caminho_saida, index=False)
    logging.info(f"Pipeline concluído e dados salvos em {caminho_saida}")
    print(f"Pipeline concluído! Dados limpos salvos em: {caminho_saida}")

if __name__ == "__main__":
    main()
