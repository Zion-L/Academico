## Aplicação publicada

https://zion-l.github.io/Academico/

# Controle de Gastos CLI

Versão atual: **0.2.0**

## 1. Problema escolhido

Muitas pessoas perdem o controle de pequenos gastos do dia a dia e só percebem o total no fim do mês. Isso atrapalha o planejamento financeiro e dificulta decisões simples, como cortar despesas desnecessárias.

## 2. Relevância do problema

Controle financeiro pessoal é uma necessidade comum e real. Mesmo uma solução pequena já ajuda o usuário a registrar gastos, visualizar valores e acompanhar o total acumulado.

## 3. Objetivo da solução

Criar uma aplicação simples em Python com interface CLI para cadastrar gastos, listar registros e mostrar o total salvo em arquivo local.

## 4. Funcionalidades

- adicionar gasto
- listar gastos cadastrados
- mostrar total acumulado
- salvar dados em arquivo JSON

## 5. Tecnologias utilizadas

- Python 3
- biblioteca padrão: `json` e `pathlib`
- testes automatizados com `unittest`
- lint com `ruff`
- integração contínua com GitHub Actions

## 6. Estrutura do projeto

```text
controle_gastos_cli/
|-- .github/
|   |-- workflows/
|       |-- ci.yml
|-- tests/
|   |-- test_app.py
|-- dados.json
|-- main.py
|-- README.md
|-- requirements.txt
```

## 7. Como instalar

```bash
pip install -r requirements.txt
```

## 8. Como executar

```bash
python main.py
```

## 9. Como usar

1. escolha a opção de adicionar gasto
2. informe descrição e valor
3. use a opção de listar para ver os registros e o total
4. os dados ficam salvos em `dados.json`

## 10. Testes automatizados

```bash
python -m unittest discover -s tests
```

## 11. Linting / análise estática

```bash
ruff check .
```

## 12. Dependências declaradas

O projeto usa apenas uma dependência externa para análise estática:

- `ruff==0.11.5`

Na execução principal da aplicação, a lógica usa apenas biblioteca padrão do Python.
