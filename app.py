from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)

def run_diet_generator():
    #output = subprocess.check_output(['py', 'meal_plan_generator.py'], universal_newlines=True)
    subprocess.run(['py', 'meal_plan_generator.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #list = output.split("\n")
    #return list

@app.route("/")
def index():
    
    calories = request.args.get("calories")
    try:
        if calories is not None:
            
            with open('calories.txt', 'w') as file:
                file.write(str(calories))
            
            #result = run_diet_generator()
            run_diet_generator()
            #print(result)
            # Read the content of the text file
            with open('recipe.txt', 'r') as file:
                meal_plan_content = file.read()

            # Split the content into recipes using a unique delimiter
            recipes = meal_plan_content.split('\n\n') 
            for recipe in recipes:
                print(recipe)
            #text = "Whatever"

            
            return render_template('index.html', recipes = recipes)
    except:
        pass
    return render_template('index.html')


