from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)

def run_diet_generator(calories):
    output = subprocess.check_output(['py', 'meal_plan_generator.py', str(calories)], universal_newlines=True)
    list = output.split("\n")
    return list

@app.route("/")
def index():
    
    calories = request.args.get("calories")
    try:
        if calories is not None:
            result = run_diet_generator(calories)
            print(result)
           
    except:
        pass
    return render_template('index.html')


