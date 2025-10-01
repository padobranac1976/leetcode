import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    output = scores.sort_values(by="score", ascending=False).drop(columns=["id"])
    ranks = list(output['score'].unique())
    output['rank'] = output["score"].apply(lambda x: ranks.index(x) + 1)
    return output


if __name__ == '__main__':
    ids = [1, 2, 3, 4, 5, 6]
    scores = [3.50, 3.65, 4.0, 3.85, 4.0, 3.65]
    df = pd.DataFrame({"id": ids, "score": scores})

    print(order_scores(df))