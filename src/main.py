# Este arquivo é o ponto de entrada do programa.
# Sua responsabilidade é apenas iniciar a aplicação.

try:
    # Quando o módulo é importado como parte de um pacote, usamos a importação
    # relativa para manter a organização do projeto.
    from .jogo import criar_tabuleiro, mostrar_tabuleiro
except ImportError:
    # Quando o arquivo é executado diretamente como um script, a importação
    # relativa não funciona. Neste caso, usamos a importação simples.
    from jogo import criar_tabuleiro, mostrar_tabuleiro


def main():
    """
    Inicia a execução do programa.

    Cria um tabuleiro vazio e o mostra no terminal.
    """
    tabuleiro = criar_tabuleiro()
    mostrar_tabuleiro(tabuleiro)


if __name__ == "__main__":
    main()