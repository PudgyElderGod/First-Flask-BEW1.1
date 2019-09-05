#Imports
from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

#Lists
compliments = ['coolio', 'smashing', 'neato', 'fantabulous', 'radicool']
horoscopes = ['Aries: Polish them horns.', 'Pisces: Do not eat seafood, you cannibal.', 'Sagitarius: Practice your archery. The olympics are coming.', 'Capricorn: stop being a big nerd.']


#Functions
@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, 3)

    return render_template(
        'compliments.html',
        name=name,
        show_compliments=show_compliments,
        compliments=compliments_to_show)
# @app.route('/compliment')
# def get_compliment():
#     """Give the user a compliment"""
#     name = request.args.get('name')
#     show_compliments = request.args.get('show_compliments')
#     compliment = choice(compliments)
#     compliments_to_show = sample(compliments, 3)
#
#     return render_template(
#         'compliments.html',
#         name=name,
#         show_compliments=show_compliments,
#         compliment=compliment),
#         compliments=compliments_to_show


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    section = 'BEW 1.1 Section A'
    greeting = 'Good Morning'
    return render_template('index.html',
    section = section,
    greeting = greeting
    )



@app.route('/horoscope')
def get_horoscope():
    horoscope = choice(horoscopes)
    return f'Hello, user! {horoscope}'



if __name__ == "__main__":
   app.run(debug=True)
