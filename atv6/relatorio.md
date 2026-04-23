# Relatório de Testes - atv6

## Resultados dos testes

- Execução: `pytest -q`
- Resultado: `24 passed`
- Tempo de execução: 0.66s

## Cobertura de código

O relatório de cobertura gerado em `htmlcov/index.html` mostra:

- Total de linhas: 159
- Linhas não cobertas: 3
- Cobertura geral: 98%
- `src/calculadora.py`: 43 linhas de código, 3 linhas não cobertas
- `src/repositorio.py`: 11 linhas de código, 0 linhas não cobertas

Os testes em `atv6/tests` exibem cobertura completa de 100% em todos os arquivos de teste e garantem que os caminhos principais da lógica da calculadora e do repositório foram exercitados.

## Observações sobre os testes realizados

A suíte de testes abrange:

- `tests/test_unidade.py`: validações de operações matemáticas, tratamento de erros, limites e mensagens de exceção.
- `tests/test_doubles.py`: uso de doubles para isolar dependências de `HistoricoRepositorio`.
- `tests/test_integracao.py`: integração entre `Calculadora` e `HistoricoRepositorio`, incluindo histórico de operações e contagem de registros.

## Reflexão: diferença prática entre stub e mock

Na prática, o `stub` é usado quando precisamos fornecer uma dependência com comportamento pré-definido, mas não queremos depender da implementação real. Em `TestComStub`, o `stub_repo` é um objeto que retorna um valor fixo em `total()` para permitir que o teste foque apenas na lógica da calculadora sem precisar de um repositório funcional.

O `mock`, por outro lado, é usado para verificar interações entre objetos. Em `TestComMock`, o `mock_repo` não apenas substitui a dependência, mas também permite verificar se `salvar()` foi chamado, quantas vezes foi chamado e com quais argumentos. Isso é útil para testar efeitos colaterais e contratos de colaboração.

Resumo prático:

- Stub: foca em fornecer um comportamento determinístico para a dependência.
- Mock: foca em verificar que o código sob teste interage corretamente com a dependência.

No contexto deste projeto, o uso de `stub` ajudou a testar a lógica de cálculo isoladamente, enquanto o uso de `mock` garantiu que a gravação do histórico só ocorresse quando esperada e que não ocorresse em caso de erro.
