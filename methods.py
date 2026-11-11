from flask import Flask
app = Flask(__name__)
@app.route('/retrieve',methods=['GET'])
def get_item():
    items={
        "Book" : 60,
        "pen" : 10,
        "Nails" : 20,
        "Pot" : 40
    }
    payload = {
        "message" : " I got these items in stock, Tell me what you want",
        "items" : items
    }
    return payload
if __name__=='__main__':
    app.run(debug = True)