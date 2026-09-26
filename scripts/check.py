"""Executa a verificação acumulada do projeto com um único comando."""

import shutil
import subprocess
import sys
from pathlib import Path


root = Path(__file__).resolve().parents[1]
if subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=root).returncode:
    raise SystemExit(1)

frontend = root / "frontend"
if frontend.exists():
    npm = shutil.which("npm")
    if npm is None:
        raise SystemExit("npm não encontrado. Instale Node.js e execute npm ci em frontend/.")
    raise SystemExit(subprocess.run([npm, "test", "--", "--run"], cwd=frontend).returncode)
