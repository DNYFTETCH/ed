import os
LLAMA_MODEL_PATH = "ai_core/models/llama_model.gguf"

def run_llama(prompt):
    if not os.path.exists(LLAMA_MODEL_PATH):
        return "[LLAMA model not found, placeholder output]\nPrompt: " + prompt
    return "[LLAMA placeholder response]\nPrompt: " + prompt
