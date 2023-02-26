from flask import render_template
from app import app
import openai

openai.api_key = "YOUR_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

