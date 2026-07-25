from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def compare_teams():
    response = requests.get('http://127.0.0.1:5000/')
    return render_template('index.html', teams=response.json()['Teams'])


if __name__ == '__main__':
    app.run(debug=True, port=7000)
