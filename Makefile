VENV_NAME = .venv
PYTHON = $(VENV_NAME)/Scripts/python.exe

.PHONY: setup install-dev install-docs pre-commit test lint clean check-python

setup: check-python
	@if not exist $(VENV_NAME) ( \
		echo "Creating virtual environment..." && \
		python -m venv $(VENV_NAME) && \
		$(PYTHON) -m pip install --upgrade pip && \
		$(PYTHON) -m pip install -r requirements-dev.txt && \
		$(PYTHON) -m pip install -r requirements-docs.txt && \
		$(VENV_NAME)/Scripts/pre-commit.exe install \
	) else ( \
		echo "Virtual environment already exists. Skipping setup." \
	)

install-dev:
	$(PYTHON) -m pip install -r requirements-dev.txt

install-docs:
	$(PYTHON) -m pip install -r requirements-docs.txt

test:
	$(PYTHON) -m pytest

lint:
	$(VENV_NAME)/Scripts/pre-commit.exe run --all-files

clean:
	@if exist $(VENV_NAME) rd /s /q $(VENV_NAME)
	@if exist .git\hooks\pre-commit del .git\hooks\pre-commit
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

check-python:
	@python -c "import sys; v=sys.version_info; \
	assert v >= (3,9) and v < (3,12), \
	f'Python version must be 3.9 to 3.11. Found: {v.major}.{v.minor}.{v.micro}'"
