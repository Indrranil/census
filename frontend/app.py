from flask import Flask, render_template
import json

app = Flask(__name__)

def load_news_data(filename='news_data.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading news data: {e}")
        return []

@app.route('/')
def index():
    news_articles = load_news_data()
    print(news_articles)  # Debug line to check JSON content
    return render_template('index.html', news_articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)
