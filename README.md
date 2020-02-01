# Trivia 
Trivia is a Fullstack CRUD Web App that is created for practiceto levrage api development.

the following functionalities are included:
1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

the backend cod follows PEP8 style guidelines (At least i tried to follow it :') )

## Getting Started 

Folder Structer the project has two main folders

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

### Pre-requsites and Local Development

You should already have Python3,pip and node installed on your local machines.

#### Backend

From the backend folder run pip install requirments.txt. All required packeges are included in the reuirements file.

run the application on development mode:

export FLASK_APP=flaskr
export FLASK_END=development
flask run

backend will run on localhost:5000

#### Frontend

From the backend folder run 
npm install 
napm start 

frontend will run on localhost:3000

#### Tests

in order to test the app, from the backend folder run :

dropdb Trivia
createdb Trivia
psql Trivia < Trivia.psql
python test_flaskr.py


## API Reference

Trivia API documentation is included in the files  API_documentation.md
2. [`./backend/`](./backend/API_documentation.md)


## Deployment 

the project is hosted locally only 

## Authors

Souhaib Benbouzid

https://github.com/Souhaib-Benbouzid

## Acknowledgement

Thanks to Udacity team for all the videos and information shared
