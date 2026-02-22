memory_log = []

def store(msg):
    memory_log.append(msg)

def recall():
    return "\n".join(memory_log[-10:])  # last 10 messages
