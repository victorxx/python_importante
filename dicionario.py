pessoas = []

while True:
    print("\nDigite seus dados")

    pessoa = {
        "Nome": input("Digite seu nome: "),
        "Idade": int(input("Digite sua idade: ")),
        "Peso": float(input("Digite seu peso: "))
    }

    pessoas.append(pessoa)

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break

print("\nLista de pessoas cadastradas:")

for x in pessoas:
    print(x["Nome"], x["Idade"], x["Peso"])
