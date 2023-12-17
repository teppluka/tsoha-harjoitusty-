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
    allow = users.allow(id)
    if not allow:
        message = "Ei oikeutta nähdä sivua"
        return render_template("error.html", message=message)
    
    delete = users.delete_possible(id)

    info = recipes.recipe(id)
    return render_template("recipe.html", id=info[0], name=info[1], ingredients=info[2], steps=info[3], delete=delete)

@app.route("/delete/<int:id>")
def delete(id):
    if users.delete_possible(id):
        recipes.delete(id)
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":       
        if not users.login():
            message = "Väärä tunnus tai salasana"
            return render_template("error.html", message=message)
        
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
        if not users.register():
            message = "Käyttäjätunnus on varattu"
            return render_template("error.html", message=message)
        return redirect("/")

@app.route("/search", methods=["GET"])
def search():
    query = request.args["query"]
    userlist = users.search(query)
    if userlist == 0:
        message = "Käyttäjiä ei löytynyt"
        return render_template("error.html", message=message)
    return render_template("search.html", userlist=userlist)

@app.route("/user/<int:id>")
def user(id):
    username = users.user(id)
    recipelist = recipes.friend_recipes(id)
    possible = users.request_possible(id)
    return render_template("user.html", id=id, username=username, recipes=recipelist, possible=possible)

@app.route("/friends")
def friends():
    requests = users.friend_requests()
    friendlist = users.friends()
    return render_template("friends.html", requests=requests, friends=friendlist)

@app.route("/request/<int:id>")
def send_request(id):
    users.send_request(id)
    return redirect("/friends")

@app.route("/accept/<int:id>/<int:r_id>")
def accept(id, r_id):
    users.accept(id, r_id)
    return redirect("/friends")

@app.route("/reject/<int:id>/<int:r_id>")
def reject(id, r_id):
    users.reject(r_id)
    return redirect("/friends")