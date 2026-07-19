from src.main import criar_tabuleiro, mostrar_tabuleiro


def test_mostrar_tabuleiro_formato_legivel(capsys):
    tabuleiro = criar_tabuleiro()

    mostrar_tabuleiro(tabuleiro)

    output = capsys.readouterr().out
    assert "   |   |   " in output
    assert "---+---+---" in output
