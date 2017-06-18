# -*- coding: utf-8 -*-
from src.app import app
from src.controllers.mainController import *
from flask import render_template


@app.route('/')
def index():
    return homeController.index()
