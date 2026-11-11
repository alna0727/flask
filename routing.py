from flask import Flask
app = Flask(__name__)


@app.route('/')
def starting():
    return "Welcome to Flask"
@app.route('/home')
def home():
    return "This is home"
@app.route('/profile')
def profile():
    return "This is profile"
@app.route('/user/<username>')
def userpage(username):
    return f"Home page for:{username}"
@app.route('/post/<int:post_id>')
def posts(post_id):
    return f"Displaying blog post number:{post_id}"
@app.route('/message/<sender>/<recipient>')
def message(sender,recipient):
    return f"Hello I am {sender},how are you {recipient}?"

if __name__=='__main__':
    app.run(debug = True)