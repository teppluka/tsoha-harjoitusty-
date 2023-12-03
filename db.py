from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"
db = SQLAlchemy(app)

