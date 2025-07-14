import numpy as np

def score_wallets(features_df):
    # Simplistic scoring rule-based model
    scores = []

    for _, row in features_df.iterrows():
        score = 500

        # Reward high repayment ratio
        score += 200 * min(row['repayment_ratio'], 1.0)

        # Penalize high borrow-to-deposit ratio
        if row['borrow_to_deposit_ratio'] > 1:
            score -= 100 * (row['borrow_to_deposit_ratio'] - 1)

        # Penalize liquidations
        score -= 50 * row['num_liquidation']

        # Clip to [0, 1000]
        score = np.clip(score, 0, 1000)
        scores.append(score)

    features_df['credit_score'] = scores
    return features_df[['wallet', 'credit_score']]
