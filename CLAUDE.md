# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão Geral do Repositório

Este é um site estático de página única para o "Radar de Tendências" — um projeto pessoal que faz curadoria e comparação de produtos em alta no Brasil com base em dados públicos do Google Trends, voltado para quem revende online.

O site inteiro é um único arquivo autocontido: `index.html`. Não há sistema de build, gerenciador de pacotes, suíte de testes, linter ou framework — não existem comandos de instalação, build ou teste. Para visualizar as alterações, abra o `index.html` diretamente no navegador (ou sirva com qualquer servidor de arquivos estáticos, ex.: `python3 -m http.server`).

## Arquitetura e Convenções

- **Site de arquivo único**: toda a marcação, os estilos e o conteúdo ficam em `index.html`. O CSS está inline em um bloco `<style>` no `<head>`; não há JavaScript. Mantenha as alterações autocontidas nesse arquivo, a menos que o projeto cresça deliberadamente para além de uma página.
- **Idioma**: todo o conteúdo voltado ao usuário é em português do Brasil (`lang="pt-BR"`). Escreva novos conteúdos em português e mantenha o tom existente (informativo, transparente, "menos achismo").
- **Estilização**: tema escuro baseado em propriedades customizadas de CSS no `:root` (`--bg`, `--card`, `--text`, `--muted`, `--accent`). Reutilize essas variáveis em qualquer estilo novo em vez de fixar cores manualmente. O layout é mobile-first e responsivo (`clamp()` para tipografia, grid com `auto-fit` na seção de passos, coluna de conteúdo com largura máxima de 720px).
- **Estrutura da página**: `header` (badge + título + apresentação) → `main` com seções `.card` ("O que é", "Como funciona" com o grid `.steps`, "Contato") → `footer` com o aviso de que o site não tem vínculo oficial com os marketplaces citados. Novas seções devem seguir o padrão `.card`.
