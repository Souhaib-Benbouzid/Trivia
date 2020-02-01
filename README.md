## Trivia API Docuemntaion 

Trivia is a simple REST API , The API endpoints return questions, answers, question categories in JSON format , directly from a local hosted  database.the API is developed for practice only on a local machine.  

### Getting Started

Base URL: the api is run locally and is not hosted.the backend is hosted at http://localhost:5000
API Keys : there is no authentication or keys needed.

### Errors
Errors are returned as JSON objects in the following format:

{
    "success": False,
    "error": 400,
    "message": "bad request"
}

on a fail requests The API return three error types :

- 400: Bad Request
- 404: Resource Not Found
- 422: Unprocessable Entity
- 405: Method Not Allowed

### Response Headers 

- Access-Control-Allow-Credentials: true
- Access-Control-Allow-Headers: Content-Type, Authorization
- Access-Control-Allow-Methods: GET, POST, PATCH, DELETE, OPTIONS
- Access-Control-Allow-Origin: http://localhost:3000

### Endpoints

#### GET /questions

- General:
    - Returns a an object contain a list of question objects  and a list of categories
    - Results are questions are paginated in groups of 10. include a request.argument to choose page number, starting from 1.
- Sample: curl http://localhost:5000/questions

{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 4, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 4, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 4, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 3, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 5, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 5, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 2, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 2, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }
  ], 
  "success": true, 
  "total_questions": 16
}

#### DELETE /questions

- General:
    - Delete a question based the question id 
    - Returns a list of question objects left that are paginated on groups of 10, a response success, and total number of questions left. 
- Sample: curl -X DELETE http://localhost:5000/questions/10

{
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 4, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 4, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 4, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 3, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 5, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 2, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 2, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 1, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ], 
  "success": true, 
  "total_questions": 15
}

#### POST /questions

- General:
    - add a new question 
    - Returns the new question id and list of question objects that are paginated on groups of 10, a response success, and total number of questions left. 
- Sample: curl -X POST -H "Content-Type: application/json" -d  '{"question":"What's the name","answer":"sohaib","difficulty":1,"category":1}' http://localhost:5000/questions

{
  "question_id": 34, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 4, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 4, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 4, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 3, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 5, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 2, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 2, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 1, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ], 
  "success": true, 
  "total_questions": 19
}


#### POST /question/search 
- General:
    - case insenstive search on questions based on a given search term provided in the request
    - Return list of obeject of all available categories and list of question objects that match the search alongside the total number of questions. 
    - restults are paginated on groups of 10.
- Sample: curl -X POST -H "Content-Type: application/json" -d  '{"searchTerm":"TEST"}' http://localhost:5000/questions/search

{
  "current_category": [
    {
      "id": 0, 
      "type": "Science"
    }, 
    {
      "id": 1, 
      "type": "Art"
    }, 
    {
      "id": 2, 
      "type": "Geography"
    }, 
    {
      "id": 3, 
      "type": "History"
    }, 
    {
      "id": 4, 
      "type": "Entertainment"
    }, 
    {
      "id": 5, 
      "type": "Sports"
    }
  ], 
  "questions": [
    {
      "answer": "test", 
      "category": 1, 
      "difficulty": 1, 
      "id": 34, 
      "question": "test"
    }
  ], 
  "total_questions": 19
}


#### GET /categories

- General:
    - Returns an object contain a list of categories available, total number of categories and request success and total categories number
    
- Sample: curl http://localhost:5000/categories

{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "success": true, 
  "total_categories": 6
}


#### GET /categories/id/questions

- General:
    -Returns a current category and list of all questions in the category along number of question in the category and status of the request
- Sample: curl  http://localhost:5000/categories/1/questions

{
  "current_category": "Art", 
  "questions": [
    {
      "answer": "Escher", 
      "category": 1, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "One", 
      "category": 1, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 1, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}

#### POST /quizzes 

- General:
    - Return a random question based on category questions. 
- Sample: curl -X POST -H "Content-Type: application/json" -d  '{"previous_questions":[],"quiz_category":{"type":"Art","id":"1"}}' http://localhost:5000/quizzes

{
  "question": {
    "answer": "Escher", 
    "category": 1, 
    "difficulty": 1, 
    "id": 16, 
    "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
  }
}















export FLASK_APP=__init__.py
export FLASK_ENV=development
flask run --host 0.0.0.0

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)
