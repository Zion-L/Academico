import urllib.request
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

VERSAO = "0.3.0"
API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

client = MongoClient(os.environ["MONGO_URI"])
db = client["controle_gastos"]
colecao = db["gastos"]


def buscar_cotacao_dolar():
    try:
        with urllib.request.urlopen(API_URL, timeout=5) as resposta:
            dados = json.loads(resposta.read())
            return float(dados["USDBRL"]["bid"])
    except Exception:
        return None


def carregar():
    return list(colecao.find({}, {"_id": 0}))


def adicionar(descricao, valor):
    descricao = descricao.strip()
    valor = round(float(valor), 2)

    if not descricao or valor < 0:
        raise ValueError("Gasto inválido")

    colecao.insert_one({"descricao": descricao, "valor": valor})


def total(gastos):
    return round(sum(gasto["valor"] for gasto in gastos), 2)


def listar(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado.")
        return

    for indice, gasto in enumerate(gastos, start=1):
        print(f"{indice}. {gasto['descricao']} - R$ {gasto['valor']:.2f}")

    total_brl = total(gastos)
    print(f"\nTotal: R$ {total_brl:.2f}")

    cotacao = buscar_cotacao_dolar()
    if cotacao:
        print(f"Cotação do dólar: R$ {cotacao:.2f}")
        print(f"Total em USD: $ {total_brl / cotacao:.2f}")
    else:
        print("(cotação do dólar indisponível no momento)")


def menu():
    while True:
        print(f"\nControle de Gastos CLI v{VERSAO}")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            descricao = input("Descrição: ").strip()
            valor = input("Valor: ").replace(",", ".").strip()
            try:
                adicionar(descricao, valor)
                print("Gasto salvo.")
            except ValueError:
                print("Gasto inválido.")

        elif opcao == "2":
            gastos = carregar()
            listar(gastos)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()