# API Development and Documentation 

## What are APIs ?

An application Programming Interface is a way for different systems to interract with one another.

## The benefit of API ?
- It doesn't expose the program implementation to those who shouldn't have the access to it.
- The API provides provide a standard way of access the application
- Makes it much easier to access the application's data

### How an API works ?

- A client sends a request to an API server
- The API server parse the request 
- If the request is formatted correctly the server queries the database for the data requested by the client or performs the action in the request (Delete, PATCH ...)
- The server formats the response and sends it back to the client
- The client renders the response according to its implementation 

## RESTful ( Representational State Transfe ) APIs 

Representational State Transfer is an architectural style introduced by Roy Fielding in 2000.

An API is RESTful if it follows the following REST principles:
- Client-Server: There must be both a client and a server in the architecture
- Uniform Interface: A rest architectur has a standardized way of accessing and processing data resources.
    - for the request: This include unique resource identifier (unique URL). 
    - for the response: Self-descriptive messages in the server response describe how to process the representation of the data resources 
- Stateless: Every client request is self-contained and the server doesn't need to store data to process the subsequent requests
- Cacheable & Layered System: Caching and layering to increase the network efficiency 


## HTTP Basics:

Hypertext Transfer Protocol (HTTP) is a protocol that provides a standardized way for computers to communicate with each other. 

### HTTP Protocol Features:

- Connectionless: When a request is sent, the client opens the connection; once a response is received, the client closes the connection. The client and server only maintain a connection during the response and request. Future responses are made on a new connection.
- Stateless: There is no dependencies between successive requests
- Not Sessionless: Utilizing headers and cookies, sessions can be created to allow each HTTP request to share the same context.
- Media Independent: Any type of data can be sent over HTTP as long as both the client and the server know how to handle the data format

### HTTP Protocol Elements:

- Universal Resource Identifiers (URI): http://www.example.com/tasks/term=homework
    It has certain components:
    - Scheme: specifies the protocol used to access the resource, HTTP or HTTPS. In our example http
    - Host: specifies the host that holds the resources. In our example www.example.com.
    - Path: specifies the specific resource being requested. In our example, /tasks.
    - Query: an optional component, the query string provides information the resource can use for some purpose such as a search parameter. In our example, /term=homework.

#### URI vs URL: the difference is between a URI (Universal Resource Identifier) and a URL (Universal Resource Locator).

The term URI can refer to any identifier for a resource—for example, it could be either the name of a resource or the address of a resource (since both the name and address are identifiers of that resource). In contrast, URL only refers to the location of a resource—in other words, it only ever refers to an address.

So, "URI" could refer to a name or an address, while "URL" only refers to an address. Thus, URLs are a specific type of URI that is used to locate a resource on the internet when a client makes a request to a server.

- Methods
- Requests
- Responses
- Status Codes

### HTTP Requests

HTTP requests are sent from the client to the server to initiate some operation.

#### Elements of HTTP requests:

- Path: The URL of the resource to be fetched, excluding the scheme and host
- Method: Defines the operation to be performed
- HTTP Version
- Headers: optional information, success as Accept-Language
- Body: optional information, usually for methods such as POST and PATCH, which contain the resource being sent to the server

#### Request Methods:

Different request methods indicate different operations to be performed. It's essential to attend to this to correctly format your requests and properly structure an API.
- GET: ONLY retrieves information for the requested resource of the given URI
- POST: Send data to the server to create a new resource.
- PUT: Replaces all of the representation of the target resource with the request data
- PATCH: Partially modifies the representation of the target resource with the request data
- DELETE: Removes all of the representation of the resource specified by the URI
- OPTIONS: Sends the communication options for the requested resource

### HTTP Responses

After the request has been received by the server and processed, the server returns an HTTP response message to the client. The response informs the client of the outcome of the requested operation.

#### Elements of HTTP response

