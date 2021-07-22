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

# <> denotes a route variable.
@app.route('/profile/<users_name>')
def profile(users_name):
    return"<h2>Hello, " + users_name + "!</h2>"

@app.route("/date/<month>/<day>/<year>")
def displayGivenDate(month, day, year):
    return f"{month} / {day} / {year}"

# creating a <form>
formData = f""" 
    <form action="/result" method="GET">
        What's your favorite pizza flavor?
        <input type="text" name="pizza_flavor">
        <br>
        What's your favorite crust type?
        <input type="text" name="crust">
        <input type="submit" value="submit pizza">
    </form>
    """

@app.route("/formExample")
def firstForm():
    return formData

@app.route("/result")
def resultPage():
    return "<p>Hey</p>"

# turn the server on for serving
if __name__ == "__main__":
    app.run(debug=True, port=3000)