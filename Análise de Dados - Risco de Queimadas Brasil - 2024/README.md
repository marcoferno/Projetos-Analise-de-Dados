<h1 align="left">Desmatamento nos Biomas do Brasil - 2024</h1>

###

<p align="left">Este projeto foi desenvolvido para a análise do desmatamento nos biomas brasileiros, utilizando dados de monitoramento ambiental e climático. A análise é focada em identificar padrões críticos de desmatamento e queimadas, a fim de fornecer insights que possam embasar políticas públicas e ações de preservação.</p>

###

<h2 align="left">Sobre o Projeto e Objetivos</h2>

###

<p align="left">O estudo analisa o impacto do desmatamento nos biomas brasileiros em 2024, com foco nas variáveis climáticas e ambientais que influenciam o desmatamento e o aumento do risco de incêndios. As informações incluem dados como precipitação, dias sem chuva, risco de fogo e intensidade dos focos de calor (FRP - Potência Radiativa do Fogo).<br><br>> Identificar padrões de desmatamento: Analisar fatores críticos que influenciam o desmatamento em diferentes estados e biomas.<br><br>> Fornecer insights para políticas públicas: Auxiliar na formulação de estratégias de preservação ambiental.<br><br>> Entender correlações climáticas: Investigar a relação entre variáveis como dias sem chuva, precipitação e risco de incêndio.</p>

###

<h2 align="left">Dados</h2>

###

<p align="left">Os dados utilizados foram obtidos do Portal de Dados Abertos do Governo Brasileiro, com informações do INPE (Instituto Nacional de Pesquisas Espaciais). As variáveis principais incluem:<br><br>> Média de dias sem chuva<br><br>> Média de precipitação<br><br>> Risco médio de incêndios<br><br>> FRP (Potência Radiativa do Fogo)</p>

###

<h2 align="left">Configuração do Ambiente</h2>

###

<p align="left">Para rodar o projeto, certifique-se de ter instalado as bibliotecas abaixo:<br></p>

