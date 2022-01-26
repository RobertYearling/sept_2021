from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL

db = 'sept_class_db'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO classes ( first_name, last_name, email )
                    VALUES ( %(first_name)s, %(last_name)s, %(email)s );"""
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = " SELECT * FROM classes WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def user_validation(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 3:
            flash('First name has to be longer than 3 characters')
            is_valid = False
        if len(data['last_name']) < 3:
            flash('Last name has to be longer than 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('You have an invalid email address')
            is_valid = False
        return is_valid