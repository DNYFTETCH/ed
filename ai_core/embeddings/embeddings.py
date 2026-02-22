import os, json
EMBEDDINGS_PATH = "ai_core/embeddings/local_embeddings.json"

def save_embedding(key, vector):
    data = {}
    if os.path.exists(EMBEDDINGS_PATH):
        with open(EMBEDDINGS_PATH, "r") as f:
            data = json.load(f)
    data[key] = vector
    with open(EMBEDDINGS_PATH, "w") as f:
        json.dump(data, f)

def load_embedding(key):
    if os.path.exists(EMBEDDINGS_PATH):
        with open(EMBEDDINGS_PATH, "r") as f:
            return json.load(f).get(key, None)
    return None
