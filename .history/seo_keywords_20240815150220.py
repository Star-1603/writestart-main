import openai
import os
from models.chat import chat

# Make sure to set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Your chat function should look something like this:
def chat(prompt, message_history):
    response = openai.completions.create(
        model="gpt-4",  # or another appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *message_history,
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']


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
