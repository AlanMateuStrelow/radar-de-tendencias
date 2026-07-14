# Radar de Tendências

Curadoria de produtos em alta de busca no Brasil, baseada em dados públicos do
Google Trends, para quem revende online e quer decidir com mais dado e menos
achismo.

## Estrutura

| Arquivo | O que é |
| --- | --- |
| `index.html` | Página inicial (apresentação do projeto) |
| `produtos.html` | Página "Produtos em alta agora", que lê `data/produtos.json` |
| `data/produtos.json` | Lista de produtos monitorados, com status e variação de busca |
| `scripts/atualizar_tendencias.py` | Script que consulta o Google Trends e atualiza o JSON |
| `.github/workflows/atualizar-tendencias.yml` | Automação diária que roda o script e faz commit |

## Como funciona

1. **Monitoramento** — o script consulta o interesse de busca de cada
   `termo_busca` no Google Trends (Brasil, últimos 3 meses).
2. **Sinalização** — compara a média dos últimos 7 dias com a dos 7 dias
   anteriores e classifica cada produto como `subindo`, `estavel` ou `caindo`
   (limiar de ±10%).
3. **Publicação** — a página `produtos.html` exibe os cards a partir do JSON.

## Rodando localmente

```bash
pip install pytrends
python scripts/atualizar_tendencias.py   # atualiza data/produtos.json
python -m http.server 8000               # abre o site em http://localhost:8000
```

## Adicionando um produto

Basta acrescentar um objeto em `data/produtos.json` com os campos `nome`,
`termo_busca`, `categoria`, `status`, `variacao_busca`, `faixa_preco` e
`observacao`. A automação diária atualiza `status` e `variacao_busca`
sozinha a partir do `termo_busca`.

---

Conteúdo informativo, sem vínculo oficial com marketplaces citados.
