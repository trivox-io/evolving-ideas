# 🧠 Evolving Ideas CLI

<!--start-->
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

Evolving Ideas provides a streamlined setup for Windows environments using a Makefile.

- Requires **python>=3.9<=3.11**
- OpenAI API Key in .env
- **Windows only** support for now

### ✅ Automated Setup (Windows only)

If you're on Windows and have Python 3.9–3.11 installed:

```bash
make setup
```

This will:

- Check your Python version (must be between 3.9 and 3.11)
- Create a virtual environment at .venv
- Install all dev and docs dependencies
- Set up pre-commit hooks for linting and formatting

After that, activate your environment with:

```bash
.venv\Scripts\activate
```

### 🛠 Manual Setup (Linux/Mac or fallback)

If you're not on Windows or prefer manual steps:

```bash
# Create and activate the virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-docs.txt

# (Optional but recommended) Set up pre-commit
pre-commit install
```

### ✨ Pre-commit

We use pre-commit to ensure consistent formatting and linting across the codebase. Hooks include:

- ``**isort**`` (with ``black`` profile)
- **black**
- **pylint** (with several warnings disabled)
- **pytest**

To run them manually on all files:

```bash
pre-commit run --all-files
```

If you skip pre-commit installation, you'll need to run the formatters and linters manually before committing.

## 🧪 Usage

```bash
python manage.py add
```

## 📚 Documentation

<!-- Full documentation is available at:  
👉 [docs.trivox.io](https://docs.trivox.io) -->

To build the docs locally:

```bash
# Create virtualenv and install docs dependencies
python -m venv .venv
source .venv\Scripts\activate
pip install -r requirements-docs.txt

# Build docs
cd docs
make.bat html
```

Then open: ``docs/build/html/index.html`` in your browser.

## 📜 License

MIT – see [LICENSE](LICENSE)

---

## 🤝 Contributing

We welcome contributions! Please read the [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md) before getting started.
<!--end-->
