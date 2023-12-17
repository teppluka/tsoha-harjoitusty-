from app import app
from db import db
import users

from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def index():
    sql = text("SELECT * FROM recipes WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":users.user_id()})
    recipes = result.fetchall()
    return recipes

def create(name, ingredients, steps):
    sql = text("SELECT COUNT(*) FROM recipes")
    id = db.session.execute(sql).fetchone()[0] + 1

    txt = ingredients.split("\n")
    ing = []
    for i in txt:
        ing.append(i.strip())
    txt = steps.split("\n")
    stp = []
    for i in txt:
        stp.append(i.strip())

    sql = text("INSERT INTO recipes (name, user_id) VALUES (:name, :user)")
    db.session.execute(sql, {"name":name, "user":users.user_id()})
    for ingredient in ing:
        sql = text("INSERT INTO ingredients (name, recipe) VALUES (:ingredient, :id)")
        db.session.execute(sql, {"ingredient":ingredient, "id":id})
    for step in stp:
        sql = text("INSERT INTO steps (name, recipe) VALUES (:step, :id)")
        db.session.execute(sql, {"step":step, "id":id})
    db.session.commit()

    return [name, ing, stp]

def result():
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]
    info = create(name, ingredients, steps)
    return info

def recipe(id):
    sql = text("SELECT name FROM recipes WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()
    sql = text("SELECT name FROM ingredients WHERE recipe=:id")
    result = db.session.execute(sql, {"id":id})
    ingredients = result.fetchall()
    sql = text("SELECT name FROM steps WHERE recipe=:id")
    result = db.session.execute(sql, {"id":id})
    steps = result.fetchall()
    return [id, name[0], ingredients, steps]

def friend_recipes(id):
    sql = text("SELECT * FROM recipes WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":id})
    recipes = result.fetchall()
    return recipes
