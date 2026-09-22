# Pesquisa de Opinião - TudoWeb
# Atividade Agenda 08 - Desenvolvimento de Sistemas

excelente = 0
ruim = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")
for entrevistado in range(1, 51):
    print(f"\nEntrevistado {entrevistado}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print("\nAvalie nosso atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))


    if opiniao == 1:
        excelente += 1
        print("Avaliação registrada: EXCELENTE")

    elif opiniao == 2:
        print("Avaliação registrada: BOM")

    elif opiniao == 3:
        ruim += 1
        print("Avaliação registrada: RUIM")

    else:
        print("Opção inválida!")


print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")