class Aluno:
    """docstring for Aluno."""
    def __init__(self, nome: str, registro: int):
        self.nome: str = nome
        self.registro: int = registro
        self.historico: list[int] = []

    def getTotal(self) -> int:
        total_carga = 0
        for carga in self.historico:
            total_carga += carga
        return total_carga
