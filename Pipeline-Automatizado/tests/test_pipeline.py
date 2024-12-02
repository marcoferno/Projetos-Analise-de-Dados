import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pandas as pd
import pytest
from src.carregar_dados import carregar_dados
from src.tratar_ausentes import tratar_valores_ausentes
from src.formatar_dados import formatar_colunas
from src.detectar_outliers import detectar_outliers

# Dados de exemplo para os testes
@pytest.fixture
def dados_exemplo():
    return pd.DataFrame({
        "Coluna 1": [1.0, 2.0, None, 4.0, 1000.0],
        "Coluna 2": [" A ", "B", None, "C", "D"],
        "Coluna 3": [10.5, 20.1, 15.2, None, 50.8]
    })

def test_carregar_dados(tmp_path):
    # Cria um arquivo temporário de exemplo
    caminho_arquivo = tmp_path / "dados_teste.csv"
    dados_exemplo = pd.DataFrame({
        "Coluna 1": [1, 2, 3],
        "Coluna 2": ["A", "B", "C"]
    })
    dados_exemplo.to_csv(caminho_arquivo, index=False)

    # Testa a função carregar_dados
    dados_carregados = carregar_dados(caminho_arquivo)
    assert not dados_carregados.empty
    assert list(dados_carregados.columns) == ["Coluna 1", "Coluna 2"]

def test_tratar_valores_ausentes_media(dados_exemplo):
    # Testa a estratégia de preencher com a média
    dados_tratados = tratar_valores_ausentes(dados_exemplo, estrategia="media")
    
    # Verifica se não há valores ausentes em colunas numéricas
    assert not dados_tratados.select_dtypes(include=['number']).isnull().any().any(), \
        "Existem valores ausentes nas colunas numéricas após o tratamento"
    
    # Verifica se a média foi aplicada corretamente
    media_coluna_1 = dados_exemplo["Coluna 1"].mean()
    assert dados_tratados.loc[2, "Coluna 1"] == media_coluna_1, \
        "O valor ausente na Coluna 1 não foi preenchido corretamente com a média"
    
    media_coluna_3 = dados_exemplo["Coluna 3"].mean()
    assert dados_tratados.loc[3, "Coluna 3"] == media_coluna_3, \
        "O valor ausente na Coluna 3 não foi preenchido corretamente com a média"

def test_tratar_valores_ausentes_remover(dados_exemplo):
    # Testa a estratégia de remover valores ausentes
    dados_tratados = tratar_valores_ausentes(dados_exemplo, estrategia="remover")
    assert dados_tratados.isnull().sum().sum() == 0
    assert len(dados_tratados) < len(dados_exemplo)  # Linhas devem ter sido removidas

def test_formatar_colunas(dados_exemplo):
    # Testa a formatação de colunas
    dados_formatados = formatar_colunas(dados_exemplo)
    assert all("_" in col for col in dados_formatados.columns)  # Verifica se há "_" nos nomes
    assert all(col.islower() for col in dados_formatados.columns)  # Verifica se estão em letras minúsculas

def test_detectar_outliers(dados_exemplo):
    # Testa a detecção e remoção de outliers
    dados_sem_outliers = detectar_outliers(dados_exemplo, limite=1.5)
    assert len(dados_sem_outliers) < len(dados_exemplo)  # Linhas com outliers devem ter sido removidas
