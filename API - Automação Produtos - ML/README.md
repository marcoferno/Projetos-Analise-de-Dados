
# Automatização de Anúncios - Mercado Livre

![Image](https://github.com/user-attachments/assets/9a345bef-db1a-4f75-bca1-23c2ea63aa02)

Este projeto desenvolvido com Google Apps Script automatiza a extração e organização de informações sobre anúncios do Mercado Livre, integrando diretamente a API do Mercado Livre ao Google Sheets. O script coleta automaticamente dados essenciais como preços, categorias, disponibilidade e detalhes do envio, proporcionando um método eficiente para análise e monitoramento de produtos.

### Documentação Oficial da API:
[API Mercado Livre](https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br)

---

## Problema e Objetivo

Coletar manualmente informações detalhadas de múltiplos anúncios no Mercado Livre é demorado, trabalhoso e suscetível a erros humanos. Este projeto automatiza esse processo, garantindo precisão, agilidade e atualizações contínuas sem intervenção manual.

---

## Estrutura da Solução

### Google Sheets

Esta planilha foi organizada em três abas distintas:

- **Token**: Armazena o token OAuth 2.0 necessário para autenticar requisições na API do Mercado Livre.
- **Anúncios**: Guarda informações detalhadas dos produtos anunciados:
  - ID do Anúncio
  - Título
  - Categoria
  - Estado (novo/usado)
  - Preço
  - Disponibilidade
  - Vendedor
  - Data de Publicação

- **Valores**: Realiza análises financeiras sobre os produtos vendidos:
  - ID do Anúncio (referência cruzada)
  - Preço de Venda
  - Custo do Produto
  - Lucro
  - Data da Venda

### Google Apps Script

#### Conexão com Abas da Planilha

O script estabelece conexões diretas com as diferentes abas mencionadas acima para armazenar os dados obtidos da API.

![Aouth](https://github.com/user-attachments/assets/5341e035-cd2b-4517-b56b-452b9049d521)

#### Autenticação e Gestão do Token (OAuth 2.0)

O script autentica as requisições com segurança através do fluxo OAuth 2.0, atualizando automaticamente o token quando necessário.

![Aouth2](https://github.com/user-attachments/assets/07c07215-bafa-42c2-b4ae-32e30890ef38)

#### Processo de Busca e Extração de Dados

- **Requisição Principal**: O script realiza buscas com base em termos definidos na planilha, obtendo anúncios relevantes.

![Função Busca](https://github.com/user-attachments/assets/723458d7-caf4-4286-9a8a-8cfaa0263129)

- **Requisições Secundárias**: Para cada anúncio, realiza requisições adicionais para obter informações específicas como taxas aplicáveis e opções de envio.

![Função Busca 2](https://github.com/user-attachments/assets/456c1c37-214a-4e0d-b3dc-45d5f14c0c02)
![função busca 3](https://github.com/user-attachments/assets/4d93d4b2-360a-4f8f-b078-d34928c658cd)

#### Tratamento de Erros

O script conta com mecanismos robustos de tratamento de erros, garantindo que falhas nas requisições não interrompam a execução geral e sejam devidamente registradas na planilha ou logs.

---

## Benefícios da Aplicação

- **Eficiência**: Automação total na coleta de grandes volumes de dados rapidamente.
- **Precisão**: Reduz significativamente erros em comparação à coleta manual.
- **Escalabilidade**: Facilmente adaptável para aumentar a quantidade de anúncios ou adicionar novos dados conforme necessário.

---

## Considerações Finais e Resultados

Registro detalhado das requisições à API para busca de produtos, anúncios, precificação e custos.

![Retorno Info](https://github.com/user-attachments/assets/4459a764-4fba-441f-b55c-745496f1112c)

Registro detalhado das requisições à API para precificação aprofundada dos produtos.

![Taxas](https://github.com/user-attachments/assets/9657d218-eaaf-4a09-83fb-eb38fb6b58ed)

Este projeto é uma solução prática e robusta para estudantes e profissionais que buscam eficiência na coleta e análise de dados do Mercado Livre. Sua implementação permite integração com diversas ferramentas e plataformas como Python, PHP, Power BI e Excel, ampliando sua aplicabilidade e facilitando insights estratégicos para tomadas de decisão.
```

