from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def compare_teams():
    response = requests.get('http://127.0.0.1:5000/')
    return render_template('index.html', teams=response.json()['Teams'])

@app.route('/teamvsteam', methods=['GET'])
def teamvsteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = requests.get('http://127.0.0.1:5000/api/teamvsteam?team1={}&team2={}'.format(team1, team2))
    return render_template('index.html', teamvsteam=response.json())

if __name__ == '__main__':
    app.run(debug=True, port=7000)
