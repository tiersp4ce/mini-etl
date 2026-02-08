# Mini-ETL de Vendas Imobiliárias
 **Transformação de dados brutos de vendas em relatórios de desempenho organizados.**

O **Mini-ETL Imobiliário** é uma ferramenta desenvolvida em **Python** para automatizar o processamento de dados de vendas. O projeto simula o fluxo básico de um processo de **ETL (Extract, Transform, Load)**: extrai informações via terminal, transforma-as através de lógica de negócios (cálculo de comissões) e gera um relatório formatado de saída.

O projeto foi criado com o objetivo de consolidar conceitos fundamentais de programação antes da transição para ferramentas de análise de dados mais robustas, como a biblioteca **Pandas**.

## Funcionalidades Técnicas
O sistema realiza o processamento de dados seguindo critérios de desempenho pré-estabelecidos:

* **Extração Dinâmica:** Coleta de dados essenciais (nome do corretor, valor da venda e período) com tratamento de strings (`.upper()` e `.strip()`).
* **Lógica de Transformação (Comissões):**
    * $Vendas \ge R\$ 500.000,00$: Aplicação de **5%** de comissão.
    * $Vendas < R\$ 500.000,00$: Aplicação de **3%** de comissão.
* **Categorização de Performance:** Classificação automática do corretor baseada no valor final da comissão:
    * **Status ELITE:** Comissões superiores a **R$ 20.000,00**.
    * **Status PADRÃO:** Comissões abaixo do patamar de elite.
* **Geração de Relatório:** Saída formatada utilizando *f-strings* e alinhamento visual para facilitar a leitura dos dados.

## Tecnologias e Ferramentas
* **Linguagem:** Python 3.x
* **Conceitos Aplicados:** * Variáveis e Tipagem de Dados (`str`, `float`, `int`)
    * Estruturas Condicionais (`if/else`)
    * Formatação de Moeda e Strings
    * Interação via Terminal (CLI)

## Exemplo de Saída (Relatório)
```text
------------------------------
RELATÓRIO DE DESEMPENHO - MÊS 10
------------------------------
Corretor:      HENRIQUE HEMÃ
Venda Total:   R$ 600,000.00
Comissão:      R$ 30,000.00
Status:        ELITE
------------------------------
PARABÉNS!!!!
```

## Próximos Passos

* [ ] Implementar leitura de dados a partir de arquivos `.csv`.
* [ ] Adicionar suporte à biblioteca **Pandas** para manipulação de grandes volumes de dados.
* [ ] Exportar o relatório final para um arquivo de texto externo.

## Como executar o projeto

1. **Clone o repositório:**
```bash
git clone [https://github.com/tiersp4ce/mini-etl-imobiliario](https://github.com/tiersp4ce/mini-etl-imobiliario)

```


2. **Acesse a pasta:**
```bash
cd mini-etl-imobiliario

```


3. **Execute o script:**
```bash
python main.py

```
