# Decisões de Arquitetura

## ADR-001

### Representação do Tabuleiro

Decisão

Representar o tabuleiro utilizando uma lista de listas.

Justificativa

- simples;
- didático;
- fácil de testar;
- adequado para iniciantes.

# Decisão 001 - Configuração de testes Python

## Contexto

Os testes inicialmente precisavam alterar sys.path manualmente
para localizar módulos da aplicação.

## Decisão

Adotar pyproject.toml para configurar o pytest e manter
os testes independentes da estrutura de execução.

## Consequência

Os testes ficam mais limpos e preparados para evolução futura.

## Melhoria configuração do proejeto
Criação de arquivo pyproject.toml para limpar a importação de modulos
