import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "Trivia"
        self.database_path = "postgres://{}/{}".format('vagrant:sohaib@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # new question 
        self.new_quetion = {
            'question' : 'What time is it ?',
            'answer' : 'the test if failing oh-lock !!',
            'category' : 1,
            'difficulty' : 5
        }            
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = res.get_json()
       

        self.assertEqual(data['success'] , True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_categories'])
        self.assertEqual(res.status_code, 200)

    def test_pagination_not_allowed_for_category(self):
        res_no_endpoint = self.client().get('/categories/1')

        self.assertEqual(res_no_endpoint.status_code, 404)

    def test_404_request_beyond_valid_pages_for_category(self):
        res_no_endpoint = self.client().get('/categories/9999/questions')
        
        self.assertEqual(res_no_endpoint.status_code, 404)

    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'] , True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['total_questions'])
        
    def test_404_request_beyond_valid_pages_for_questions(self):
        res_no_page= self.client().get('/questions?page=999')
        
        self.assertEqual(res_no_page.status_code, 404)

    def test_get_all_questions(self):
        res = self.client().get('/questions')
        res_no_page= self.client().get('/questions?page=999')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_no_page.status_code, 404)
    
    def test_add_question(self):
        res = self.client().post('/questions', json={"question":"question","answer":"answer","difficulty":"difficulty","category":2} )
    
    def test_non_complete_data_add_question(self):
        res = self.client().post('/questions', json={"answer":"answer","difficulty":"difficulty","category":2} )

        self.assertEqual(res.status_code, 422)

    def test_delete_question(self):
        res = self.client().delete('/questions/5')
        data = res.get_json()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
    
    def test_delete_non_existing_question(self):
        res = self.client().delete('/questions/999')
        
        self.assertEqual(res.status_code, 404)

    
    def test_search_question(self):
        res = self.client().post('/questions/search', json={"searchTerm":"a"})
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])

    def test_search_non_existing_question(self):
        res = self.client().post('/questions/search', json={"searchTerm":"$$$$"})
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['questions'] , [])
        
    def test_quizzes(self):
        res = self.client().post('/quizzes' , json={"previous_questions":[],"quiz_category":{"type":"Geography","id":"2"}})
        data = res.get_json()
   
        self.assertTrue(data['question'])

    def test_quizzes_non_existing(self):
        res = self.client().post('/quizzes' , json={"previous_questions":[14,15,17],"quiz_category":{"type":"Geography","id":"2"}})
        data = res.get_json()
   
        self.assertEqual(data['question'], None)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()