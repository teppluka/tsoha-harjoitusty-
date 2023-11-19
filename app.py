from urllib import request
from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
db = SQLAlchemy(app)


@app.route("/")
def index():
    result = db.session.execute(text("SELECT * FROM recipes"))
    recipes = result.fetchall()
    return render_template("index.html", recipes = recipes)

@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/result", methods=["POST"])
def result():
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]
    create(name, ingredients, steps)
    return render_template("result.html", name=name, ingredients=ingredients, steps=steps)

def create(name, ingredients, steps):
    sql = text("INSERT INTO recipes (name, ingredients, steps) VALUES (:name, :ingredients, :steps)")
    db.session.execute(sql, {"name":name, "ingredients":ingredients, "steps":steps})
    db.session.commit()

@app.route("/recipe/<int:id>")
def recipe(id):
    sql = text("SELECT name FROM recipes WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()
    sql = text("SELECT ingredients FROM recipes WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    ingredients = result.fetchone()
    sql = text("SELECT steps FROM recipes WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    steps = result.fetchone()
    return render_template("recipe.html", id=id, name=name[0], ingredients=ingredients[0], steps=steps[0])

