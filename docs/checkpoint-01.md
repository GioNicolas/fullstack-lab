# Checkpoint 01 — Cadastrar eventos pela API

## O problema

A organização já consegue listar eventos e consultar um evento pelo ID. Ela precisa cadastrar novos eventos pela API. Seu trabalho é completar `POST /events` em `app/main.py`.

## Antes de começar

1. Siga o setup e rode `python scripts/check.py` conforme o `README.md`.
2. Execute a API e visite `/docs` no navegador para explorar as rotas.
3. Leia `EventInput`, `create_app` e os testes em `tests/test_events.py`.

É esperado que os testes de criação falhem antes da sua implementação. A listagem e a busca por ID já devem funcionar.

## Comportamento esperado

Envie um `POST /events` com este JSON:

```json
{"title":"Semana de Tecnologia","date":"2026-10-10","capacity":2}
```

A API deve responder **201** com os mesmos dados e um `id` positivo. Em seguida, `GET /events` e `GET /events/{id}` devem encontrar o evento. Criações diferentes recebem IDs diferentes.

Rejeite com **422** título vazio, data inválida e capacidade menor ou igual a zero. Uma requisição rejeitada não pode acrescentar evento à listagem.

## Onde trabalhar

- **Leia:** `README.md`, `app/main.py`, `tests/test_events.py`.
- **Altere:** `app/main.py`, nas partes de entrada e criação de evento.
- **Preserve:** testes, `scripts/check.py`, `.github/workflows/check.yml` e arquivos de orientação.

## Caminho sugerido

1. Faça um evento válido ser criado e encontrado na listagem.
2. Garanta IDs diferentes.
3. Trate as entradas inválidas e confirme que não houve escrita.
4. Rode `python scripts/check.py` e faça push para `aluno`.
5. Confira a execução verde na aba **Actions** do seu fork.

## Dicas graduais

<details><summary>1. Onde os dados ficam agora?</summary>

O dicionário `events` dentro de `create_app` guarda os eventos desta instância da API.

</details>

<details><summary>2. O que valida o JSON?</summary>

O FastAPI cria um `EventInput` antes de chamar a rota. Tipos de dados já são verificados; regras como título não vazio e capacidade positiva ainda precisam ser expressas.

</details>

<details><summary>3. Como identificar o novo evento?</summary>

O ID deve ser positivo e diferente dos IDs já usados nessa instância. Observe o dicionário existente antes de escolher um valor.

</details>

## Conclusão

O checkpoint está concluído quando `python scripts/check.py` passa localmente e a execução do Actions para o mesmo commit está verde. Para conferir seu entendimento, identifique onde a validação acontece e o que ocorreria com os dados após reiniciar a aplicação.
