<h1 align="left">Projeto: Automação com Google Apps Script para Mercado Livre</h1>

###

<p align="left">Este projeto é um script desenvolvido em Google Apps Script para automatizar a integração entre o Google Sheets e a API do Mercado Livre, permitindo gerenciar informações de anúncios, consultar dados de produtos e taxas, e realizar atualizações de tokens de autenticação diretamente em uma planilha.</p>

###

<h2 align="left">Requisitos</h2>

###

<p align="left">Conta do Google: Acesso ao Google Sheets e Google Apps Script.<br><br>Credenciais da API do Mercado Livre:<br>> Client ID.<br>> Client Secret.<br>> Código de autorização inicial.<br><br>Configuração do Ambiente: Crie uma planilha no Google Sheets com as abas mencionadas. Insira o script no editor do Google Apps Script vinculado à planilha.</p>

![Aouth](https://github.com/user-attachments/assets/5341e035-cd2b-4517-b56b-452b9049d521)

###

<h2 align="left">Estrutura da Planilha</h2>

###

<p align="left">O script utiliza as seguintes abas:<br><br>> Token: Armazena o token de acesso e o refresh token.<br><br>> Anúncios: Exibe as informações dos produtos e suas respectivas taxas.<br><br>> Valores e Preços: Abas auxiliares (não manipuladas pelo script principal).</p>

###

<h2 align="left">Funcionalidades</h2>

###

<p align="left">Autenticação com a API do Mercado Livre: Atualiza e gerencia os tokens de acesso e atualização (OAuth).<br>
  
  ![Aouth2](https://github.com/user-attachments/assets/07c07215-bafa-42c2-b4ae-32e30890ef38)
  
  Consulta de Produtos: Busca dados de produtos no Mercado Livre com base em palavras-chave.<br>
  
  ![Função Busca](https://github.com/user-attachments/assets/723458d7-caf4-4286-9a8a-8cfaa0263129)
  
  Retorna informações como título, preço, categoria, ID, quantidade disponível, entre outros.<br>

  ![Função Busca 2](https://github.com/user-attachments/assets/456c1c37-214a-4e0d-b3dc-45d5f14c0c02)
  
  Cálculo de Taxas e Envio: Obtém informações sobre taxas de venda e opções de envio para cada produto listado.<br>

  ![função busca 3](https://github.com/user-attachments/assets/4d93d4b2-360a-4f8f-b078-d34928c658cd)
  
  Armazenamento em Planilha: Os dados são organizados automaticamente em abas específicas do Google Sheets.</p>
  
  ![Retorno Info](https://github.com/user-attachments/assets/4459a764-4fba-441f-b55c-745496f1112c)
  
  ![Taxas](https://github.com/user-attachments/assets/9657d218-eaaf-4a09-83fb-eb38fb6b58ed)

  ###

  <h2 align="left">Conclusão</h2>

  ###

  <p align="left">O objetivo deste projeto é fornecer uma solução prática e automatizada para vendedores do Mercado Livre gerenciarem suas informações de anúncios diretamente no Google Sheets, simplificando o processo de integração com a API do Mercado Livre, permitindo que os usuários:<br><br>> Atualizem tokens de autenticação de forma fácil e segura.<br><br>> Consultem e armazenem dados de produtos em tempo real.<br><br>> Analisem taxas, preços e opções de envio diretamente na planilha.<br><br>> Tomem decisões estratégicas com base em dados organizados e atualizados.<br><br>Este projeto visa aumentar a produtividade dos vendedores, reduzir erros manuais e melhorar a eficiência na gestão de produtos no Mercado Livre.</p>

  ###
