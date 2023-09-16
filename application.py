# simple flask "hello world" sample
# from: https://flask.palletsprojects.com/en/1.1.x/quickstart/

# python dependencies are declared in the requirements.txt file
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
