import sys, os, random, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from memory.memory_store import store, recall
from ai_core.embeddings.embeddings import save_embedding, load_embedding
from ai_core.utils.cloud_fallback import cloud_llm
from tool_engine.executor import safe_execute

responses = ["Analyzing...", "Processing...", "Thinking...", "Reviewing...", "Evaluating..."]

def generate_response(prompt):
    store(prompt)
    save_embedding(prompt, [random.random() for _ in range(5)])
    history = recall()

    time.sleep(1)

    # Hybrid cloud fallback for long prompts
    if len(prompt) > 200:
        return f"[CLOUD RESPONSE]\n{cloud_llm(prompt)}"

    # Execute safe commands if prompt looks like a command
    if prompt.startswith("run:"):
        cmd = prompt[4:].strip()
        return safe_execute(cmd)

    return f"{random.choice(responses)}\nRecent context:\n{history}\nYou said: {prompt}"

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    print(generate_response(user_input))
