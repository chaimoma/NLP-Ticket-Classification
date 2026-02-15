````
# NLP Ticket Classification Pipeline

This project is a batch NLP pipeline to classify IT support tickets automatically.  
It preprocesses ticket text, generates embeddings, trains a classifier, and outputs predictions.  
The pipeline is Dockerized for reproducibility.

---

## Requirements

- Python 3.10+
- pip packages (see `requirements.txt`):
  - pandas
  - scikit-learn
  - sentence-transformers
  - chromadb

---

## Setup

1. Create and activate virtual environment:

```bash
python -m venv tickvenv
source tickvenv/bin/activate   # Linux/Mac
tickvenv\Scripts\activate      # Windows
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Locally

```bash
python src/pipeline.py
```

* Preprocesses data (`subject + body` → clean text)
* Generates embeddings with `all-MiniLM-L6-v2`
* Trains a classifier and prints evaluation metrics
* Prints sample predictions

---

## Run with Docker

1. Build Docker image:

```bash
docker build -t nlp-pipeline .
```

2. Run container:

```bash
docker run --rm nlp-pipeline
```

* Pipeline executes inside the container exactly as local run

---

## Output

* Evaluation metrics (precision, recall, f1-score) printed to console
* Top predictions printed to console

```
```
