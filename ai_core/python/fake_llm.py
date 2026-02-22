import random
import sys
import time
from memory.memory_store import store, recall
from ai_core.embeddings.embeddings import save_embedding, load_embedding

responses = [
    "Analyzing request...",
    "Processing your input...",
    "Thinking deeply...",
    "Reviewing system context...",
    "Evaluating possibilities..."
]

def generate_response(prompt):
    # Save prompt to memory
    store(prompt)

    # Example embedding storage
    save_embedding(prompt, [random.random() for _ in range(5)])

    # Recall last 5 messages
    history = recall()

    time.sleep(1)
    return f"{random.choice(responses)}\n\nRecent context:\n{history}\n\nYou said: {prompt}"

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    print(generate_response(user_input))
