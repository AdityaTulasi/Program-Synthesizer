init:
    pip install -r requirements.txt
	python -m spacy download en_core_web_sm	
	python -m spacy download en_core_web_lg

test:
    py.test tests

.PHONY: init test