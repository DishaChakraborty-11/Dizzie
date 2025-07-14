import pandas as pd

def engineer_features(df):
    grouped = df.groupby('wallet')
    features = []

    for wallet, group in grouped:
        f = {
            'wallet': wallet,
            'num_transactions': len(group),
            'num_deposit': (group['action'] == 'deposit').sum(),
            'num_borrow': (group['action'] == 'borrow').sum(),
            'num_repay': (group['action'] == 'repay').sum(),
            'num_liquidation': (group['action'] == 'liquidationcall').sum(),
            'total_deposit_amount': group.loc[group['action'] == 'deposit', 'amount'].sum(),
            'total_borrow_amount': group.loc[group['action'] == 'borrow', 'amount'].sum(),
            'total_repay_amount': group.loc[group['action'] == 'repay', 'amount'].sum(),
        }

        f['repayment_ratio'] = (
            f['total_repay_amount'] / f['total_borrow_amount']
            if f['total_borrow_amount'] > 0 else 0
        )

        f['borrow_to_deposit_ratio'] = (
            f['total_borrow_amount'] / f['total_deposit_amount']
            if f['total_deposit_amount'] > 0 else 0
        )

        features.append(f)

    return pd.DataFrame(features)
