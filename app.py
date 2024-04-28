from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 8000), debug=True)