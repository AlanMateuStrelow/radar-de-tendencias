#!/usr/bin/env python3
"""Atualiza data/produtos.json com dados do Google Trends (Brasil).

Para cada produto, compara a média de interesse de busca dos últimos 7 dias
com a média dos 7 dias anteriores e classifica como subindo/estavel/caindo.

Uso:
    pip install pytrends
    python scripts/atualizar_tendencias.py
"""

import json
import sys
import time
from datetime import date
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parent.parent / "data" / "produtos.json"

# Variação (em %) acima da qual consideramos que a busca está subindo/caindo.
LIMIAR = 10.0


def classificar(variacao_pct: float) -> str:
    if variacao_pct >= LIMIAR:
        return "subindo"
    if variacao_pct <= -LIMIAR:
        return "caindo"
    return "estavel"


def buscar_variacao(pytrends, termo: str) -> float | None:
    """Retorna a variação % da última semana vs. a anterior, ou None se falhar."""
    pytrends.build_payload([termo], timeframe="today 3-m", geo="BR")
    df = pytrends.interest_over_time()
    if df.empty or termo not in df:
        return None
    serie = df[termo]
    recente = serie.tail(7).mean()
    anterior = serie.tail(14).head(7).mean()
    if anterior == 0:
        return 100.0 if recente > 0 else 0.0
    return (recente - anterior) / anterior * 100.0


def main() -> int:
    try:
        from pytrends.request import TrendReq
    except ImportError:
        print("pytrends não instalado. Rode: pip install pytrends", file=sys.stderr)
        return 1

    dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    pytrends = TrendReq(hl="pt-BR", tz=180)
    houve_atualizacao = False

    for produto in dados["produtos"]:
        termo = produto["termo_busca"]
        try:
            variacao = buscar_variacao(pytrends, termo)
        except Exception as erro:  # rede, rate limit, mudança de API…
            print(f"[aviso] falha ao consultar '{termo}': {erro}", file=sys.stderr)
            variacao = None

        if variacao is None:
            print(f"[aviso] sem dados para '{termo}', mantendo valores atuais")
        else:
            produto["variacao_busca"] = f"{variacao:+.0f}%"
            produto["status"] = classificar(variacao)
            houve_atualizacao = True
            print(f"{produto['nome']}: {produto['variacao_busca']} ({produto['status']})")

        # Pausa entre consultas para reduzir chance de bloqueio por rate limit.
        time.sleep(5)

    if not houve_atualizacao:
        print("Nenhum produto atualizado; mantendo arquivo como está.", file=sys.stderr)
        return 1

    dados["atualizado_em"] = date.today().isoformat()
    ARQUIVO.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Arquivo atualizado: {ARQUIVO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
