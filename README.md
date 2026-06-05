# Mini Projeto - Módulo 1: Processamento de Dados da Olist

Este repositório contém o desenvolvimento do primeiro mini projeto do módulo de processamento de dados. O objetivo principal é aplicar técnicas de programação e manipulação de dados para limpar e estruturar uma base de dados real de e-commerce.

---

## Descrição do Projeto

A **Olist** é a maior loja de departamentos dentro dos marketplaces brasileiros, conectando pequenos negócios de todo o país a canais de venda unificados. Por lidar com volumes massivos de transações diárias, os dados brutos gerados contêm inconsistências, valores ausentes, duplicatas e formatos desalinhados (como datas salvas como texto).

O **objetivo deste script** é realizar o processo de ETL (*Extract, Transform, Load*), focando especialmente na etapa de **Transformação (Limpeza e Padronização)**. O código filtra anomalias, trata dados nulos e consolida as informações das tabelas da Olist para que estejam prontas, consistentes e confiáveis para análises preditivas ou relatórios de inteligência de negócios.

---

## Guia de Execução
Siga os passos abaixo para instalar as dependências e executar o script principal.

**Requisitos**
- Python 3.8 ou superior
- Espaço em disco suficiente para processar os arquivos CSV

1. Criar e ativar um ambiente virtual (recomendado)

Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows (cmd):
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependências

Se existir `requirements.txt` no repositório, rode:
```bash
pip install -r requirements.txt
```

Se não houver `requirements.txt`, instale as bibliotecas mínimas usadas pelo projeto:
```bash
pip install pandas numpy
```

3. Executar o script principal via linha de comando

Com o ambiente virtual ativado, execute:
```bash
python main.py
```

O script irá ler os arquivos CSV presentes no repositório e gerar/atualizar os arquivos validados, por exemplo `orders_validated.csv` e `products_validated.csv`.


---

## Reflexão Teórica sobre Machine Learning:

A máxima "lixo entra, lixo sai" (garbage in, garbage out) resume a importância vital da limpeza de dados no ciclo de vida da Inteligência Artificial. Quando aplicamos uma lógica de programação rigorosa para tratar valores nulos, remover duplicatas e filtrar outliers (anomalias) que não representam o comportamento real do negócio, estamos impedindo que o modelo decore ruídos. Se um algoritmo de Machine Learning for treinado com dados poluídos, ele sofrerá de Overfitting (superajuste), memorizando as imperfeições da base de treino e falhando miseravelmente ao tentar prever cenários com dados novos do mundo real.

Além disso, a padronização correta ajuda a mitigar o viés (bias) nos modelos futuros. No contexto da Olist, se o script de limpeza não tratar de forma justa a desproporção de dados faltantes de determinadas regiões ou categorias de produtos, a IA resultante poderá aprender um comportamento preconceituoso ou distorcido, priorizando ou penalizando certos perfis de vendedores de forma errônea. Portanto, uma lógica de tratamento de dados bem estruturada garante a integridade estatística da base, permitindo que os modelos de IA generalizem o aprendizado de forma justa, ética e precisa.