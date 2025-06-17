session_memory = {}

def add_to_memory(user_id: str, message: str):
    session_memory.setdefault(user_id, []).append(message)
    return session_memory[user_id]