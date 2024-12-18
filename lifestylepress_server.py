from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("index2.html")

@app.route("/page3")
def page3():
    return render_template("index3.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/article1")
def article1():
    return render_template("article1.html")

@app.route("/article2")
def article2():
    return render_template("article2.html")

if __name__ == "__main__":
    app.run()