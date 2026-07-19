# Este projeto implementa um jogo da velha.
# Inicialmente queremos criar uma representação do tabuleiro.
# Explique uma possível arquitetura para este projeto.

def criar_tabuleiro():
    """
    Cria um tabuleiro vazio para o jogo da velha.

    Retorna uma matriz 3x3 preenchida com espaços vazios.
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro de forma legível no terminal.

    Mantém a estrutura interna como lista de listas, mas melhora a
    apresentação para o usuário.
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        if linha is not tabuleiro[-1]:
            print("---------")


tabuleiro = criar_tabuleiro()
mostrar_tabuleiro(tabuleiro)