from flask import Flask, session, render_template
from random import choice

app = Flask(__name__)
app.secret_key = 'this-should-be-something-unguessable'

the_list = ["apple", "berry", "cherry"]

# session = {}

@app.route("/")
def show_home():
    """blah"""

    random_fruit = choice(the_list)

    # session.setdefault("history", []).append(random_fruit)

    # if "history" in session:
    #     print session["history"]
    #     session["history"].append(random_fruit)
    #     print session["history"]
    # else:
    #     print "in else"
    #     session["history"] = [random_fruit]

    session["history"] = session.get("history", [])
    session["history"].append(random_fruit)

    # print session["history"]
    return render_template("index.html", fruit=random_fruit,
                           history=session["history"])

if __name__ == "__main__":
    app.run(debug=True)
