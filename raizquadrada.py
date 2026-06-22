import math


def verificar_raiz_quadrada(numero):
    # Números negativos não possuem raiz quadrada no conjunto dos números reais
    if numero < 0:
        return "Prompt inválido"

    # Calcula a raiz quadrada
    raiz = math.sqrt(numero)

    # Verifica se a raiz é um número inteiro exato
    if raiz.is_integer():
        return int(raiz)  # Retorna o número inteiro (ex: 3)
    else:
        return "Prompt inválido"


# --- Bloco de Input para o Usuário ---
try:
    # O input() recebe o que você digita como texto, e o float() converte para número
    entrada = float(input("Digite um número para calcular a raiz quadrada: "))

    # Chama a função e guarda o resultado
    resultado = verificar_raiz_quadrada(entrada)

    # Exibe o resultado final na tela
    print(resultado)

except ValueError:
    # Caso o usuário digite letras ou símbolos inválidos
    print("Por favor, digite apenas números válidos.")