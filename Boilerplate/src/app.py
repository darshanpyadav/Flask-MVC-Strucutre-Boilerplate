# -*- coding: utf-8 -*-
from flask import Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_htmlmin import HTMLMIN


driver = 'mysql'
db_username = 'root'
db_passwd = 'passwd'
db_host = 'localhost'
db_name = 'db_name'

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.secret_key = "SOSECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}/{}'.format(driver, db_username, db_passwd, db_host, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MINIFY_PAGE'] = True
HTMLMIN(app)
db = SQLAlchemy(app)

from .controllers import mainController
from .models import mainModel
from .routes import mainRouter
