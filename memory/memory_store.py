memory_log = []

def store(message):
    memory_log.append(message)

def recall():
    return "\n".join(memory_log[-5:])
