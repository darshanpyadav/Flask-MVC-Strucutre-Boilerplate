# -*- coding: utf-8 -*-
from src.app import app, db


class Model(db.Model):
    __tablename__ = 'table_name'
    
    id = db.Column('id', db.Integer, primary_key=True)

    

    def __init__(self):
        pass