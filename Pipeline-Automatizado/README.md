<h1 align="left">Pipeline Automatizado de Limpeza de Dados</h1>

###

<p align="left">Este projeto implementa um pipeline automatizado para limpeza de dados brutos. Ele trata de valores ausentes, formata colunas e remove outliers, otimizando a preparação de dados para análises ou modelagens.</p>

###

<h2 align="left">Funcionalidades</h2>

###

<p align="left">> Carregamento de dados: Suporte para arquivos CSV.<br><br>> Tratamento de valores ausentes: Estratégias configuráveis, como preenchimento com média ou remoção de registros incompletos.<br><br>> Formatação de colunas: Padroniza nomes de colunas para letras minúsculas e substitui espaços por underscores.<br><br>> Detecção e remoção de outliers: Baseado no intervalo interquartil (IQR).<br><br>> Logs detalhados: Registra cada etapa da limpeza, erros e resultados.</p>

###

<h2 align="left">Pré-requisitos</h2>

###

<p align="left">> Python 3.8 ou superior<br><br>> Bibliotecas: pandas, numpy e pytest</p>

###

<h2 align="left">Como Usar:</h2>

###

<p align="left">1. Organize os arquivos de dados: Coloque os dados brutos na pasta data/bruto/ e ajuste o nome do arquivo no pipeline.py.<br><br>2. Execute o pipeline: python src/pipeline.py<br><br>3. Verifique os dados processados: O arquivo limpo estará disponível em data/processado/dados_limpos.csv. <br><br>4. Consulte logs em logs/limpeza_dados.log.<br><br>----------------------------------------------------------------------------------<br><br>Os testes garantem a robustez das funções do pipeline. <br>Para executar: pytest test_pipeline.py</p>

###
