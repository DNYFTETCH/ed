import sys, os, random, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from memory.memory_store import store, recall
from ai_core.embeddings.embeddings import save_embedding, load_embedding
from ai_core.utils.cloud_fallback import cloud_llm

responses = ["Analyzing...", "Processing...", "Thinking...", "Reviewing...", "Evaluating..."]

def generate_response(prompt):
    store(prompt)
    save_embedding(prompt, [random.random() for _ in range(5)])
    history = recall()

    time.sleep(1)

    # Hybrid cloud: fallback if prompt too long
    if len(prompt) > 200:
        cloud_response = cloud_llm(prompt)
        return f"[CLOUD RESPONSE]\n{cloud_response}"

    return f"{random.choice(responses)}\nRecent context:\n{history}\nYou said: {prompt}"

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    print(generate_response(user_input))
