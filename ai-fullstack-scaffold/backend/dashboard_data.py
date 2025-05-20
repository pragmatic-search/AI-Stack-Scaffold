import json

def generate_summary(logs):
    count = len(logs)
    prompts = [log['prompt'] for log in logs]
    return {
        "total_requests": count,
        "unique_prompts": list(set(prompts))
    }
