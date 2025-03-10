from typing import Dict

def get_reply(message: str) -> Dict[str, str]:
    return {"reply": f"You said: '{message}'. This is a mock reply."}