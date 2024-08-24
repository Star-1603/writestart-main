import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from logger import get_logger
from models.user_info import UserInfo
from models.chat import chat
from models.user_table import UserTable

load_dotenv()
print(load_dotenv())

message_history = []

user_table = UserTable

# Function to extract SEO keywords
def get_seo_keywords(product_title):
    seo_prompt = f"Generate SEO keywords for the product titled '{product_title}'."
    seo_result = chat(seo_prompt, message_history)
    return seo_result.strip().split(', ')

# Function to get tweets
def get_tweets(company_name, product_name, ideal_user, is_premium):
    user_input = f"""
    Write the first 30 Tweets for my company {company_name}.
    Our main product revolves around {product_name} and the ideal user is {ideal_user}.
    Rules:
    1. No hashtags
    2. Tweet 1-5 should be about the launch
    3. Tweet 6-10 should be about the problem the product solves
    4. Tweet 11-15 should be about how the product solves the problem
    5. Tweet 16-20 should be about testimonials
    6. Tweet 21-25 should be funny and engaging content
    7. Tweet 26-30 should be about the roadmap of the company's product.
    Make sure you give each tweet in a new line.
    """

    result = chat(user_input, message_history)
    
    if not is_premium:
        return "\n".join(result.split("\n")[:3])
    else:
        return result

# Function to get Instagram posts
def get_posts(company_name, product_name, ideal_user, is_premium):
    user_input = f"""
    Write the first 10 Instagram posts for my company {company_name} in the format:
    1. Caption
    2. Slide 1 Content
    3. Slide 2 Content
    Our main product revolves around {product_name} and the ideal user is {ideal_user}.
    Make sure you give each post in a new line.
    """

    result = chat(user_input, message_history)

    if not is_premium:
        return "\n".join(result.split("\n")[:3])
    else:
        return result

# Function to get blog posts
def get_blogs(company_name, product_name, ideal_user, is_premium):
    user_input = f"""
    Write the first 10 blogs for my company {company_name}.
    Our main product revolves around {product_name} and the ideal user is {ideal_user}.
    Make sure you give each blog in a new line.
    """

    result = chat(user_input, message_history)

    if not is_premium:
        return "\n".join(result.split("\n")[:3])
    else:
        return result

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        company_name = request.form['question1']
        product_name = request.form['question2']
        feature_name = request.form['question3']
        ideal_user = request.form.get('question4', 'Default Value or Placeholder')
        overview = request.form.get('overview', 'Default overview value')
        user_table.put_info(UserInfo.attach_random_id(company_name=company_name, ideal_user=ideal_user, product_name=product_name))
        
        # Step 5: Run SEO chat function before main chat function
        seo_keywords = get_seo_keywords(product_name)
        print(f"SEO Keywords: {seo_keywords}")

        user_input = f"My product is called {product_name}. Write a PRD of a feature {feature_name} for my product. An overview for the feature is: {overview}. Make sure to include keywords: {', '.join(seo_keywords)}."
        get_logger("experiment").info(message_history)
        gpt_resp = chat(user_input, message_history)
        splitted_gpt_resp = gpt_resp.split('\n')
        
        print(splitted_gpt_resp)
        resp = jsonify({
            'tweets': get_tweets(company_name, product_name, ideal_user, is_premium=True), 
            'posts': get_posts(company_name, product_name, ideal_user, is_premium=True), 
            'blogs': get_blogs(company_name, product_name, ideal_user, is_premium=True)
        })

        print(resp)
        for i in splitted_gpt_resp:
            resp = jsonify({'output': i})
        return resp
    return render_template('index.html')

@app.route("/admin")
def card_view():
    get_logger("card_view").info("card_view()")
    data = user_table.get_all_info()
    return render_template('user_info.html', data = data)


@app.route("/test")
def experiment():
    get_logger("experiment").info("experiment()")
    return "works"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
