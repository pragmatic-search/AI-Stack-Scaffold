from transformers import pipeline

# Load model globally
text_generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt: str):
    result = text_generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']
