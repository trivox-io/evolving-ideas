# 🧠 Trivox – Evolving Ideas Architecture

Welcome to the core structure of **Evolving Ideas**, the automation engine that turns raw thoughts into structured, evolving blueprints.

---

## 🔁 Main Flow

1. **CLI**  
   Parses commands and routes execution.  
   → [`cli.py`](https://github.com/trivox-io/evolving-ideas/blob/main/evolving_ideas/cli.py)

2. **EvolvingIdeaApp**  
   The central app interface: implements commands like `add`, `improve`, `evolve`.  
   → [`app.py`](https://github.com/trivox-io/evolving-ideas/blob/main/evolving_ideas/app.py)

3. **IdeaRepository**  
   Handles creation, reading, and listing of idea files.  
   → [`idea_repository.py`](https://github.com/trivox-io/evolving-ideas/blob/main/evolving_ideas/domain/repositories/idea_repository.py)

4. **IdeaTree**  
   Represents the idea's version tree and evolution structure.  
   → [`idea_tree.py`](https://github.com/trivox-io/evolving-ideas/blob/main/evolving_ideas/domain/services/idea_tree.py)

---

## 👋 Contributing

New here?  
Check out:

- [README](readme)
- [Good First Issues](https://github.com/trivox-io/evolving-ideas/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [CONTRIBUTING.md](https://github.com/trivox-io/evolving-ideas/blob/main/CONTRIBUTING.md)

---

## 🚀 Get Started

Try:

```bash
python manage.py add
```

Explore commands with:

```bash
python manage.py --help
```
