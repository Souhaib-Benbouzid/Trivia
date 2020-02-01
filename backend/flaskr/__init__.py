import os
from flask import Flask, request, abort, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs [done]
  '''
  CORS(app, resources={ r"*" : {'origins':'*'}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response
  '''

  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    categories = Category.query.order_by(Category.id).all()
    current_categories = [ category.format() for category in categories ]
    categories_type = [i["type"] for i in current_categories]

    if categories is None:
      abort(404)
    else:
      formated_catigories = [ category.format() for category in categories ]

      return jsonify({
        'success':True,
        'categories': categories_type,
        'total_categories': len(categories)
      })

    current_categories = [ category.format() for category in categories ]
    categories_type = [i["type"] for i in current_categories]


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  @app.route('/questions')
  def get_questions():
    questions = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, questions)

    categories = Category.query.order_by(Category.id).all()
    current_categories = [ category.format() for category in categories ]
    categories_type = [i["type"] for i in current_categories]

    if len(current_questions) == 0 :
      abort(404)
    
    return jsonify({
      'success':True,
      'questions': current_questions,
      'categories': categories_type,
      'total_questions': len(questions)
    })

  def paginate_questions(request, questions):
    page = request.args.get('page', 1, type = int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formated_questions = [ question.format() for question in questions ]
    
    return formated_questions[start:end]


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 
  
  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_questions(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()
      
      if question is None:
        abort(404)

      question.delete()
      
      questions = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, questions)

      return jsonify({
        'success':True,
        'questions': current_questions,
        'total_questions': len(questions)
      })
    except:
      abort(404)



  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def add_questions():
    body = request.get_json()

    new_question =  body.get('question', None)
    new_answer =  body.get('answer', None)
    new_category =  body.get('category', None)
    new_difficulty = body.get('difficulty', None)

    try:
      question = Question(question = new_question, answer = new_answer, category = new_category, difficulty=new_difficulty)
      question.insert()

      questions = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, questions)

      return jsonify({
        'success': True,
        'Created': question.id,
        'questions': current_questions,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)

    ''' curl -X POST -H "Content-Type: application/json" -d  '{ "answer": "what's my name ?", "category": 3, "difficulty": 2, "question": "Sohaib?" }' http://localhost:5000/questions
    '''
    



  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    body = request.get_json()
    search_term =  body.get('searchTerm', None)
    
    questions = Question.query.filter(Question.question.ilike("%{}%".format(search_term))).all()
    current_questions = [ question.format() for question in questions]

    categories = Category.query.all()
    if categories is None:
      abort(404)
    formated_catigories = [ category.format() for category in categories ]

    return jsonify({
        "questions": current_questions,
        "total_questions": len(Question.query.all()),
        "current_category": formated_catigories})
  

    ''' 
    curl -X POST -H "Content-Type: application/json" -d  '{ "searchTerm": "Sohaib?" }' http://localhost:5000/questions/search
    '''





  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def get_by_category(category_id):
    category = Category.query.filter(Category.id == category_id ).all()
    questions = Question.query.filter(Question.category == category_id).all()
    if questions is None:
      abort(404)
    else:
      current_questions = paginate_questions(request, questions)    
     

    if len(current_questions) == 0 :
      abort(404)
    
    return jsonify({
      'success':True,
      'questions': current_questions,
      'current_category':category[0].type,
      'total_questions': len(questions)
    })
    
    

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def get_quizzes():
    body = request.get_json()
    category = body.get('quiz_category')['id']
    previous_questions = body.get('previous_questions')
    
    if category == 0 :
      question = Question.query.filter(~Question.id.in_(previous_questions)).first()
    else:
      question = Question.query.filter(~Question.id.in_(previous_questions), Question.category == category).first()
    
    if question:
      current_question = question.format()
      return jsonify({
        "question" : current_question
      })
    else:
      return jsonify({
        "question" : None
      })


  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "sucess": False,
      "error": 422,
      "message": "Unprocessable Entity"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "Bad Request"
    }), 400

  @app.errorhandler(405)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "Method Not Allowed"
    }), 405


  return app

    