from src.main import criar_tabuleiro
from src.jogo import fazer_jogada


def test_criar_tabuleiro_vazio():
    # Arrange: nenhum dado extra é necessário para esta função.

    # Act: cria o tabuleiro vazio do jogo.
    tabuleiro = criar_tabuleiro()

    # Assert: o tabuleiro deve ter 3 linhas e 3 colunas, todas vazias.
    assert len(tabuleiro) == 3
    assert all(len(linha) == 3 for linha in tabuleiro)
    assert tabuleiro == [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]


def test_fazer_jogada_em_posicao_vazia():
    # Arrange: tabuleiro vazio e uma posição válida.
    tabuleiro = criar_tabuleiro()

    # Act: o jogador X faz uma jogada na linha 1, coluna 2.
    tabuleiro_atualizado = fazer_jogada(tabuleiro, 1, 2, "X")

    # Assert: somente a posição informada deve receber o símbolo do jogador.
    assert tabuleiro_atualizado[1][2] == "X"
    assert tabuleiro_atualizado[0][0] == " "
    assert tabuleiro_atualizado[0][1] == " "
    assert tabuleiro_atualizado[0][2] == " "
    assert tabuleiro_atualizado[1][0] == " "
    assert tabuleiro_atualizado[1][1] == " "
    assert tabuleiro_atualizado[2][0] == " "
    assert tabuleiro_atualizado[2][1] == " "
    assert tabuleiro_atualizado[2][2] == " "
