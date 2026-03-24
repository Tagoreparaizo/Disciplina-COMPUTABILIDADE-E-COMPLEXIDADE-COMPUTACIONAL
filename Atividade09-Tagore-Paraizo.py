alfabeto = ["1", "2", "3"]
estado_atual = "q0"
sequencia_valida = True

transicoes = {
    "q0": {"1": "q1", "2": "q2", "3": "q3"},
    "q1": {"1": "q4", "2": "q5", "3": "q6"},
    "q2": {"1": "q5", "2": "q6", "3": "q7"},
    "q3": {"1": "q6", "2": "q7", "3": "q8"},
    "q4": {"1": "q7", "2": "q8", "3": "q9"},
    "q5": {"1": "q8", "2": "q9", "3": "q0"},
    "q6": {"1": "q9", "2": "q0", "3": "q1"},
    "q7": {"1": "q0", "2": "q1", "3": "q2"},
    "q8": {"1": "q1", "2": "q2", "3": "q3"},
    "q9": {"1": "q9", "2": "q9", "3": "q0"}
}

entrada = input("Digite a sequência de símbolos (1, 2, 3): ")
for simbolo in entrada:
    print(simbolo)
    if simbolo in alfabeto:
        estado_atual = transicoes[estado_atual][simbolo]
        print(f"Símbolo: {simbolo}, Estado atual: {estado_atual}")
    else:
        print(f"A sequencia é invalida. O símbolo '{simbolo}' não pertence ao alfabeto.")
        sequencia_valida = False
        break
if sequencia_valida and estado_atual == "q9":    print("A sequência é aceita.")
else:    print("A sequência é rejeitada.")