- Status Code & Status Message
    - Codes fall into five categories:
        - 1xx Informational
        - 2xx Success
        - 3xx Redirection
        - 4xx Client Error
        - 5xx Server Error
    - HTTP Version
    - Headers: similar to the request headers, provides information about the response and resource representation. Some common headers include: Date
    - Content-Type: the media type of the body of the request
    - Body: optional data containing the requested resource

## Flask 

### Flask Set Up Summary

Starting any Flask app will follow the same general flow for a simple application. The steps below are the same steps as taken in the screencast and can be referenced if you get stuck during the exercise.

### Directory & Virtualenv Set Up

Create the project directory mkdir [project_name] and navigate into it
Install flask using pip pip3 install flask
Make the flaskr directory and flaskr/__init__.py file within it
At this point you're ready to start working on your app!

### Create_app

In our setup, we will configure the basic Flask app. In these notes, I'll also include how to set up the application to handle specialized configuration.

### Basic App

- Import your dependencies
    from flask import Flask, jsonify
- Define the create_app function with parameter test_config initially set to None. Then within the function:
- Define the application. Ensure you include the first parameter. __name__is the name of the current Python module.
    app = Flask(__name__)
- Return the app instance.
    return app

### Configured Application

The below information is for your reference and related information can be found in the Flask documentation. You are expected to use the basic application set up for this course. However, as you build larger applications that utilize multiple environments and configurations (production, development, testing, etc) this knowledge will be helpful for streamlining your development process.

- Import additional dependencies. You'll need to import os in order to access the operating system and file structure import os

- Set up your default configuration. When working in development your SECRET_KEY can be hardcoded as shown but for production should come from a secret environment variable. DATABASE is the path for the database file.

