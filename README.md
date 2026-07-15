# Financial Decision Simulator & Consequence Engine

A local Streamlit financial-literacy app for a CBSE Class 12 competition. It compares cash, EMI, wait-and-save, and lower-cost purchase options using visible formulas and stated assumptions. It does not offer financial advice or declare a universal best option.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the local address shown by Streamlit. Click **Load official demo** to use the fictional laptop example (Rs. 50,000 income, Rs. 1,50,000 savings, Rs. 60,000 laptop).

## Test

```bash
pytest -q
```

## What is included

- Nine main modules, four purchase scenarios, comparison, what-if analysis, stress testing, visual analytics, learning content, methodology and privacy/disclaimer screens.
- Formula engine for surplus/deficit, emergency coverage, simple and compound interest, EMI, repayment, interest, goal delay, and conditional opportunity-cost future value.
- Session-only data, CSV export, validation, demo data, and 35 documented test cases in `documentation/test_cases.csv`.

## Important limits

All results are simulations based on entered values and assumptions. Never enter banking credentials or personal identifiers. Future projections are not guarantees.
