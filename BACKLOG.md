# 🧠 Evolving Ideas – Backlog

*Last updated: 2025-07-24*

---

## 🌿 Core CLI Features

- [x] `add` command: structured idea capture (✅ implemented)
- [ ] `improve` command: guided refinement prompts
- [ ] `evolve` command: branch & diverge idea paths
- [ ] `show`, `list`, `show_tree`: view idea summaries, trees, and metadata
- [ ] Strategy selector (`--method` or prompt-aware auto selection)
- [ ] Interactive prompt mode for idea refinement (CLI or TUI)

---

## 🧠 AI + Model Support

- [ ] GPT model selector (`gpt-4`, `gpt-4o`, `gpt-3.5`, etc.)
- [ ] Support for non-OpenAI APIs (e.g. DeepSeek, Claude, Mistral)
- [ ] Local model support (Ollama, LM Studio, vLLM)
- [ ] Cost estimation per idea (tokens + $ breakdown)
- [ ] Smart tag suggestions using LLM
- [ ] AI co-pilot (`co_create`) that proposes backlog items & improvements
- [ ] LLM-based changelog summarizer between idea versions
- [ ] Content-aware prompt tuning per strategy

---

## 🧩 Project Generators & Templates

- [ ] `generate` command to scaffold project folder from idea
- [ ] Selectable templates: feature spec, API design, TDD, blog post, etc.
- [ ] Daily prompt or reminder: revisit or improve a past idea (`daily spark`)
- [ ] User-defined templates stored in `%APPDATA%/evolving_ideas/templates` (Win/macOS/Linux compatible)

---

## 💡 Idea Management & Versioning

- [ ] Fuzzy CLI search by keyword, tag, or author
- [ ] Merge two ideas into a composite version
- [ ] GitHub Gist export / Markdown export
- [ ] Git integration for auto-committing idea versions
- [ ] Version bumping and changelog generation based on metadata diffs
- [ ] Lock idea versions from further editing

---

## 💻 Developer Experience

- [ ] Auto-version bump and changelog on PRs to `main`
- [ ] Auto-generate markdown docs from docstrings (`mkdocs` or similar)
- [ ] Auto-run format/lint/test pipeline locally on commit
- [ ] Pre-commit hooks: `black`, `pylint`, `isort`, `pytest`
- [ ] CLI diagnostics (`evolving-ideas doctor`)
- [ ] Cross-platform config dir support (`~/.config/`, `%APPDATA%/`, etc.)
- [ ] Poetry migration + dev-friendly config in `pyproject.toml`

---

## 🌐 UI & Visualization

- [ ] CLI idea tree visualization (`ascii-tree`, `rich`)
- [ ] Web-based graph/tree viewer (D3.js, Cytoscape.js)
- [ ] Future Web UI (Tauri, Flask, or Markdown-style like Obsidian)
- [ ] Toggleable themes (light/dark, minimal/full) for Web UI
- [ ] Import/export ideas between CLI and UI

---

## 🛠 DevOps & Automation

- [x] CI/CD split: feature, develop, main, release pipelines
- [x] Slack + Discord notifications across workflows
- [ ] Semantic version + changelog enforcement in CI
- [ ] Auto-lint, format, test in GitHub Actions
- [ ] Build GitHub release assets for packaged CLI (zip/tarball)
- [ ] Optional telemetry for usage patterns (opt-in)

---

## 📢 Community & Collaboration

- [ ] `contribute` CLI command that shows active issues, invites contributions
- [ ] GitHub Discussions webhook (for open roadmap)
- [ ] Export idea summaries to team Slack/Discord via webhook
- [ ] Team mode (multi-user workspace support)
- [ ] Access control for collaborative edits (via config or UI layer)
- [ ] Plugin system for external contributors (strategies, renderers, etc.)

---

## 📦 Packaging & Distribution

- [ ] Publish CLI to PyPI (`pip install evolving-ideas`)
- [ ] Build standalone binary with `pyinstaller` or `shiv`
- [ ] Docker container for headless automation
- [ ] Portable mode with self-contained `.evolving_ideas` folder
