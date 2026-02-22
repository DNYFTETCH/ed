memory_log = []

def store(message):
    memory_log.append(message)

def recall():
    # Return last 5 messages
    return "\n".join(memory_log[-5:])