![Bibliotecas](https://github.com/user-attachments/assets/614e25fa-368b-4961-954e-4f7a955ac956)


###

<h2 align="left">Etapas da Análise</h2>

###

<p align="left">O código realiza as seguintes etapas de análise:<br><br>1. Preenchimento de dados nulos: Valores ausentes são preenchidos com a mediana para variáveis numéricas e com a moda para variáveis categóricas.<br><br>2. Conversão de Datas: Converte a coluna Data para o formato datetime para facilitar análises temporais.<br><br>3. Análise Estatística: Gráficos de distribuição para variáveis como dias sem chuva e risco de fogo.<br><br>4. Agrupamento por estados e biomas para calcular médias de risco de incêndio e precipitação.</p>

###

<h2 align="left">Gráficos</h2>

###

<p align="left">As principais visualizações incluem:<br><br>1. Distribuição de Dias sem Chuva: Mostra a frequência de dias secos, indicando eventos de seca prolongada.<br>
  
  ![Gráficos Distribuição Média de Dias sem Chuva](https://github.com/user-attachments/assets/cf2f3972-02ad-40ca-a067-858d0b13fa95)
  
  <br>2. Distribuição do Risco de Queimadas: Apresenta a concentração de risco, destacando períodos de alto e baixo risco.<br>
  
  ![Gráficos Distribuição Média Risco de Fogo](https://github.com/user-attachments/assets/668b99aa-2eac-4020-a592-6238270140a6)
  
  <br>3. Ranking de Estados:<br><br>> Estados com maiores médias de dias sem chuva.<br>
  
  ![Top 10 Estados sem Dias de Chuva](https://github.com/user-attachments/assets/b539a406-1779-40df-8866-72a57250555a)
  
  <br>> Estados com maior risco de queimadas.<br>
  
  ![Top 10 Estados com Risco de Queimada](https://github.com/user-attachments/assets/70b3cded-942e-4374-8068-a9ba25833cc1)
  
  <br>> Estados com maior média de precipitação.<br>
  
  ![Top 10 Estados com Precipitações](https://github.com/user-attachments/assets/0b097926-6f39-432f-affa-b41a821ae2a4)
  
  <br>4. Ranking de Biomas:<br><br>> Biomas com mais dias secos e maior risco de queimadas.<br>
  
  ![Top 10 Biomas sem Dias de Chuva](https://github.com/user-attachments/assets/bd70bc01-226c-4c74-8993-9451e94d7d06)
  ![Top 10 Biomas com Risco de Queimada](https://github.com/user-attachments/assets/b2264a29-14d0-4517-bf84-6e2e9b330b4c)

  <br>> Biomas com maiores precipitações.<br>

  ![Top 10 Biomas com Precipitações](https://github.com/user-attachments/assets/84a95ee0-0f16-414e-894e-11fdbd7c452b)
  
  <br>5. Correlação entre Variáveis: Mapa de calor e gráficos de dispersão para identificar relações entre precipitação, dias sem chuva, FRP e risco de fogo.</p>

  ![Mapa de Calor Correlacionando as Variáveis](https://github.com/user-attachments/assets/9c27f49b-39f1-4475-9817-82d09c6fb2b6)
  
###

<h2 align="left">KPIs e Insights</h2>

###

<p align="left">Os indicadores revelam a correlação entre variáveis ambientais e o desmatamento:<br>
  
<br>1. Correlação entre dias sem chuva e risco de fogo: Mostra que longos períodos de seca aumentam significativamente o risco de incêndios.<br>

![Correlação entre Dias Sem Chuva e Risco de Fogo](https://github.com/user-attachments/assets/549c5e2c-cbad-4057-8815-5ac4ddfaab4a)

<br>2. Correlação entre FRP e variáveis climáticas: Indica como a intensidade dos incêndios está relacionada a fatores como o número de dias secos.<br>

![Correlação entre FRP e Dias Sem Chuva](https://github.com/user-attachments/assets/5e94d9d5-0123-49c2-a1da-6cce48a33d49)

<br>3. Correlação entre FRP e risco de fogo: Indica como a intensidade dos incêndios está relacionada a potência do sol indicando incêndios naturais nos biomas.<br>

![Correlação entre FRP e Risco de Fogo](https://github.com/user-attachments/assets/d96aa8fe-4799-4910-8d5d-687a8cffe239)

<br>4. Tendência temporal do risco de incêndio: O risco de fogo apresenta um aumento constante ao longo de 2024, alcançando valores altos e preocupantes.</p>

![Evolução do Risco de Fogo ao Longo do Tempo](https://github.com/user-attachments/assets/8872786e-b972-4570-bf76-aa2715551129)

###

<h2 align="left">Conclusão e Previsões</h2>

###

<p align="left">A análise do desmatamento e das condições ambientais nos biomas brasileiros em 2024 revela um cenário alarmante de degradação que afeta diretamente a sustentabilidade e a biodiversidade do país. O estudo constatou que biomas como o Cerrado e a Mata Atlântica estão particularmente vulneráveis ao risco de incêndios, influenciados tanto por fatores climáticos, como dias sem chuva e baixa precipitação, quanto por pressões antropogênicas, incluindo a expansão agrícola e práticas ilegais de queimadas. Ao longo do ano, observou-se um aumento expressivo no risco de fogo, que atinge valores críticos no segundo semestre, destacando um padrão sazonal de secas prolongadas que elevam a probabilidade de incêndios em grande escala.<br><br>As variáveis ambientais analisadas, como precipitação média, dias sem chuva e Potência Radiativa do Fogo (FRP), demonstraram correlações significativas entre si. A análise mostrou que períodos secos e prolongados estão diretamente associados ao aumento do risco de fogo, especialmente em biomas onde a vegetação é naturalmente inflamável. Essa condição não apenas agrava a perda de cobertura vegetal, mas também representa uma ameaça para a fauna, aumenta a erosão do solo e reduz a capacidade de regeneração natural desses ecossistemas.<br><br>Além disso, a tendência ascendente de risco de incêndios até o final de 2024 é um indicativo claro de que, se ações de preservação não forem intensificadas, o cenário pode se agravar, levando a uma perda irreparável de recursos naturais e a um aumento das emissões de carbono na atmosfera. A previsão para os meses de outubro a dezembro indica que o risco de queimadas pode permanecer acima de 90%, o que exige uma resposta urgente por parte dos órgãos responsáveis pela preservação ambiental e do governo para a implementação de políticas mais rigorosas de monitoramento, controle e prevenção de incêndios.<br><br>Esta análise oferece uma base robusta para a formulação de políticas públicas eficazes e para a mobilização de esforços em prol da proteção dos biomas brasileiros. O fortalecimento das estratégias de conservação e a conscientização sobre os impactos ambientais e climáticos do desmatamento são fundamentais para reverter o quadro atual e assegurar a resiliência dos ecossistemas brasileiros frente às mudanças climáticas. O estudo reforça a importância da ciência de dados e do monitoramento contínuo como ferramentas essenciais para identificar, prever e mitigar riscos, garantindo que as próximas gerações herdem um ambiente mais equilibrado e sustentável.<br></p>

<p align="left">Em relação as previsões podemos observar que:<br>

![Gráfico de previsão](https://github.com/user-attachments/assets/82448baf-05fc-4b99-a49c-133156fb7b1a)

Este gráfico apresenta uma previsão do risco de incêndio para o último trimestre de 2024, mostrando tanto uma série histórica quanto uma projeção para os próximos meses.<br>

<br>Análise Conclusiva para o 4º Trimestre<br>

Série Histórica: A linha azul, representando a série histórica, indica uma tendência crescente no risco de incêndio ao longo de 2024. Observa-se que o risco de incêndio começou em torno de 30% no início do ano, com picos e quedas ao longo dos meses, mas houve um aumento consistente ao longo do período analisado, atingindo aproximadamente 80% ao final do terceiro trimestre.

Projeção para o Último Trimestre: A linha vermelha, indicando a previsão, mostra uma previsão estabilizada em torno de 90% para os meses finais de 2024. Isso sugere que o risco de incêndio pode permanecer em um nível elevado até o final do ano, sem expectativa de queda.

Contexto Climático e Sazonalidade: O aumento contínuo ao longo do ano pode estar associado a condições climáticas sazonais, como períodos mais secos, que são comuns em certos meses. O fato de a previsão se manter elevada sugere uma possível persistência de condições desfavoráveis, como baixa umidade e temperaturas altas, que contribuem para o risco elevado de incêndios.

</p>

###
