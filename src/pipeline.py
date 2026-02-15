from preprocessing import preprocess
from embeddings import generate_embeddings, save_embeddings
from train import train_model

def main():
    df = preprocess()

    embeddings = generate_embeddings(df["clean_text"].tolist())
    save_embeddings(df["clean_text"].tolist(), embeddings)

    preds, y_test = train_model(embeddings, df["type"])

    # print metrics
    for i, (p, y) in enumerate(zip(preds[:10], y_test[:10])):
        print(f"pred: {p}, true: {y}")

if __name__ == "__main__":
    main()
