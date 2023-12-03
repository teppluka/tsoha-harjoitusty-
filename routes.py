from app import app
import recipes
import users

from flask import render_template, request, redirect, session

@app.route("/")
def index():
    info = recipes.index()
    return render_template("index.html", recipes = info)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    info = recipes.result()
    return render_template("result.html", name=info[0], ingredients=info[1], steps=info[2])


@app.route("/recipe/<int:id>")
def recipe(id):
    info = recipes.recipe(id)
    return render_template("recipe.html", id=info[0], name=info[1], ingredients=info[2], steps=info[3])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":       
        if not users.login():
            return render_template("error.html")
        
    return redirect("/")

@app.route("/logout")
def logout():
    del session["user_id"]
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        users.register()
        return redirect("/")
