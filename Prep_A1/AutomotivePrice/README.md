# 📊 Análise Exploratória de Preços de Veículos Usados

## 📝 Descrição
Este projeto consiste em uma análise exploratória de dados (Exploratory Data Analysis - EDA) sobre um dataset de preços de veículos usados, obtido na plataforma Kaggle. O objetivo é ler, limpar, analisar e visualizar os dados para extrair insights sobre os fatores que influenciam o preço de um carro, utilizando a linguagem Python e suas principais bibliotecas de análise de dados.

Este trabalho foi desenvolvido para a disciplina de **Tópicos Especiais em Software** como parte da avaliação A1.

## 📦 Dataset
O conjunto de dados utilizado é o **Vehicle Price Prediction**, que contém informações sobre quase um milhão de anúncios de carros usados, incluindo características como marca, modelo, ano, potência, tipo de combustível, histórico de acidentes e preço.

- **Fonte:** [Kaggle](https://www.kaggle.com/datasets/metawave/vehicle-price-prediction/data)
- **Formato:** `.csv`

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Bibliotecas Principais:**
  - `pandas` para manipulação e análise dos dados.
  - `matplotlib` e `seaborn` para a visualização dos dados.
  - `pathlib` para a manipulação de caminhos de arquivos de forma robusta.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar a análise em seu ambiente local.

### 1. Pré-requisitos
- Ter o [Python 3](https://www.python.org/downloads/) instalado.
- Ter o [Git](https://git-scm.com/downloads) instalado para clonar o repositório.

### 2. Estrutura de Pastas Essencial
Para que o script funcione corretamente, o dataset `.csv` **deve** estar na seguinte estrutura de pastas, a partir da raiz do projeto. Crie as pastas `Prep_A1` e `AutomotivePrice` se elas não existirem e coloque o arquivo `vehicle_price_prediction.csv` dentro delas.

.
├── Prep_A1/
│   └── AutomotivePrice/
│       └── vehicle_price_prediction.csv  <-- COLOQUE O ARQUIVO CSV AQUI
├── seu_script_de_analise.py
└── README.md


### 3. Configuração do Ambiente
Abra seu terminal, clone o repositório e configure o ambiente virtual.

```bash
# Clone este repositório
git clone [URL_DO_SEU_REPOSITORIO_AQUI]
cd [NOME_DA_PASTA_DO_REPOSITORIO]

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instale as bibliotecas necessárias
pip install pandas matplotlib seaborn
4. Executar o Script
Com o ambiente virtual ativado, execute o script principal (certifique-se de que ele esteja na pasta raiz do projeto):

Bash

python seu_script_de_analise.py
Após a execução, todos os 9 gráficos gerados serão salvos automaticamente na pasta Prep_A1/AutomotivePrice/.

📂 Explicação do Código-Fonte
O script é dividido em blocos lógicos que realizam a análise de forma sequencial.

Bloco 1: Configuração Inicial e Caminhos
Nesta seção, importamos as bibliotecas necessárias. O destaque é o uso da biblioteca pathlib para definir os caminhos do arquivo de dados e da pasta de destino dos gráficos. Isso garante que o script funcione independentemente do sistema operacional ou do local de onde é executado, tornando o código mais robusto e portátil.

Bloco 2: Leitura e Limpeza dos Dados
Leitura: O arquivo .csv é carregado em um DataFrame do pandas usando pd.read_csv().

Limpeza de Colunas: Os nomes das colunas são padronizados (removendo espaços e quebras de linha).

Remoção de Colunas: As colunas year, mileage_per_year, trim e brand_popularity são removidas com base.drop(). A decisão foi baseada na redundância de informações (year vs. vehicle_age) ou na baixa clareza e relevância para a análise inicial (trim, brand_popularity).

Bloco 3: Validação e Tratamento de Nulos
Diagnóstico: O código verifica a presença de valores nulos (NaN), strings vazias ('') e zeros (0) em todas as colunas. A função .isnull().sum() revelou que a coluna accident_history continha um grande volume de dados faltantes.

Tratamento: A hipótese adotada foi que um valor nulo em accident_history significa a ausência de acidentes registrados. Portanto, esses valores foram preenchidos com a string 'No Accidents' usando o método .fillna(), transformando dados ausentes em uma categoria informativa.

Bloco 4: Geração dos Gráficos de Composição (Gráficos 1-4)
Este bloco foca em entender a composição do dataset.

Gráfico 1 (Marcas): Utiliza um gráfico de barras horizontais para mostrar a contagem de todas as marcas. Esta visualização foi escolhida em vez de um gráfico de pizza por ser mais clara e legível para um grande número de categorias.

Gráficos 2, 3 e 4 (Carroceria, Transmissão, Combustível): Para estas colunas com poucas categorias, gráficos de pizza foram usados para mostrar a proporção de cada tipo em relação ao todo, com o percentual exibido em cada fatia.

Bloco 5: Geração dos Gráficos de Análise Exploratória (Gráficos 5-9)
Este bloco investiga as relações entre as variáveis, com foco no preço.

Gráfico 5 (Histograma de Preços): Com sns.histplot(), visualizamos a distribuição da variável alvo (price), identificando as faixas de valores mais comuns.

Gráfico 6 (Regressão Preço vs. Quilometragem): sns.regplot() é usado para plotar um gráfico de dispersão com uma linha de regressão, confirmando visualmente a forte correlação negativa entre as duas variáveis.

Gráfico 7 (Mapa de Calor): A correlação entre todas as variáveis numéricas é calculada com .corr() e visualizada com sns.heatmap(). As cores e os valores anotados mostram a força e a direção das relações (ex: preço e potência têm correlação positiva, enquanto preço e idade têm correlação negativa).

Gráfico 8 (Depreciação Geral): Usando sns.lineplot() sem o parâmetro hue, calculamos o preço médio por idade do veículo para todo o dataset, mostrando a curva de depreciação média do mercado.

Gráfico 9 (Depreciação por Marca): Uma análise mais aprofundada que seleciona as 4 marcas mais populares e usa o parâmetro hue do sns.lineplot() para criar uma linha de depreciação para cada uma, permitindo uma comparação direta sobre a retenção de valor entre as marcas.

📈 Resultados e Conclusões
A análise exploratória permitiu extrair conclusões importantes sobre o mercado de veículos usados representado no dataset. Foi possível confirmar que a idade e a quilometragem são fatores primários na desvalorização, e que a potência do motor influencia positivamente no preço. Além disso, a composição do dataset foi detalhada, mostrando um mercado com predominância de certas marcas (como Ford e Chevrolet), tipos de carroceria (Sedan e SUV) e combustíveis (Gasolina).

Abaixo estão dois dos principais gráficos gerados pelo script que resumem essas descobertas:

Contagem de Veículos por Marca

Curva de Depreciação por Marca (Top 4)