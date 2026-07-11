.PHONY: all risk gap dashboard test lint clean

all: risk gap

risk:
	python scripts/generate_risk_register.py

gap:
	python scripts/generate_gap_analysis.py

generate-all:
	python scripts/generate_all.py

dashboard:
	streamlit run dashboard/app.py

test:
	python -m pytest tests/ -q

lint:
	ruff check .

clean:
	rm -rf outputs/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
