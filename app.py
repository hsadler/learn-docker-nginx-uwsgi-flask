
from flask import Flask


# init Flask instance
app = Flask(__name__)


# route examples
@app.route('/')
def index():
    return 'I\'m the index.'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/profile/<username>')
def profile(username):
    return 'This is the profile for "%s"' % username

@app.route('/userpage/<username>/<int:page_number>')
def userpage(username, page_number):
    return  username + "'s page number: " + str(page_number)


# run the app if executed as main file to python interpreter
if __name__ == '__main__':
    app.run()
