install:
	pip install -e .

test:
	pytest tests

lint:
	ruff check src/ tests/
	black --check src/ tests/

format:
	black src/ tests/

build:
	python -m build

publish:
	twine upload dist/*

