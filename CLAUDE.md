# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static, single-page landing site for "Radar de Tendências" — a personal project that curates and compares trending products in Brazil based on public Google Trends data, aimed at online resellers.

The entire site is one self-contained file: `index.html`. There is no build system, package manager, test suite, linter, or framework — no commands to install, build, or test. To preview changes, open `index.html` directly in a browser (or serve it with any static file server, e.g. `python3 -m http.server`).

## Architecture and Conventions

- **Single-file site**: all markup, styles, and content live in `index.html`. CSS is inline in a `<style>` block in `<head>`; there is no JavaScript. Keep changes self-contained in this file unless the project deliberately grows beyond one page.
- **Language**: all user-facing content is Brazilian Portuguese (`lang="pt-BR"`). Write new content in Portuguese and keep the existing tone (informative, transparent, "menos achismo").
- **Styling**: a dark theme driven by CSS custom properties on `:root` (`--bg`, `--card`, `--text`, `--muted`, `--accent`). Reuse these variables for any new styling rather than hard-coding colors. Layout is mobile-first and responsive (`clamp()` for type, `auto-fit` grid for the steps section, max-width 720px content column).
- **Page structure**: `header` (badge + title + pitch) → `main` with `.card` sections ("O que é", "Como funciona" with a `.steps` grid, "Contato") → `footer` with a disclaimer that the site has no official ties to the marketplaces mentioned. New sections should follow the `.card` pattern.
