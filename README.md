# Naming the Pain in Machine Learning - Análises Visuais
Este repositório visa estabelecer um ambiente de desenvolvimento para visualizações gráficas das respostas apresentadas no survey disponível em https://ww2.unipark.de/uc/seml/. 

Inicialmente, as questões D1 a D15 e Q1 a Q7 serão exploradas em notebook do Jupyter. 

## Como Executar

O projeto está contido em um ambiente virtual do Python usando pipenv, então para executar basta:

- pip install --user pipenv (instalar na sua máquina)
- pipenv install (em um terminal na mesma pasta que este projeto for clonado)
- pipenv shell (inicializa o terminal com as dependências já instaladas)
- jupyter notebook (abre um servidor na pasta deste projeto com todos os arquivos criados, incluindo os jupyter notebooks)

## Novas Bibiliotecas

Para instalar ou desinstalar novas bibliotecas e dependências, é necessário instalar com o pipenv. Ou seja,

- pipenv install pandas (pode ser qualquer biblioteca presente no pip)
- pipenv uninstall pandas (pode ser qualquer biblioteca presente no pip)
