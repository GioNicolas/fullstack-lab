# Laboratório Full Stack — Trilha

Você vai construir um sistema de eventos ao longo de quatro atividades para casa. Cada atualização acrescenta material ao **mesmo projeto**. A atividade atual é [Checkpoint 01 — Cadastrar eventos pela API](docs/checkpoint-01.md).

## O que precisa instalar

- Python 3.11 ou superior
- Git
- Uma conta no GitHub

Node.js será necessário quando o frontend chegar. Você não precisa configurar banco de dados nesta primeira atividade.

## Primeiro acesso

1. Faça um **fork** do repositório oficial no GitHub. Na aba **Actions** do seu fork, habilite workflows para que os testes possam rodar no seu repositório.
2. Clone **o seu fork** e adicione o repositório oficial como `upstream`:

```bash
git clone <url-do-seu-fork>
cd fullstack-lab
git remote add upstream https://github.com/TrilhaUFPB/fullstack-lab.git
git switch -c aluno
git push -u origin aluno
```

Substitua `<url-do-seu-fork>` pelo endereço mostrado no GitHub. A `main` do seu fork acompanha o repositório oficial; todo o seu código vai para `aluno`. Se o repositório já estiver clonado, não clone novamente: entre na pasta e confira `git remote -v`.

## Preparar Python

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-test.txt
```

No Windows (PowerShell):

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-test.txt
```

Com o ambiente ativado, execute os testes:

```bash
python scripts/check.py
```

Os testes de criação começarem vermelhos é esperado. Eles descrevem o que falta implementar. Ao terminar a atividade, todos devem passar.

Para iniciar a API:

```bash
python -m uvicorn app.main:app --reload
```

Abra `http://127.0.0.1:8000/docs` para testar as rotas pelo navegador. Pare o servidor com `Ctrl+C`.

## Sua rotina em cada checkpoint

1. Leia o documento do checkpoint atual.
2. Rode `python scripts/check.py` para ver o que falta.
3. Implemente a funcionalidade e rode os testes novamente.
4. Faça commit e push na branch `aluno`:

```bash
git add app
git commit -m "Implementa cadastro de eventos"
git push origin aluno
```

5. No GitHub, abra **Actions** no seu fork e confira a execução referente ao último commit na branch `aluno`. O checkpoint está concluído quando os testes locais e essa execução estão verdes.

## Receber a atualização da semana seguinte

Conclua ou guarde suas mudanças antes de sincronizar. Depois execute:

```bash
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main
git switch aluno
git merge main
git push origin aluno
```

Se um comando parar por conflito ou porque `main` não pode avançar diretamente, **não apague commits**. Guarde a mensagem de erro e peça ajuda. O novo documento de checkpoint explicará os arquivos acrescentados naquela atualização.

## Uso de IA

Você pode pedir a uma IA para explicar o código, sugerir um plano, implementar, testar e revisar. Leia as mudanças, execute `python scripts/check.py` e certifique-se de que consegue explicar o fluxo. `AGENTS.md` e `CLAUDE.md` orientam agentes que trabalham neste repositório. Os testes, seed e workflow são parte do enunciado: se parecerem errados, mostre o caso ao professor ou monitor.

## Como pedir ajuda

Envie o número do checkpoint, o comando executado, a mensagem de erro completa, o que você esperava acontecer e a saída de `git status`. Isso permite reproduzir o problema sem adivinhar o estado do seu projeto.
