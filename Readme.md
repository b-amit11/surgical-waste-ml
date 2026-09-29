# Surgical Waste Reduction with Machine Learning

A machine-learning prototype for estimating surgical-supply demand and surfacing recommendations intended to reduce avoidable operating-room waste.

## Components

- Data-preparation utilities and configurable training workflow.
- Model-training and recommendation modules.
- Streamlit interface for interactive exploration.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run apps/streamlit_app.py
```

## Responsible use

This is a decision-support prototype. It should be validated with local clinical, inventory, and safety stakeholders before any operational use.
