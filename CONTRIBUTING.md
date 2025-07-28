# Contributing to Evolving Ideas CLI

<!--start-->
First off, thanks for taking the time to contribute! ❤️

Whether it's a bug report, feature suggestion, or a pull request — you're helping make this project better.

## 🛠 Setup

```bash
git clone https://github.com/trivox-io/evolving-ideas.git
cd evolving-ideas
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## 📦 Environment

- Python >=3.9<=3.11
- OpenAI API Key in .env
- Run with: python manage.py add

## ✅ How to Contribute

### 🐞 Report Bugs

Use GitHub Issues with:

- Steps to reproduce
- Expected behavior
- Environment info (OS, Python version)

### 💡 Suggest Features

Open a discussion or issue and explain:

- What problem you're solving
- Why it's useful
- Example use case or workflow

### 🧪 Submit a Pull Request

- Fork the repo
- Create your branch: git checkout -b my-feature
- Commit changes: git commit -am 'Add cool feature'
- Push to your fork: git push origin my-feature
- Open a pull request on GitHub

### 🧼 Style & Linting

For now, we use ``pylint`` to ensure code quality. Please run it before submitting:

```bash
pylint evolving_ideas
```

>🛠 Note: In the future, we plan to adopt ``black``, ``isort``, and a full formatting + linting pipeline using ``poetry``. Stay tuned!

## 🧪 Tests

Test suite coming soon — but if you want to get ahead of it, feel free to contribute tests using ``pytest``.

```bash
pip install pytest
pytest
```

>🛠 We'll integrate ``pytest`` officially once the test structure is ready. If you're adding tests, please follow the pattern: tests/test_<your_module>.py.

### Testing with Example Data

To run the CLI using test data instead of your own ideas, you can override the default storage path by creating a config file.

#### 1. Create a YAML config file

Create a file at:

```bash
.storage/config.yml
```

With the following content:

```yaml
storage_path: tests/example_data/ideas
```

This setting will override the default storage path (``.storage/ideas``) and load the example ideas provided for testing.

#### 2. How settings are loaded

The app loads settings in the following order of priority:

``.storage/config.yml`` (YAML config – highest priority)

``.env`` file (for things like OpenAI API keys)

Hardcoded defaults (fallbacks in case the above don’t exist)

#### 3. Accessing settings in code

If you need to check or use any setting in the codebase, use the settings singleton:

```python
from evolving_ideas.settings import settings

# Get the storage path

path = settings.get("storage_path")

# Get the OpenAI model name

model = settings.get("openai.model")
```

This setup ensures contributors can easily point the CLI to test data while developing features like list, show, or show_tree.

Thanks again! You're awesome 🙌
<!--end-->
