install:
	pip install -e .

test:
	pytest tests

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

build:
	python -m build

testpublish:
	python -m twine upload --verbose --repository testpypi dist/*

publish:
	twine upload dist/*

check_compat:
	tox

bump_version:
	@echo "Current version: $$(cat VERSION)"
	@read -r -p "Enter new version: " new_version && \
	echo $$new_version > VERSION && \
	sed -i.bak "s/^version = \".*\"/version = \"$$new_version\"/" pyproject.toml && \
	rm -f pyproject.toml.bak && \
	@git add VERSION pyproject.toml && \
	@git commit -m "Bump version to $$new_version" && \
	@git tag -a v$$new_version -m "Version $$new_version" && \
	git push origin v$$version



clean:
	rm -rf __pycache__ *.egg-info build dist .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

.PHONY: clean lint format test install build publish


