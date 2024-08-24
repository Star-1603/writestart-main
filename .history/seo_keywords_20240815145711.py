import os
import openai
from models.chat import chat

message_history = []

def get_seo_keywords(product_title):
    seo_prompt = f"Generate SEO keywords for the product titled '{product_title}'."
    seo_result = chat(seo_prompt, message_history)
    return seo_result.strip().split(', ')


product_name = "Neem Facewash"
seo_keywords = get_seo_keywords(product_name)
print(f"SEO Keywords: {seo_keywords}")