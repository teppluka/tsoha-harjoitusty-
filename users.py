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
    sql = text("SELECT id, password FROM users WHERE username=:username")
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
    sql = text("SELECT COUNT(*) FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username}).fetchone()
    if result[0] != 0:
        return False
    else:
        hash_value = generate_password_hash(password)

        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()

    return

def search(query):
    sql = text("SELECT id, username FROM users WHERE username LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    users = result.fetchall()
    if len(users) == 0:
        return 0
    return users

def user(id):
    sql = text("SELECT username FROM users WHERE id=:id")
    result = db.session.execute(sql, {"id":id}).fetchone()
    return result[0]

def friends():
    sql = text("SELECT f.user2 id, u.username username FROM friends f JOIN users u ON f.user1=:id AND f.user2 = u.id")
    result = db.session.execute(sql, {"id":user_id()}).fetchall()
    return result

def friend_requests():
    sql = text("SELECT f.id r_id, f.sender id, u.username username FROM friendrequests f JOIN users u ON f.sender = u.id and f.receiver=:id AND f.visible = TRUE")
    result= db.session.execute(sql, {"id":user_id()}).fetchall()
    return result

def send_request(id):
    sql = text("SELECT COUNT(*) FROM friendrequests WHERE (sender=:sender AND receiver=:receiver) OR (sender=:receiver AND receiver=:sender) AND visible = TRUE")
    result = db.session.execute(sql, {"sender":user_id(), "receiver":id}).fetchone()
    if result[0] == 0:
        sql = text("SELECT COUNT(*) FROM friends WHERE user1=:user1 AND user2=:user2")
        result = db.session.execute(sql, {"user1":user_id(), "user2":id}).fetchone()
        if result[0] == 0:
            sql = text("INSERT INTO friendrequests (sender, receiver, visible) VALUES (:sender, :receiver, TRUE)")
            db.session.execute(sql, {"sender":user_id(), "receiver":id})
            db.session.commit()

def accept(id, r_id):
    sql = text("INSERT INTO friends (user1, user2) VALUES (:user1, :user2)")
    db.session.execute(sql, {"user1":id, "user2":user_id()})
    db.session.execute(sql, {"user1":user_id(), "user2":id})
    sql = text("UPDATE friendrequests SET visible=FALSE WHERE id=:id")
    db.session.execute(sql, {"id":r_id})
    db.session.commit()

def reject(r_id):
    sql = text("UPDATE friendrequests SET visible=FALSE WHERE id=:id")
    db.session.execute(sql, {"id":r_id})
    db.session.commit()