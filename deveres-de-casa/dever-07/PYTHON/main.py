"""
DESAFIO: SISTEMA DE TRIAGEM HOSPITALAR COM MAX-HEAP
====================================================
Estrutura: Max-Heap baseado em nível de dor (1-10)
Invariante: heap[pai].dor >= heap[filho].dor
Complexidade analisada ao final.
"""

from dataclasses import dataclass, field
from typing import Optional
import random


# ─────────────────────────────────────────
#  MODELO DE DADOS
# ─────────────────────────────────────────

@dataclass
class Paciente:
    nome: str
    dor: int           # 1 (mínima) a 10 (máxima)
    id: int = field(default_factory=lambda: Paciente._next_id())
    _counter: int = 0

    @staticmethod
    def _next_id():
        Paciente._counter += 1
        return Paciente._counter

    def __str__(self):
        return f"{self.nome} (dor={self.dor}, id={self.id})"


# ─────────────────────────────────────────
#  MAX-HEAP DE TRIAGEM
# ─────────────────────────────────────────

class TriagemHeap:
    """
    Max-Heap indexado por nível de dor.
    Array interno: heap[0] sempre é o paciente mais crítico.

    Índices:
        pai(i)    = (i - 1) // 2
        esquerdo  = 2*i + 1
        direito   = 2*i + 2
    """

    def __init__(self):
        self._heap: list[Paciente] = []

    # ── utilidades internas ──────────────────

    def _pai(self, i: int) -> int:
        return (i - 1) // 2

    def _esq(self, i: int) -> int:
        return 2 * i + 1

    def _dir(self, i: int) -> int:
        return 2 * i + 2

    def _trocar(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    # ── operações principais ─────────────────

    def inserir(self, paciente: Paciente) -> None:
        """
        Insere paciente no final e sobe até restaurar invariante.

        Complexidade: O(log n)  — percorre no máximo altura da árvore.
        """
        self._heap.append(paciente)
        self._subir(len(self._heap) - 1)

    def extrair_max(self) -> Optional[Paciente]:
        """
        Remove e retorna o paciente com maior dor (raiz).
        Substitui raiz pelo último elemento e desce.

        Complexidade: O(log n)
        """
        if not self._heap:
            return None

        # troca raiz com último e remove
        self._trocar(0, len(self._heap) - 1)
        paciente = self._heap.pop()

        if self._heap:
            self._descer(0)

        return paciente

    def peek_max(self) -> Optional[Paciente]:
        """
        Retorna o paciente mais crítico SEM removê-lo.

        Complexidade: O(1)  — apenas lê heap[0].
        """
        return self._heap[0] if self._heap else None

    def change_key(self, indice: int, nova_dor: int) -> None:
        """
        Ajusta a prioridade de um paciente já na fila.
        Após mudar o valor, decide se sobe ou desce.

        Casos:
          • nova_dor > antiga → sobe  (heapify-up)
          • nova_dor < antiga → desce (heapify-down)
          • nova_dor == antiga → nada a fazer

        Complexidade: O(log n)
          - Localizar por índice: O(1) (índice dado)
          - Uma subida ou descida: O(log n)

        ⚠ Se o índice for desconhecido e precisar buscar por nome/id:
          - Busca linear: O(n)  → total O(n + log n) = O(n)
          Para evitar isso, mantemos um dicionário id→índice
          na versão estendida abaixo (TriagemIndexada).
        """
        if indice < 0 or indice >= len(self._heap):
            raise IndexError("Índice fora do heap.")

        dor_antiga = self._heap[indice].dor
        self._heap[indice].dor = nova_dor

        if nova_dor > dor_antiga:
            self._subir(indice)
        elif nova_dor < dor_antiga:
            self._descer(indice)

    # ── heapify ─────────────────────────────

    def _subir(self, i: int) -> None:
        """Sobe o elemento i enquanto for maior que o pai."""
        while i > 0:
            pai = self._pai(i)
            if self._heap[i].dor > self._heap[pai].dor:
                self._trocar(i, pai)
                i = pai
            else:
                break

    def _descer(self, i: int) -> None:
        """Desce o elemento i escolhendo o filho maior."""
        n = len(self._heap)
        while True:
            maior = i
            esq = self._esq(i)
            dir = self._dir(i)

            if esq < n and self._heap[esq].dor > self._heap[maior].dor:
                maior = esq
            if dir < n and self._heap[dir].dor > self._heap[maior].dor:
                maior = dir

            if maior != i:
                self._trocar(i, maior)
                i = maior
            else:
                break

    # ── utilitários ─────────────────────────

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def imprimir(self) -> None:
        """Exibe o heap por níveis."""
        if not self._heap:
            print("  [heap vazio]")
            return
        import math
        n = len(self._heap)
        levels = math.floor(math.log2(n)) + 1
        idx = 0
        for level in range(levels):
            count = 2 ** level
            row = []
            for _ in range(count):
                if idx >= n:
                    break
                p = self._heap[idx]
                row.append(f"{p.nome[:6]}({p.dor})")
                idx += 1
            print("  " + "  ".join(row))


# ─────────────────────────────────────────
#  VERSÃO INDEXADA (change_key O(log n))
# ─────────────────────────────────────────

class TriagemIndexada:
    """
    Estende o heap com um dicionário id→posição,
    permitindo change_key em O(log n) sem busca linear.

    Manter o índice atualizado a cada _trocar é O(1) por troca,
    então o custo total de inserir/extrair permanece O(log n).
    """

    def __init__(self):
        self._heap: list[Paciente] = []
        self._pos: dict[int, int] = {}   # id → índice no array

    def _trocar(self, i: int, j: int) -> None:
        hi, hj = self._heap[i], self._heap[j]
        self._heap[i], self._heap[j] = hj, hi
        self._pos[hi.id] = j
        self._pos[hj.id] = i

    def inserir(self, p: Paciente) -> None:
        self._pos[p.id] = len(self._heap)
        self._heap.append(p)
        self._subir(len(self._heap) - 1)

    def change_key_por_id(self, pid: int, nova_dor: int) -> None:
        """
        Change key usando id do paciente → O(log n) garantido.
        """
        if pid not in self._pos:
            raise KeyError(f"Paciente id={pid} não encontrado.")
        i = self._pos[pid]
        dor_antiga = self._heap[i].dor
        self._heap[i].dor = nova_dor
        if nova_dor > dor_antiga:
            self._subir(i)
        elif nova_dor < dor_antiga:
            self._descer(i)

    def extrair_max(self) -> Optional[Paciente]:
        if not self._heap:
            return None
        self._trocar(0, len(self._heap) - 1)
        p = self._heap.pop()
        del self._pos[p.id]
        if self._heap:
            self._descer(0)
        return p

    def _pai(self, i): return (i - 1) // 2
    def _esq(self, i): return 2 * i + 1
    def _dir(self, i): return 2 * i + 2

    def _subir(self, i):
        while i > 0:
            pai = self._pai(i)
            if self._heap[i].dor > self._heap[pai].dor:
                self._trocar(i, pai)
                i = pai
            else:
                break

    def _descer(self, i):
        n = len(self._heap)
        while True:
            maior = i
            for filho in (self._esq(i), self._dir(i)):
                if filho < n and self._heap[filho].dor > self._heap[maior].dor:
                    maior = filho
            if maior != i:
                self._trocar(i, maior)
                i = maior
            else:
                break

    def __len__(self): return len(self._heap)


# ─────────────────────────────────────────
#  DEMONSTRAÇÃO
# ─────────────────────────────────────────

def demo():
    print("=" * 55)
    print("  PRONTO-SOCORRO — SISTEMA DE TRIAGEM COM MAX-HEAP")
    print("=" * 55)

    triagem = TriagemHeap()

    # 1. Chegada de pacientes
    pacientes = [
        Paciente("Ana",     dor=3),
        Paciente("Bruno",   dor=8),
        Paciente("Carlos",  dor=5),
        Paciente("Diana",   dor=10),
        Paciente("Eduardo", dor=2),
        Paciente("Fernanda",dor=7),
        Paciente("Gabriel", dor=9),
    ]

    print("\n[1] ADMISSÃO DE PACIENTES")
    for p in pacientes:
        triagem.inserir(p)
        print(f"  + {p}")

    print(f"\n[2] ESTRUTURA DO HEAP (níveis):")
    triagem.imprimir()
    print(f"\n  Próximo a ser atendido: {triagem.peek_max()}")

    # 2. Change Key — Ana ficou pior (dor 3 → 9)
    print("\n[3] CHANGE KEY — Ana piora: dor 3 → 9")
    # localiza Ana no array (índice 0-based)
    idx_ana = next(i for i, p in enumerate(triagem._heap) if p.nome == "Ana")
    triagem.change_key(idx_ana, 9)
    print(f"  Heap após ajuste:")
    triagem.imprimir()
    print(f"  Próximo a ser atendido: {triagem.peek_max()}")

    # 3. Atendimento por ordem de gravidade
    print("\n[4] ATENDIMENTOS (ExtractMax)")
    ordem = []
    while triagem:
        p = triagem.extrair_max()
        ordem.append(p)
        print(f"  Atendendo: {p}")

    print(f"\n  Ordem de atendimento: {[p.nome for p in ordem]}")

    # 4. Análise de complexidade
    print("\n" + "=" * 55)
    print("  ANÁLISE DE COMPLEXIDADE")
    print("=" * 55)
    print("""
  Operação          | Complexidade | Justificativa
  ──────────────────┼──────────────┼───────────────────────────────
  inserir()         | O(log n)     | heapify-up: altura = log₂ n
  extrair_max()     | O(log n)     | heapify-down: altura = log₂ n
  peek_max()        | O(1)         | leitura direta de heap[0]
  change_key(idx)   | O(log n)     | 1 subida OU 1 descida
  change_key(id)    | O(log n)*    | *com dicionário id→pos
  change_key(busca) | O(n)         | busca linear sem índice

  Espaço            | O(n)         | n nós no array

  Impacto do change_key na complexidade:
  ─────────────────────────────────────
  • Com índice direto: O(log n) — ideal para triagem onde
    o sistema conhece a posição do paciente.
  • Sem índice: O(n) para buscar + O(log n) = O(n) total.
  • Solução: manter dicionário {id → posição}, atualizado
    a cada swap, sem custo adicional assintótico.
""")


if __name__ == "__main__":
    demo()