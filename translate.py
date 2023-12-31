from googletrans import Translator
import re

def translate(file_content):

    translator = Translator()

    #file_path = 'recipe.txt'

    #with open(file_path, 'r', encoding='UTF-8') as file:
        #file_content = file.read()

    translation = translator.translate(file_content, dest='en', scr='pl')
    return translation.text


#print("CLEANUP TEST - Ingredients")
#print()
# Extract Ingredients
# ingredients_pattern = re.compile(r'(\d+\s*g\s*\([^)]+\)\s*\S+(?:\s*\(.*?\))?.*?)(?:\n|$)')
# ingredients_matches = ingredients_pattern.findall(translation.text)
# ingredients_list = [match.strip() for match in ingredients_matches]

# # Print the extracted ingredients
# for ingredient in ingredients_list:
#     print(ingredient)


# print("CLEANUP TEST - Instructions")
# print()
# # Extract Instructions
# instructions_pattern = re.compile(r'(?:(?<=^)|(?<=\n))\d\.\s*(.*?)(?:\n\d\.\s*(.*?))*(?:\n|$)')
# instructions_matches = instructions_pattern.findall(translation.text)
# instructions_list = [match[0].strip() for match in instructions_matches]

# # Print the extracted instructions
# for instruction in instructions_list:
#     print(instruction)