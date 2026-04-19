class AutomatoPilha:
    def __init__(self):
        self.pilha = ['Z']
        self.estado = 'q0'

    def processar(self, cadeia: str) -> bool:
        print(f"Iniciando processamento da cadeia: '{cadeia}'\n")
        print(f"{'Estado':<8} | {'Fita Restante':<15} | {'Pilha'}")
        print("-" * 45)
        
        self._exibir_status(cadeia)

        for i, simbolo in enumerate(cadeia):
            fita_restante = cadeia[i+1:]
            topo = self.pilha[-1]

            if simbolo == '(':
                self.pilha.append('X')
            elif simbolo == ')':
                if topo == 'X':
                    self.pilha.pop()
                else:
                    print(f"\n[ERRO] Rejeitado: Encontrou ')' mas o topo da pilha é '{topo}'.")
                    return False
            else:
                print(f"\n[ERRO] Símbolo inválido '{simbolo}'.")
                return False
            self._exibir_status(fita_restante)

        if self.pilha[-1] == 'Z' and len(self.pilha) == 1:
            self.estado = 'qf'
            print("\n[SUCESSO] Cadeia Aceita! (Pilha apenas com Z e estado qf alcançado)\n")
            return True
        else:
            print("\n[ERRO] Rejeitado: Fita terminou, mas sobraram elementos na pilha.\n")
            return False

    def _exibir_status(self, fita: str):
        pilha_str = "".join(self.pilha)
        fita_exibicao = fita if fita else "ε (vazia)"
        print(f"{self.estado:<8} | {fita_exibicao:<15} | {pilha_str}")


if __name__ == "__main__":
    automato1 = AutomatoPilha()
    print("TESTE 1: (()())")
    automato1.processar("(()())")
    
    print("TESTE 2: (()))")
    automato1.processar("(()))")