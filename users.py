from app import app
from db import db

from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash


app.secret_key = getenv("SECRET_KEY")

def user_id():
    return session.get("user_id", 0)

def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = text("SELECT id, password FROM users3 WHERE username=:username")
    result = db.session.execute(sql, {"username":username})

    user = result.fetchone()
    if user:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["user_id"] = user.id
            return True
    return False

def register():
    username = request.form["username"]
    password = request.form["password"]
    sql = text("SELECT COUNT(*) FROM users3 WHERE username=:username")
    result = db.session.execute(sql, {"username":username}).fetchone()
    if result[0] != 0:
        return redirect("/register")
    else:
        hash_value = generate_password_hash(password)

        sql = text("INSERT INTO users3 (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()

    return