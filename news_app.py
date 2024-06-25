from flask import Flask, render_template, jsonify, request
import requests
import cohere

app = Flask(__name__)

# Initialize Cohere client
co = cohere.Client('JzASWHGkKurcFzE1w0bP3roLLECjqz59yswgyjLc')

# News API key
news_api_key = 'c919c0052bc9439996c9cf4c65a18694'

# Define news categories
categories = ['General', 'Business', 'Technology', 'Entertainment', 'Sports', 'Science', 'Health']

def summarize_article(article_text):
    prompt = f"""
Summarize the following news article in approximately 150 words. 
Focus on the key points, main events, and essential details. 
Maintain a neutral tone and avoid personal opinions.
Include the most important who, what, where, when, why, and how information.
Ensure the summary is coherent and flows well.

News Article:
{article_text}

Now, please summarize the provided news article:

Summary:
"""
    
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=400,
        temperature=0.7,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"]
    )
    return response.generations[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/api/news/<category>')
def get_news(category):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={news_api_key}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    if not articles:
        return jsonify([])
    
    summarized_articles = []
    for article in articles[:5]:  # Limit to 5 articles for brevity
        title = article['title']
        content = article.get('content') or article.get('description') or article.get('title') or ""
        summary = summarize_article(content)
        summarized_articles.append({
            'title': title,
            'summary': summary,
            'url': article['url'],
            'image_url': article.get('urlToImage')
        })
    
    return jsonify(summarized_articles)

@app.route('/api/search')
def search_news():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])

    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={news_api_key}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    
    summarized_articles = []
    for article in articles[:1]:  
        title = article['title']
        content = article.get('content') or article.get('description') or article.get('title') or ""
        summary = summarize_article(content)
        summarized_articles.append({
            'title': title,
            'summary': summary,
            'url': article['url'],
            'image_url': article.get('urlToImage')
        })
    
    return jsonify(summarized_articles)

if __name__ == '__main__':
    app.run(debug=True)