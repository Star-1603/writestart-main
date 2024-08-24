import os
import openai
from models.chat import chat

# Initialize an empty message history
message_history = []

# Function to get SEO keywords based on product title
def get_seo_keywords(product_title):
    seo_prompt = f"Generate SEO keywords for the product titled '{product_title}'."
    seo_result = chat(seo_prompt, message_history)
    return seo_result.strip().split(', ')

# Define the product name
product_name = "Neem Facewash"

# Get the SEO keywords
seo_keywords = get_seo_keywords(product_name)

# Print the SEO keywords
print(f"SEO Keywords: {seo_keywords}")
