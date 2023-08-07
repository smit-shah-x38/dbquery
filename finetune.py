# Import the necessary libraries
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained("/var/basefolder_smit/dbq/localdata")
model = AutoModelForCausalLM.from_pretrained("/var/basefolder_smit/dbq/localdata")

# Define the prompt
prompt = 'Describe the charachter of Vito Corleone in the Godfather. Context: Vito Corleone is the main character in Mario Puzo\'s novel, "The Godfather," and is portrayed by Marlon Brando in the 1972 film adaptation directed by Francis Ford Coppola. Vito Corleone, also known as Don Vito, is a powerful and respected Italian-American crime boss who rules over the Corleone crime family with an iron fist. He is a ruthless and cunning leader who will stop at nothing to protect his family and his business.'

# Encode the prompt and generate a response
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output_ids = model.generate(input_ids, max_length=200, do_sample=True, top_p=0.9)

# Decode the output and print it
output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(output)
