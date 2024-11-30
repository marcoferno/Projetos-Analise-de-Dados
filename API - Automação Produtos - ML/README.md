<h1 align="left">Automatização de Anúncios Mercado Livre</h1>

<p align="left">Este projeto é uma implementação em Google Apps Script, projetada para automatizar a extração e organização de dados de anúncios no Mercado Livre, utilizando as capacidades da API do Mercado Livre, o script realiza requisições para coletar informações essenciais, como preços, categorias, e detalhes de envio, e armazena essas informações diretamente em uma planilha do Google Sheets. Esta solução é ideal para otimizar processos de coleta de dados para análise e monitoramento de produtos online.</p>

<p align="left"> Documentação da API do Mercado Livre: https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br</p>

###

<h2 align="left">Problemas e Desafios do Projeto</h2>

###

<p align="left">Coletar manualmente informações detalhadas de múltiplos anúncios no Mercado Livre é uma tarefa que consome tempo e está sujeita a erros humanos. Este script automatiza todo o processo, eliminando a necessidade de intervenção manual e assegurando que os dados sejam coletados de maneira eficiente e precisa, com atualizações automáticas conforme necessário.</p>

###

<h2 align="left">Etapas do Projeto</h2>

###

- Preparação da planilha no Google Sheets<br>

Esta planilha foi organizada em três abas distintas: "Token", "Anúncios" e "Valores", cada uma desempenhando um papel fundamental na coleta, organização e análise de dados relacionados aos produtos anunciados e vendidos no Mercado Livre.<br><br>A primeira aba, Token, é dedicada ao armazenamento do token de autenticação necessário para acessar a API do Mercado Livre, este token é um valor único que garante que as requisições à API sejam autorizadas, permitindo a coleta de dados de maneira segura e confiável.<br><br>A aba, Anúncios foi criada para agrupar informações detalhadas sobre os produtos anunciados. Os principais campos desta aba incluem: <br><br>- ID do Anúncio (Identificador de cada produto)<br>- Título (nome do produto)<br>- Categoria (classificação do produto no mercado) <br>- Estado (indica se o produto é novo, usado, etc.) <br>- Preço (valor atual do produto)<br>- Disponibilidade (quantidade disponível para venda)<br>- Vendedor (dados do vendedor)<br>- Data de Publicação (data em que o anúncio foi publicado). <br><br>Esta organização permite uma visão abrangente dos produtos disponíveis na plataforma.<br><br>A aba, Valores foca na análise financeira dos produtos vendidos. Os campos desta aba incluem:<br><br>- ID do Anúncio (para referência cruzada com a aba de Anúncios)<br>- Preço de Venda (valor pelo qual o produto foi vendido) <br>- Custo (custo associado ao produto),<br>- Lucro (diferença entre o preço de venda e o custo)<br>- Data da Venda (quando a transação foi realizada)<br><br>Esta estrutura facilita o monitoramento do desempenho financeiro dos produtos, permitindo uma análise clara do lucro obtido com cada venda.<br><br>

- Conexão com Abas da Planilha<br>

O script estabelece conexões diretas com diferentes abas de uma planilha do Google Sheets. Essas abas são utilizadas para armazenar os dados recuperados da API.
  
![Aouth](https://github.com/user-attachments/assets/5341e035-cd2b-4517-b56b-452b9049d521)
  
- Autenticação e Gestão do Token<br>

Para garantir que todas as requisições à API do Mercado Livre sejam autenticadas, o script inclui uma função dedicada para atualizar o token de acesso. Utilizando as credenciais do cliente (ID e chave secreta), o script solicita um novo token sempre que necessário, utilizando o fluxo de autenticação OAuth 2.0.

![Aouth2](https://github.com/user-attachments/assets/07c07215-bafa-42c2-b4ae-32e30890ef38)
  
- Busca e Extração de Dados<br>

Requisição Principal: O script executa uma requisição à API do Mercado Livre com base em um termo de pesquisa definido na planilha. A resposta da API, contendo uma lista de anúncios correspondentes, é então processada para extrair dados relevantes como ID do anúncio, título, preço, e quantidade disponível.<br>

![Função Busca](https://github.com/user-attachments/assets/723458d7-caf4-4286-9a8a-8cfaa0263129)

Requisições Secundárias, para cada anúncio recuperado, são realizadas requisições adicionais para obter detalhes mais específicos, como taxas aplicáveis e opções de envio, que são igualmente armazenados na planilha.<br>

![Função Busca 2](https://github.com/user-attachments/assets/456c1c37-214a-4e0d-b3dc-45d5f14c0c02)
![função busca 3](https://github.com/user-attachments/assets/4d93d4b2-360a-4f8f-b078-d34928c658cd)

- Tratamento de Erros<br>

O script é equipado com mecanismos de tratamento de erros para lidar com possíveis falhas nas requisições à API, como respostas inválidas ou dados ausentes. Em tais casos, o script registra uma mensagem de erro na planilha ou no log, permitindo a identificação e correção de problemas sem interromper a execução geral do processo e para dados nulos.<br><br>

<h2 align="left">Benefícios da Aplicação</h2>

Eficiência: Automação completa do processo de coleta de dados, permitindo a extração de grandes volumes de informações em um tempo muito reduzido.<br><br>Precisão: Reduz a chance de erros comuns em processos manuais de coleta de dados.<br><br>Escalabilidade: Facilmente adaptável para processar um número maior de anúncios ou coletar dados adicionais conforme necessário.</p>

###

<h2 align="left">Considerações Finais e Resultados</h2>

###
<p>Registro da Requisição da API para busca de produtos, anúncios, precificação e custo. </p>

![Retorno Info](https://github.com/user-attachments/assets/4459a764-4fba-441f-b55c-745496f1112c)  

<p>Registro da Requisição da API para busca de precificação aprofundada dos produtos solicitados.</p>

![Taxas](https://github.com/user-attachments/assets/9657d218-eaaf-4a09-83fb-eb38fb6b58ed)

<p align="left">Este projeto é uma solução prática para estudantes e profissionais que desejam otimizar a coleta de dados de anúncios no Mercado Livre, integrando a API de maneira eficiente com o Google Sheets. Com uma implementação robusta e tratamento de erros, este script oferece uma maneira eficiente de gerenciar e analisar dados online.
  
Sendo possível usar em outras ferramentas e plataformas como Python, PHP, Power BI e Excel, por exemplo, este recurso torna-se extremamente versátil e aplicável em diversas áreas, facilitando a integração de dados, a automação de processos e a geração de insights para tomadas de decisão.</p>

###
