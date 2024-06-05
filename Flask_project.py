# Basics of flask
# Q-1
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Q-2
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Q-3
from flask import Flask, request
app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name")
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Q-4
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    else:
        return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Q-5
from flask import Flask, session, request
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    session["username"] = username
    return "Logged in successfully!"

@app.route("/profile")
def profile():
    username = session.get("username")
    if username:
        return f"Welcome, {username}!"
    else:
        return "You are not logged in."

if __name__ == "__main__":
    app.run(host="0.0.0.0")

# intermediate 





