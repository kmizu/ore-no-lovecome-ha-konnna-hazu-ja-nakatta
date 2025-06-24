.PHONY: help install serve build clean deploy test

help:
	@echo "俺のラブコメはこんなはずじゃなかった - Build Commands"
	@echo ""
	@echo "make install    - Install dependencies"
	@echo "make serve      - Run development server"
	@echo "make build      - Build static site"
	@echo "make clean      - Clean build artifacts"
	@echo "make deploy     - Deploy to GitHub Pages (via git push)"
	@echo "make test       - Test the build"

install:
	pip install -r requirements.txt

serve:
	mkdocs serve

build:
	mkdocs build

clean:
	rm -rf site/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

deploy:
	@echo "Deployment is handled by GitHub Actions."
	@echo "Just push to the main branch:"
	@echo "  git add ."
	@echo "  git commit -m 'Your message'"
	@echo "  git push origin main"

test: clean
	mkdocs build --strict
	@echo "Build test passed!"