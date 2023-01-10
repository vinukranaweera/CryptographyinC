PY = python3
VENV = venv
BIN=$(VENV)/bin

$(VENV): requirements.txt 
	$(PY) -m venv $(VENV)
	$(BIN)/pip install -r requirements.txt

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean