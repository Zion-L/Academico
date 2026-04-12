import json
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent / "dados.json"
VERSAO = "0.1.0"


def carregar(caminho=ARQUIVO):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar(gastos, caminho=ARQUIVO):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(gastos, arquivo, ensure_ascii=False, indent=2)


def adicionar(gastos, descricao, valor):
    descricao = descricao.strip()
    valor = round(float(valor), 2)

    if not descricao or valor < 0:
        raise ValueError("Gasto inválido")

    gastos.append({"descricao": descricao, "valor": valor})
    return gastos


def total(gastos):
    return round(sum(gasto["valor"] for gasto in gastos), 2)


def listar(gastos):
    if not gastos:
        print("Nenhum gasto cadastrado.")
        return

    for indice, gasto in enumerate(gastos, start=1):
        print(f"{indice}. {gasto['descricao']} - R$ {gasto['valor']:.2f}")

    print(f"Total: R$ {total(gastos):.2f}")


def menu():
    gastos = carregar()

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
                adicionar(gastos, descricao, valor)
            except ValueError:
                print("Gasto inválido.")
                continue

            salvar(gastos)
            print("Gasto salvo.")
        elif opcao == "2":
            listar(gastos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
