class MaquinaTuring:
    def __init__(self, entrada):
        self.fita = {i: char for i, char in enumerate(entrada)}
        self.cabeca = 0
        self.estado = 'q0'

        # Mapeamento (estado_atual, simbolo) -> (novo_estado, escrever, direcao)
        # 1 = Direita, -1 = Esquerda, 0 = Parado
        self.regras = {
            ('q0', 'a'): ('q1', 'X', 1),
            ('q0', 'Y'): ('q4', 'Y', 1),
            ('q0', 'B'): ('q_final', 'B', 0), 

            ('q1', 'a'): ('q1', 'a', 1),
            ('q1', 'Y'): ('q1', 'Y', 1),
            ('q1', 'b'): ('q2', 'Y', 1),

            ('q2', 'b'): ('q2', 'b', 1),
            ('q2', 'Z'): ('q2', 'Z', 1),
            ('q2', 'c'): ('q3', 'Z', -1),

            ('q3', 'Z'): ('q3', 'Z', -1),
            ('q3', 'b'): ('q3', 'b', -1),
            ('q3', 'Y'): ('q3', 'Y', -1),
            ('q3', 'a'): ('q3', 'a', -1),
            ('q3', 'X'): ('q0', 'X', 1),

            ('q4', 'Y'): ('q4', 'Y', 1),
            ('q4', 'Z'): ('q4', 'Z', 1),
            ('q4', 'B'): ('q_final', 'B', 0)
        }

    def _ler(self):
        return self.fita.get(self.cabeca, 'B')

    def _renderizar_fita(self):
        limite = max(self.fita.keys(), default=0) + 2
        return "".join([self.fita.get(i, 'B') for i in range(limite)])

    def executar(self):
        print("--- Processamento da Máquina de Turing ---")
        
        while self.estado != 'q_final':
            simbolo_atual = self._ler()
            
            print(f"[{self.estado:^4}] Head: {self.cabeca:^2} | Fita: {self._renderizar_fita()}")

            transicao = self.regras.get((self.estado, simbolo_atual))

            # Se a tupla não estiver no dicionário, a máquina crasha (rejeição)
            if not transicao:
                print(f"\n[!] Execução interrompida. Sem regra para '{simbolo_atual}' no estado '{self.estado}'.")
                return False

            prox_estado, novo_simbolo, movimento = transicao
            
            self.fita[self.cabeca] = novo_simbolo
            self.estado = prox_estado
            self.cabeca += movimento

        print("\n[+] Palavra aceita com sucesso!")
        return True


if __name__ == '__main__':
    # Modifique a string abaixo para testar outras entradas
    teste = "aabbc"
    print(f"Testando entrada: '{teste}'\n")
    
    mt = MaquinaTuring(teste)
    mt.executar()