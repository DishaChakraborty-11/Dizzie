import argparse
from preprocess import load_json, basic_clean
from feature_engineering import engineer_features
from model import score_wallets

def main(input_path, output_path):
    print("Loading data...")
    df = load_json(input_path)
    df = basic_clean(df)

    print("Engineering features...")
    features_df = engineer_features(df)

    print("Scoring wallets...")
    scored_df = score_wallets(features_df)

    print(f"Saving to {output_path}...")
    scored_df.to_csv(output_path, index=False)
    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to user-transactions.json')
    parser.add_argument('--output', required=True, help='Path to output CSV')
    args = parser.parse_args()

    main(args.input, args.output)
