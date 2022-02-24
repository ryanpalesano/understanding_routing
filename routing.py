from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/Dojo!')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello(name):
    return f"Hi {name}"

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/repeat/<int:num>/<string:word>')
def repeat_phrase(num, word):
    output = ''
    for i in range(0, num):
        output += f"<p>{word}</p>"
    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)