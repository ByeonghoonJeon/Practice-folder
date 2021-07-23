# WHY = seperate the python code from the HTML code and make it scalable!

# import the flask library for usage
from flask import Flask, request, render_template
# creat an instance of the flask server
# as the root directory within 'main.py'
app = Flask(__name__)

# create some routes


@app.route('/')
def displayHompage():
    return render_template('index.html')


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


@app.route("/formExample")
def firstForm():
    return render_template('form.html')


@app.route("/results", methods=['POST'])
def resultPage():
    pizza_flavor = request.form.get("pizza_flavor")
    crust = request.form.get("crust")
    return f"<h3>A {crust} crust {pizza_flavor} pizza has been ordered!</h3>"


@app.route('/pizza/submit', methods=['GET', 'POST'])
def submit_pizza():
    users_email = request.args.get('email')
    users_phone = request.args.get('phone')
    crust_type = request.args.get('crust')
    pizza_size = request.args.get('size')
    list_of_toppings = request.args.getlist('toppings')
    accepted_terms = request.args.get('terms_conditions')

    if accepted_terms != 'accepted':
        return 'Please accept the terms and conditions and try again!'

        # HTML being returned as plain text
    return f"""
    Your order summary: <br>
    Email: {users_email} <br>
    Phone number: {users_phone} <br><br>

    You ordered a {crust_type} crust pizza of size {pizza_size}-inch
    with the following toppings: {', '.join(list_of_toppings)}
    """


# turn the server on for serving
if __name__ == "__main__":
    app.run(debug=True, port=3000)
