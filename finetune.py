# Import the necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained("meta-ai/llama-2-7b-chat")
model = AutoModelForCausalLM.from_pretrained("meta-ai/llama-2-7b-chat")

# Define the prompt
prompt = "Hello, this is Llama 2. How are you today?"

# Encode the prompt and generate a response
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output_ids = model.generate(input_ids, max_length=50, do_sample=True, top_p=0.9)

# Decode the output and print it
output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output)