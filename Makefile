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

clean:
	rm -rf __pycache__ *.egg-info build dist .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

.PHONY: clean


