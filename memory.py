# Mémoire simple en Python (version minimale)

memory_store = []

def save_memory(item: str):
    memory_store.append(item)
    return True

def get_memory():
    return memory_store
