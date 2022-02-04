from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user_model
from flask import flash


class Word:
    db = "polyglot_test_db"
    def __init__(self, data):
        self.id = data['id']
        self.word_english = data['word_english']
        self.word_spanish = data['word_spanish']
        self.meaning = data['meaning']
        self.category = data['category']
        self.subcategory = data['subcategory']
        self.img_file_path = data['img_file_path']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_word(cls,data):
        query = "SELECT * FROM words WHERE category = %(category)s LIMIT 1 OFFSET %(pagenum)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls( results[0] )


    @classmethod
    def get_all_words(cls):
        query = "SELECT * FROM words;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_words = []
        for row in results:
            all_words.append(cls(row))
        return all_words

    

    


   
    

