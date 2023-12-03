from app import app
from db import db
import users

from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def index():
    sql = text("SELECT * FROM recipes3 WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id":users.user_id()})
    recipes = result.fetchall()
    return recipes

def create(name, ingredients, steps):
    sql = text("INSERT INTO recipes3 (name, user_id, ingredients, steps) VALUES (:name, :user_id, :ingredients, :steps)")
    db.session.execute(sql, {"name":name, "user_id":users.user_id(), "ingredients":ingredients, "steps":steps})            
    db.session.commit()

def result():
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    steps = request.form["steps"]
    create(name, ingredients, steps)
    return [name, ingredients, steps]

def recipe(id):
    sql = text("SELECT name FROM recipes3 WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()
    sql = text("SELECT ingredients FROM recipes3 WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    ingredients = result.fetchone()
    sql = text("SELECT steps FROM recipes3 WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    steps = result.fetchone()
    return [id, name[0], ingredients[0], steps[0]]

