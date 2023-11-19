#import flask
from flask import Flask, render_template

app = Flask(__name__)

# if your web page is visited at the root url example www.google.com/ 
# This is triggered 
@app.route('/')
def index():
    return render_template('index.html')#displays our index.html file on the url


if __name__ == '__main__':
    app.run(debug=True)
