
from flask import Flask
from flask import request


# init Flask instance
app = Flask(__name__)


################## ROUTE EXAMPLES ##################

# index
@app.route('/')
def index():
    return 'I\'m the index.'

# named route
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# dynamic route
@app.route('/profile/<username>')
def profile(username):
    return 'Profile for "%s"' % username

# typed/converted variables
@app.route('/userpage/<username>/<int:page_number>')
def userpage(username, page_number):
    return  username + "'s page number: " + str(page_number)

# specify GET, POST, etc.
@app.route('/get-or-post', methods=['GET', 'POST'])
def get_or_post():
    if request.method == 'GET':
        return 'A GET request was made..'
    elif request.method == 'POST':
        return 'A POST request was made..'

####################################################


# run the app if executed as main file to python interpreter
if __name__ == '__main__':
    app.run()
