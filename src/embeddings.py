from sentence_transformers import SentenceTransformer
import chromadb
from tqdm import tqdm  # show progress

model = SentenceTransformer("all-MiniLM-L6-v2")  # load once globally

def generate_embeddings(texts, batch_size=32):
    embeddings = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Generating embeddings"):
        batch = texts[i:i+batch_size]
        batch_emb = model.encode(batch, normalize_embeddings=True)
        embeddings.extend(batch_emb)
    return embeddings

def save_embeddings(texts, embeddings):
    client = chromadb.Client()
    collection = client.get_or_create_collection("tickets")

    for i, (text, emb) in enumerate(zip(texts, embeddings)):
        collection.add(
            documents=[text],
            embeddings=[emb.tolist()],
            ids=[str(i)]
        )
