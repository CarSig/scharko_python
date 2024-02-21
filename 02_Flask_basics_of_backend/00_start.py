# how to install Flask
# pip install Flask

from flask import Flask,request,session
# The Flask class is imported from the flask module. An instance of this class will be our  application.

# request: The request object is used to access incoming request data.
# session: The sessions object is used to store information specific to a user from one request to the next.


# The Flask class is used to create an instance of the web application. The __name__ variable is passed to the Flask class. This is a special variable in Python that is used to store the name of the module. Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files. The __name__ variable is a convenient way to tell Flask where to look for templates, static files, and so on.



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# another that gets data from the request payload and also from header
@app.route("/getdata", methods=["GET", "POST"])
def getdata():
    if request.method == "POST":
        data = request.get_json()
        return data
    else:
        return 'getting data'
    
@app.route("/header")
def header():
    return request.headers.get("name")

@app.route("/session")
def session():
    session["name"] = "John"
    return "Session is set"





if __name__ == "__main__":
    app.run()

# The Flask module is imported and an instance of the Flask class is created. The route() decorator is used to specify the URL that should trigger the execution of the hello() function. The hello() function returns the string "Hello, World!" when the specified URL is accessed. The app.run() method is called to start the development server. The __name__ variable is set to "__main__" to ensure that the development server is started only when the script is executed directly, not when it is imported as a module. The development server is started on the default port 5000.
