#Imports
from flask import Flask, request
from random import choice

app = Flask(__name__) #Don't do these yet

#Lists
compliments = ['coolio', 'smashing', 'neato', 'fantabulous']
horoscopes = ['Aries: Polish them horns.', 'Pisces: Do not eat seafood, you cannibal.', 'Sagitarius: Practice your archery. The olympics are coming.', 'Capricorn: stop being a big nerd.']


#Functions
 #Don't touch this entire line block until the end of the class.
@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    compliment = choice(compliments)
    return f'Hello there, {name}! You are so {compliment}!'

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/compliment'>
        What is your name?
        <input type="text" name="name"></input>
        <button type="submit">Submit</button>
    </form>
    """
#Fuck the above

# Use this block for most of class.
# @app.route('/compliment')
# def get_compliment():
#     compliment = choice(compliments)
#     return f'Hello there, user! You are so {compliment}!'

@app.route('/horoscope')
def get_horoscope():
    horoscope = choice(horoscopes)
    return f'Hello, user! {horoscope}'



if __name__ == "__main__": #Don't do these yet.
   app.run(debug=True)
