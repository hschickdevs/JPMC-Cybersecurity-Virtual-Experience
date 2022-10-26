import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file: str):
    return pd.read_csv(file)

def exercise_1(df):
    return list(df.columns)

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return set(df['type'])

def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]

def exercise_7(df):
    return df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False)

def visual_1(df) -> None:
    def transaction_counts(df):
        return df['type'].value_counts()
    
    def transaction_counts_split_by_fraud(df):
        return exercise_6(df)['type'].value_counts()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('All Transactions by Type')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Fraudulent Transactions by Type')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Fraud Count')
    fig.suptitle('Transaction Types Visualization')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
          
    return 'Analyze transaction frequency by type, and compare the results with fraudulent transactions by type.'

def visual_2(df):
    def query(df):
        return df[df['type'] == 'CASH_OUT']
    plot = query(df).plot.scatter(x='oldbalanceOrg', y='oldbalanceDest', c='isFraud', colormap='viridis')
    plot.set_title('Balance Delta Visualization')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'The delta scatter plot for origin account balance and destination account balance for Cash Out transactions'

def exercise_custom(global_df, n: int):
    """
    Returns top fraudulent transactions by destination account.
    
    :param df: The dataframe
    :param k: The top n destination accounts to view
    """
    return global_df[global_df['isFraud'] == 1].groupby('nameDest')['nameOrig'].nunique().sort_values(ascending=False).head(n)
    
def visual_custom(custom_df):
    """
    Vizualize the top n destination accounts with the most fraudulent transactions.
    
    :param df: The dataframe in the format returned from exercise_custom()
    :param k: The top n destination accounts to view
    """
    fig, axs = plt.subplots(1, figsize=(8,6))
    custom_df.plot(ax=axs, kind='bar')
    axs.set_title(f'Top {len(custom_df)} Fraudulent Destination Accounts')
    axs.set_xlabel('Destination Account')
    axs.set_ylabel('Fraud Count')
