import subprocess 

cal = 2500
output = subprocess.check_output(['py', 'meal_plan_generator.py', str(cal)], universal_newlines=True)
list = output.split("\n")
print(list)
