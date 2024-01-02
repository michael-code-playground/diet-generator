from flask import Flask, render_template, request

app = Flask(__name__)

#def run_diet_generator(calories):


@app.route("/")
def index():
    calories = request.form.get('calories')
    return render_template('index.html')