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

    print
    print session
    print

    #way #1 that doesn't work:
    # session.setdefault("history", []).append(random_fruit)

    #way #2 that doesn't work
    # if "history" in session:
    #     print "about to append", random_fruit
    #     session["history"].append(random_fruit)
    # else:
    #     print "creating history in session with", random_fruit
    #     session["history"] = [random_fruit]

    #way #3 (credit to Ally) which DOES work
    session["history"] = session.get("history", [])
    session["history"].append(random_fruit)

    print
    print session
    print

    return render_template("index.html", fruit=random_fruit,
                           history=session["history"])

if __name__ == "__main__":
    app.run(debug=True)
