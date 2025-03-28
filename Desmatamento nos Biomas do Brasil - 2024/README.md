# Desmatamento nos Biomas do Brasil - 2024

![Imagem Principal](https://github.com/user-attachments/assets/f3055cd2-6541-4ab7-93e0-96fcc93d8e4b)

Este projeto analisa o desmatamento nos biomas brasileiros em 2024, utilizando dados ambientais e climáticos para identificar padrões críticos de degradação e incêndios florestais. O objetivo principal é fornecer informações úteis para embasar políticas públicas eficazes de preservação ambiental.

---

## Sobre o Projeto e Objetivos

A análise se concentra em fatores ambientais que influenciam o desmatamento e o risco de incêndios, tais como:

- Dias sem chuva
- Precipitação
- Risco de incêndios
- Potência Radiativa do Fogo (FRP)

Objetivos específicos:

- Identificar padrões críticos de desmatamento.
- Fornecer insights estratégicos para políticas públicas.
- Entender relações entre variáveis climáticas e o risco de incêndios.

---

## Dados

Os dados utilizados são provenientes do Portal de Dados Abertos do Governo Brasileiro e do INPE (Instituto Nacional de Pesquisas Espaciais). As variáveis-chave analisadas incluem:

- Média de dias sem chuva
- Média de precipitação
- Risco médio de incêndios
- FRP (Potência Radiativa do Fogo)

---

## Configuração do Ambiente

Para executar o projeto, certifique-se de ter instalado as seguintes bibliotecas:

![Imports](https://github.com/user-attachments/assets/513bd634-ae9b-4cf2-a88b-e4026399a4ae)

---

## Etapas da Análise

As etapas realizadas no projeto incluem:

1. **Preenchimento de dados nulos:** Mediana para numéricos e moda para categóricos.
2. **Conversão de Datas:** Padronização para análises temporais.
3. **Análise Estatística:** Distribuições e agrupamentos por estado e bioma.

---

## Visualizações

### Distribuições

- **Dias sem Chuva:**

![Distribuição Média de Dias sem Chuva](https://github.com/user-attachments/assets/536f003c-bf3e-485e-a80b-fa492ca03e8b)

- **Risco de Queimadas:**

![Distribuição Média Risco de Fogo](https://github.com/user-attachments/assets/9dc5f922-ddf8-41df-a874-aead927bfaf9)

### Rankings

- **Estados:**
  - Mais dias sem chuva
  
  ![Top 10 Estados sem Dias de Chuva](https://github.com/user-attachments/assets/a4f5ee8f-3d76-4c62-9038-4e42e19ff3a1)

  - Maior risco de queimadas
  
  ![Top 10 Estados com Risco de Queimada](https://github.com/user-attachments/assets/3a5ba00a-2e53-44f7-8a4f-cd4ac2bdde8e)

  - Maior média de precipitação
  
  ![Top 10 Estados com Precipitações](https://github.com/user-attachments/assets/b0b48583-4704-41f7-a8eb-20fbc0147d8d)

- **Biomas:**
  - Mais dias secos e risco de queimadas
  
  ![Top 10 Biomas sem Dias de Chuva](https://github.com/user-attachments/assets/8bfa79ad-32e0-483d-b66b-bbd324849362)
  ![Top 10 Biomas com Risco de Queimada](https://github.com/user-attachments/assets/8c252fad-446a-4ebc-ac50-81e8c3df972a)

  - Maiores precipitações
  
  ![Top 10 Biomas com Precipitações](https://github.com/user-attachments/assets/5a71fab6-9ba4-4c2f-875a-66e3efc66313)

### Correlações

- **Mapa de Calor das Variáveis:**

![Mapa de Calor Correlacionando as Variáveis](https://github.com/user-attachments/assets/d49f73c2-0bc5-4fda-ad4a-2e5e9d799e4b)

- **Dias sem chuva e risco de fogo:**

![Correlação Dias Sem Chuva e Risco de Fogo](https://github.com/user-attachments/assets/0643560e-e781-4419-8848-41b93502b437)

- **FRP e dias sem chuva:**

![Correlação FRP e Dias Sem Chuva](https://github.com/user-attachments/assets/4d4c89e3-67ec-4286-ba27-0ba76645d4a5)

- **FRP e risco de fogo:**

![Correlação FRP e Risco de Fogo](https://github.com/user-attachments/assets/abce27bf-eab4-4d61-be9b-963d43ed6d4f)

- **Evolução temporal do risco:**

![Evolução do Risco de Fogo](https://github.com/user-attachments/assets/1c803176-681d-4a83-9d27-512af5d0635a)

---

## Conclusões e Previsões

A análise revelou um cenário preocupante de aumento constante no risco de incêndios, particularmente no Cerrado e na Mata Atlântica, associados à seca prolongada e pressões antrópicas. A previsão para o último trimestre de 2024 indica uma permanência em torno de 90% de risco de incêndio.

![Gráfico de Previsão](https://github.com/user-attachments/assets/8b96bdbe-82c4-4044-8b88-6adacae328d8)

Essa situação demanda ações urgentes em políticas públicas para mitigar danos ambientais e garantir a sustentabilidade futura dos biomas brasileiros. A ciência de dados e o monitoramento contínuo são essenciais para a preservação ambiental e a gestão eficiente dos recursos naturais.
```

