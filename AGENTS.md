# Orientações para agentes de programação

Este repositório é uma atividade progressiva. Antes de editar, leia `README.md` e o `docs/checkpoint-XX.md` vigente; o README indica qual é.

Ao ajudar um aluno na branch `aluno`:

1. Explique o comportamento solicitado e os arquivos que pretende tocar.
2. Faça mudanças focadas no código do aluno e preserve os contratos das etapas anteriores.
3. Use testes, seed e workflow como referência; se um deles parecer incorreto, relate o caso ao aluno em vez de alterá-lo para obter verde.
4. Execute `uv run --locked python scripts/check.py` depois da mudança. Informe quais testes passaram ou falharam e por quê.
5. Resuma a solução em linguagem acessível para que o aluno consiga explicá-la e modificá-la.

É permitido implementar código quando o aluno pedir. O objetivo é ajudá-lo a entender o fluxo e verificar o comportamento, inclusive quando a IA escreveu parte da solução.
