from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/donate.html', methods=['POST', 'GET'])
def donate():
    return render_template('donate.html')

@app.route('/volunteer.html', methods=['GET'])
def volunteer():
    return render_template('create.html')

@app.route('/resource.html', methods=['GET'])
def resource():
    return render_template('resource.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')