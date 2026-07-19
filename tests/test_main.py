from src.main import criar_tabuleiro


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
