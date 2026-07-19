# Este projeto implementa um jogo da velha.
# Inicialmente queremos criar uma representação do tabuleiro.
# Explique uma possível arquitetura para este projeto.

def criar_tabuleiro():
    """
    Cria um tabuleiro vazio para o jogo da velha.

    Retorna uma matriz 3x3 preenchida com espaços vazios.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

tabuleiro = criar_tabuleiro()
print(tabuleiro)