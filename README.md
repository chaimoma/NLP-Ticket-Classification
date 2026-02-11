# NLP Ticket Classification

## Project Overview

This project is a **batch NLP pipeline** designed to automatically classify IT support tickets from customer emails.
Support teams often receive a high volume of emails, and manual classification is slow, inconsistent, and difficult to maintain.

The goal of this project is to **automate the categorization of tickets** so that they can be routed and prioritized efficiently.
The pipeline is intended to include:

* **Data preprocessing:** cleaning and preparing email text for NLP tasks
* **Embeddings generation:** transforming text into semantic vector representations
* **Classification model training:** training a supervised model to predict ticket types
* **Monitoring:** checking model performance and data quality over time
* **Deployment readiness:** containerizing and orchestrating the pipeline for production-like environments

This setup is aimed at demonstrating a full **MLOps approach** for a real-world IT support scenario.

---

## Get the Project

To get a copy of the project, clone the repository:

```bash
git clone https://github.com/chaimoma/NLP-Ticket-Classification.git
cd NLP-Ticket-Classification
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

After cloning, the repository will contain all the scripts, data placeholders, and configuration files needed to implement the NLP ticket classification pipeline.

---

## Intended Deliverables

The final project is expected to include:

* Preprocessing scripts for email text
* Embeddings stored in a vector database (ChromaDB)
* Trained classification model
* Reports for monitoring model performance and detecting drift (Evidently AI)
* Docker images for reproducible environments
* Kubernetes manifests for batch deployment
* Dashboards for monitoring infrastructure (Prometheus and Grafana)
* A final technical report documenting the project

---
