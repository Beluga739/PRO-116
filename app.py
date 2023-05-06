# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Kishan Patel" 
    age = "14"

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/static/father.jpg")

# define the route to mother webpage
@app.route("/static/mother.jpg")

# define the route to friends webpage
@app.route("/static/friend.jpg")

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
