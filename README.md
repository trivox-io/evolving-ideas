# 🧠 Evolving Ideas CLI

Turn chaos into clarity. Evolving Ideas helps developers and creators capture, structure, and evolve their thoughts into real, buildable systems.

## 🚀 Features

- Classic brainstorming method with structured prompts
- YAML versioning for ideas
- Stores context, questions, answers, and summaries
- OpenAI integration
- CLI-first interface

## 📦 Coming Soon

- `improve`: refine and push your ideas further
- `evolve`: branch and explore new directions
- Visual idea trees, idea templates, and more

## 📂 Project Structure

```bash
evolving-ideas/
│
├── .env-example # Example .env file
├── manage.py # Dev entry point
├── requirements.txt # Dependencies
├── .store/ # Ideas and cache
│ ├── cache.yaml # Cache store
│ └── ideas/ # Idea folders
├── evolving_ideas/ # Main app
│ ├── app.py # Main entry logic
│ ├── cli.py # CLI interface
│ ├── common/ # Cache & logging
│ ├── domain/ # Models, services, repos
│ ├── infra/ # OpenAI & transport
│ ├── prompts/ # Prompt templates & builder
│ ├── interface/ # Chat logs & presenters
│ ├── sessions/ # Session state
│ └── strategies/ # Brainstorming methods
```

## 🛠 Setup

- Requires **python>=3.9<=3.11**
- OpenAI API Key in .env
- **Windows only** support for now

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
cp .env-example .env
```

## 🧪 Usage

```bash
python manage.py add
```

## 📜 License

MIT – see [LICENSE](LICENSE)

---

## 🤝 Contributing

We welcome contributions! Please read the [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md) before getting started.
