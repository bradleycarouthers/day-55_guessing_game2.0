#   higher_lower2.0
# website built using Flask and decorations

from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def headline():
    return "<h1>Guess a number between 1 and 10</h1>" \
           "<img src='https://media.giphy.com/media/fAo1Tv1OGE6AQZ2s0T/giphy.gif'>"


# Generate random number for answer
answer = random.randint(1, 10)


# Create route that can detect number entered by user
@app.route('/<int:user_guess>')
def guess(user_guess):
    # Added colored h1 tags and img for each scenario
    if user_guess < answer:
        return "<h1 style=color:red>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif'>"
    elif user_guess > answer:
        return "<h1 style=color:purple>Too high, try again...</h1>" \
               "<img src='https://media.giphy.com/media/fvpsznYW7rFTk9eSww/giphy.gif'>"
    else:
        return "<h1 style=color:green>Good job, you did it!</h1>" \
               "<img src='https://media.giphy.com/media/3ornjHL4fLS94x39Wo/giphy.gif'>"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
