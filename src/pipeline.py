from preprocessing import preprocess
from embeddings import generate_embeddings, save_embeddings
from train import train_model
from evidently_report import generate_report
import pandas as pd

def main():

    df = preprocess()

    embeddings = generate_embeddings(df["clean_text"].tolist())

    save_embeddings(df["clean_text"].tolist(), embeddings)

    preds, y_test = train_model(embeddings, df["type"])

    # simple drift simulation
    ref = pd.DataFrame({"target": y_test})
    cur = pd.DataFrame({"target": preds})

    generate_report(ref, cur)


if __name__ == "__main__":
    main()
