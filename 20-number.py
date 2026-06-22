from itertools import combinations


def encontrar_somas_de_tres(lista_numeros, resultado_alvo):
    # Armazena as combinações válidas encontradas
    combinacoes_validas = []

    # Gera todas as combinações únicas de 3 elementos
    for comb in combinations(lista_numeros, 3):
        if sum(comb) == resultado_alvo:
            combinacoes_validas.append(comb)

    total_encontrado = len(combinacoes_validas)

    print("\n" + "=" * 40)
    if total_encontrado == 0:
        print(
            f"Nenhuma combinação de 3 números soma o resultado {resultado_alvo}."
        )
    else:
        print(
            f"Encontrada(s) {total_encontrado} combinação(ões) para o alvo {resultado_alvo}:\n"
        )
        for comb in combinacoes_validas:
            print(f"{comb[0]} + {comb[1]} + {comb[2]} = {resultado_alvo}")
    print("=" * 40)


# --- Interação com o Usuário ---
try:
    print("Digite cerca de 20 números separados por ESPAÇO:")
    entrada = input("> ")

    # Converte a string digitada em uma lista de números inteiros
    meus_numeros = [int(x) for x in entrada.split()]

    # Alerta o usuário caso ele coloque muitos ou poucos números (apenas como aviso)
    print(f"Você inseriu {len(meus_numeros)} números.")

    alvo = int(input("Digite o número ALVO da soma: "))

    # Executa a busca
    encontrar_somas_de_tres(meus_numeros, alvo)

except ValueError:
    print(
        "\nErro: Certifique-se de digitar apenas números inteiros válidos."
    )