# import the flask library for usage
from flask import Flask
# creat an instance of the flask server
# as the root directory within 'main.py'
app=Flask(__name__)

#create some routes
@app.route('/')
def displayHompage():
    return "<h1>Welcome to your first website</h1>"

@app.route('/route1')
def route1Info():
    return"<h3>Congrats you made route 1</h3>"

# turn the server on for serving
if __name__ == "__main__":
    app.run(debug=True, port=3000)