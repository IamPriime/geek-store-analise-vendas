# Geek Store | Análise de vendas

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IamPriime/geek-store-analise-vendas/blob/main/geek_store.ipynb)

Análise de receita, lucro e categorias de uma loja geek com Python e pandas.

Projeto de estudo de **Gabriel / [IamPriime](https://github.com/IamPriime)**, desenvolvido a partir de um notebook do Google Colab e organizado para portfólio. O foco é mostrar a lógica implementada e permitir que outra pessoa execute o projeto.

## O que o projeto faz

- Calcula receita por produto.
- Calcula lucro unitário e lucro total.
- Filtra produtos de hardware e periféricos.
- Exporta a seleção de produtos para CSV.

## Tecnologias e conceitos

Python 3.10+ · pandas · IPython · leitura e exportação de CSV · DataFrames.

## Como executar

```bash
git clone https://github.com/IamPriime/geek-store-analise-vendas.git
cd geek-store-analise-vendas
python -m venv .venv
```

Ative o ambiente: no Windows PowerShell, `.venv\Scripts\Activate.ps1`; no macOS/Linux, `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python geek_store.py
```

No Colab, use o botão no início deste README. Crie a pasta `data` no painel de arquivos e envie o CSV incluído neste repositório; abrir o notebook pelo GitHub não transfere o CSV automaticamente. O Colab já inclui pandas e IPython.

## Exemplo e interpretação

Receita = quantidade × preço de venda. Lucro unitário = preço − custo. Lucro total = lucro unitário × quantidade. O filtro de categoria usa os rótulos `Hardware`, `Periferico` e `Periférico`. A tabela de avaliações exibe as notas; não faz ranking automático.

Com o CSV fictício, a receita total é R$ 5.500 e o lucro total é R$ 1.900. A seleção exportada contém dois produtos.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `geek_store.ipynb` | Notebook para Colab/Jupyter, sem saídas antigas |
| `geek_store.py` | Versão executável localmente |
| `requirements.txt` | Dependências de execução |
| `data/` | CSV fictício e documentação de uso |

## Origem e melhorias

Origem no Colab: `geek_store.ipynb`. O arquivo no Drive foi preservado. Corrigida a exportação: agora grava o DataFrame filtrado, em vez de toda a base. As saídas de execução e os metadados pessoais do notebook foram removidos da versão publicada.

## Limitações

Os CSVs originais não foram localizados no Drive. A base incluída é fictícia, pequena e serve somente para demonstração. O código pressupõe o esquema documentado em `data/`; não implementa uma camada completa de validação de arquivos.

## Próximos passos

- Validar colunas, tipos e valores antes de processar.
- Adicionar gráficos e ampliar a análise com uma base real cuja publicação seja permitida.

## Autoria e uso

Organização de estudos de [IamPriime](https://github.com/IamPriime). Nenhuma licença de software foi escolhida para este repositório.