app.config.from_mapping( SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite') )

- If a config.py file is included in the instance folder, use its values to override the default configuration, for instance the SECRET_KEY. You can also enable a testing configuration if it was passed into the create_app function.

if test_config is None:
  // load the instance config, if it exists, when not testing
 app.config.from_pyfile('config.py', silent=True)
else:
 // load the test config if passed in
 app.config.from_mapping(test_config)

- Make the instance path directory. The app will create the database file within that directory so it needs to exist.

try:
 os.makedirs(app.instance_path)
except OSError:
 pass

### First Endpoint with JSON

@app.route('/')
def hello_world():
    return 'Hello, World!'

return jsonify({'message':'Hello, World!'})

### Run your application
In the command line, you'll run three lines of code. The first two lines tell the terminal where to find your application and to run it in development mode, which allows you to keep it running while it hotloads any modifications. The third actually starts the application. If running your application on Windows

export FLASK_APP=flaskr                        # has to be run in the flaskr directory 
export FLASK_ENV=development
flask run

### Directory layout
without a frontend 

└──  project directory    

    └── flaskr
    
        └── __init__.py    

with a frontend

└──  project directory      

    ├── frontend

    └── backend

        └── flaskr

            └── __init__.py    

## Testing the response using Curl

curl -X POST http://www.example.com/tasks/

### Curl Options

You can find more options by entering curl --help in the terminal. Some frequently used options are:
    -X or --request COMMAND
    -d or --data DATA
    -F or --form CONTENT
    -u or --user USER[:PASSWORD]
    -H or --header LINE

## Organizing API Endpoints

### Principles
- Should be intuitive
- Organize by resource
    - Use nouns in the path, not verbs
    - The method used will determine the operation taken
        GOOD:
        https://example.com/posts

- Keep a consistent scheme
    - Plural nouns for collections
    - Use parameters to specify a specific item
        GOOD:
        https://example.com/entrees
        https://example.com/entrees/5

- Don’t make them too complex or lengthy
    - No longer than collection/item/collection
        GOOD:
        https://example.com/entrees/5/reviews

## CORS 
The same-origin policy is a concept of web security that allows scripts in Webpage 1 to access data from Webpage 2 only if they share the same domain. This means that the above error will be raised in the following cases:

Different domains
Different subdomains (example.com and api.example.com)
Different ports (example.com and example.com:1234)
Different protocols (http://example.com and https://example.com)
### common CORS headers 
- Access-Control-Allow-Origin
What client domains can access its resources. For any domain use *
- Access-Control-Allow-Credentials
Only if using cookies for authentication - in which case its value must be true
- Access-Control-Allow-Methods
List of HTTP request types allowed
- Access-Control-Allow-Headers
List of http request header values the server will allow, particularly useful if you use any custom headers

## Flask-CORS
Flask-CORS library to enable CORS.

### Installation
In order to install Flask-CORS simply run

pip3 install -U flask-cors

### Initialization
Once Flask-CORS is installed, you simply import the CORS function and call it with your app instance as a parameter. This will intialize Flask-CORS will all default options.

from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)

### Resource-Specific Usage
There are multiple options you can use to specify your Flask-CORS behavior. One typical one is resources, which contains a dictionary whose keys are regular expressions and values are dictionary or kwargs

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

### Route-Specific Usage
If you need to enable CORS on a given route, like those non-simple requests, you can use @cross_origin() to enable it.

@app.route("/hello")
@cross_origin()
def get_greeting():
    return jsonify({'message':'Hello, World!'})

### Flask Route Decorator
You've already seen the @app.route decorator used in its most basic form like so:

@app.route('/hello')
def get_greeting():
    return jsonify({'message':'Hello, World!'})
In addition, the @app.route decorator can handle Variable Rules and multiple HTTP methods

### Variable Rules
In our endpoint naming scheme we follow collection/item/collection. In order to handle that variable item. In order to handle that variability in Flask, you add a <variable_name> within the path argument of the `@app.route` decorator, which is then passed to the function as a keyword argument variable_name.

You can also specify the type of the argument by using <converter:variable_name> syntax.

@app.route('/entrees/<int:entree_id>')
def retrieve_entree(entree_id):
    return 'Entree %d' % entree_id

### HTTP Methods
By default, the @app.route decorator answers only get requests. In order to enable more requests types, pass the method parameter to the decorate including a list of string methods.

@app.route('/hello', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        return create_greeting()
    else:
        return send_greeting()

### Pagination in Flask
When handling large collections of data, attempting to serialize and send all of that data to the frontend will slow down the response and rendering to the client.

A common way to handle this issue is to paginate the data you're sending, and send it in chunks instead. Similar to variables discussed above, flask can handle request arguments to get additional request conditions such as page or search terms.

### Query Parameters
The below examples show the format of query parameters. When writing query parameters convention dictates that:

A question mark precedes the query parameters
Parameters are in key=value pairs with an equal sign in between the key and value
Sets of parameters are separated by an ampersand
www.example.com/entrees?page=1

www.example.com/entrees?page=1&allergens=peanut

### Request Arguments
In flask, when a request is received with query params the route in the @app.route decorator remains the same and the request object arguments contains the parameter. You access it as shown below. request.args is a Python dictionary so we use the get method to access the value and provide a default value, in this case 1.

@app.route('/entrees', methods=['GET'])
  def get_entrees():
    page = request.args.get('page', 1, type=int)

### Error Handling  / Flask Error Handling 
When you use the abort method, the default response is not digestible for the client or user.

In addition, we want to ensure all of our server responses have consistent formatting and that we provide adequate information to the client regarding the error. The `@app.errorhandler` decorator allows you to specify the behavior for expected errors. When using this decorator take into consideration:

passing the status code or Python error as an argument to the decorator
logical naming of the function handler

consistent formatting and messaging of the JSON object response
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404

## Test an API

As with all tests, writing unittests for your API verifies the behavior. For APIs, test should be written:

To confirm expected request handling behavior
To confirm success-response structure is correct
To confirm expected errors are handled appropriately
To confirm CRUD operations persist

## Unittest Flask Key Structures
