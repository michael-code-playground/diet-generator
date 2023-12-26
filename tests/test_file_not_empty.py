
#!/usr/bin/env python3

import os

def test_file_not_empty():
    # Assuming your script is one level up from the test file
    script_path = os.path.join("..", "meal_plan_generator.py")

    # Replace 'path/to/your/file.txt' with the actual path to your text file
    file_path = os.path.join("..", "recipe.txt")

    # Check if the script file exists
    assert os.path.exists(script_path), f"Script file '{script_path}' does not exist."

    # Check if the file exists
    assert os.path.exists(file_path), f"File '{file_path}' does not exist."

    # Check if the file is not empty
    assert os.path.getsize(file_path) > 0, f"File '{file_path}' is empty."

