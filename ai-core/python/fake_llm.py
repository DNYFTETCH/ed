import random
import sys
import time

responses = [
    "Analyzing request...",
    "Processing your input...",
    "Thinking deeply...",
    "Reviewing system context...",
    "Evaluating possibilities..."
]

def generate_response(prompt):
    time.sleep(1)
    return random.choice(responses) + "\n\nYou said: " + prompt

if __name__ == "__main__":
    user_input = " ".join(sys.argv[1:])
    print(generate_response(user_input))
