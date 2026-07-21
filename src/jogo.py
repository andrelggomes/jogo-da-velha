# Este módulo concentra a lógica do jogo da velha.
# Ele mantém o tabuleiro e as funções responsáveis por sua exibição.


def criar_tabuleiro():
    """
    Cria um tabuleiro vazio para o jogo da velha.

    Retorna uma matriz 3x3 preenchida com espaços vazios.
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def fazer_jogada(tabuleiro, linha, coluna, jogador):
    """
    Faz uma jogada no tabuleiro em uma posição informada.

    A função altera apenas a célula escolhida e retorna o tabuleiro atualizado.
    """
    tabuleiro[linha][coluna] = jogador
    return tabuleiro


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
