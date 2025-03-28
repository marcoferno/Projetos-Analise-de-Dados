# Pipeline Automatizado de Limpeza de Dados

Este projeto fornece uma solução automatizada para limpeza e preparação de dados brutos para análises ou modelagens. O pipeline implementado é eficiente para tratar valores ausentes, padronizar colunas e remover outliers (valores extremos), garantindo a qualidade dos dados utilizados.

---

## Funcionalidades

- **Carregamento de Dados:** Suporta arquivos CSV.
- **Tratamento de Valores Ausentes:** Pode preencher valores faltantes com a média ou remover registros incompletos.
- **Formatação de Colunas:** Padroniza nomes das colunas para letras minúsculas e substitui espaços por underscores (_).
- **Detecção e Remoção de Outliers:** Utiliza o método de intervalo interquartil (IQR) para identificar e remover valores extremos.
- **Logs Detalhados:** Cada etapa do processo é registrada em logs detalhados para facilitar a auditoria e resolução de problemas.

---

## Pré-requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias:
  - pandas
  - numpy
  - pytest

Instale utilizando o comando:

```bash
pip install pandas numpy pytest
```

---

## Como Operar o Pipeline

**1. Organização dos Dados:**

- Crie uma pasta com o nome `data/bruto/` e coloque nela o arquivo CSV com seus dados brutos.
- Atualize o nome do arquivo no script localizado em `src/pipeline.py`.

**2. Executar o Pipeline:**

Abra o terminal na pasta raiz do projeto e execute:

```bash
python src/pipeline.py
```

Este comando realiza:
- Leitura dos dados brutos.
- Limpeza automatizada.
- Salva os dados processados na pasta `data/processado/` com o nome `dados_limpos.csv`.

**3. Verificação dos Resultados:**

- Confira o resultado em: `data/processado/dados_limpos.csv`
- Logs do processo estarão em: `logs/limpeza_dados.log`

**4. Execução dos Testes:**

Os testes automatizados garantem a robustez e eficácia do pipeline. Para executar, utilize:

```bash
pytest test_pipeline.py
```

---

## Explicação Didática

Ao executar o pipeline, o seguinte processo ocorre automaticamente:

- **Carregamento dos dados:** O arquivo bruto é lido, permitindo o início do tratamento.
- **Tratamento de valores ausentes:** Dados faltantes são preenchidos automaticamente com valores calculados (média ou moda), garantindo a integridade dos dados.
- **Padronização:** Todos os nomes de colunas são ajustados para um formato uniforme e fácil de manipular.
- **Remoção de outliers:** Dados que podem distorcer análises (outliers) são identificados e removidos utilizando critérios estatísticos.
- **Registro de etapas:** Cada passo é registrado detalhadamente em um arquivo de log, facilitando o acompanhamento e a identificação de erros ou melhorias necessárias.

Esses processos garantem que seus dados estejam preparados adequadamente, economizando tempo e garantindo análises mais precisas e confiáveis.
```

