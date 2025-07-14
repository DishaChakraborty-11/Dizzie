# Aave V2 Wallet Credit Scoring

This project predicts credit scores (0–1000) for wallets interacting with Aave V2 based on transaction history.

## How to Run

1. Install dependencies:

pip install -r requirements.txt

markdown
Copy
Edit

2. Place your `user-transactions.json` in the `data/` folder.

3. Run scoring:

python src/score_wallets.py --input data/user-transactions.json --output scores.csv

markdown
Copy
Edit

## Files

- **src/preprocess.py**: Loads and cleans raw JSON.
- **src/feature_engineering.py**: Aggregates wallet-level features.
- **src/model.py**: Defines scoring model.
- **src/score_wallets.py**: One-step script to run everything.

## Analysis

See `analysis.md` for results and interpretation.
