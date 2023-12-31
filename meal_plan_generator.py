import PyPDF2 
import os
import re
import random
from collections import OrderedDict
from translate import translate

#delete unecessary characters, convert into float
def filter_out(search_result):
    filtered = (search_result.split()[0].strip()).replace(",",".")
    if len(filtered)== 5:
        if "." not in filtered:
            assigned = float(filtered[2:])
        else:
            assigned = float(filtered)
    elif len(filtered)== 7:
           assigned = float(filtered[2:])
    else:
        assigned = float(filtered)
    return assigned

#determine path desktop, catalog with cookbooks
def create_paths():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    recipes_path = os.path.join(desktop_path, "NUTRITION")
    return recipes_path

#return folders in the main one
def return_list_of_folders():
    folders_in_nutrition = os.listdir(create_paths())
    return folders_in_nutrition

#get user's input
def get_calorie_intake():
    while True:
        intake = int(input("Enter your intake: "))
        if intake > 0:
            break
        else:
            print("Try once again")
    return intake

    
main_recipes_storage = OrderedDict()
folders_in_nutrition = return_list_of_folders()
users_intake = get_calorie_intake()

#iterate through each catalog
for folder in folders_in_nutrition:
    current_folder = os.path.join(create_paths(), folder)
    files = os.listdir(current_folder)
    storage = []
    
    #iterate through each pdf file
    for file in files:
        seperate_file = []
        with open(os.path.join(current_folder, file), 'rb') as file:
            reader = PyPDF2.PdfReader(file, strict = False)
            
            #search every page
            for page in reader.pages:
                content = page.extract_text()
                
                result = re.search("\d{3}.*kcal", content)
                if result == None:
                    continue
                page_number= reader.get_page_number(page)
                show_result = filter_out(result.group())
                assignment = (show_result, page_number)  
                seperate_file.append(assignment)
            storage.append(seperate_file)        
    
    #create dictionary - assign recipes for each category
    current_folder_name = os.path.basename(current_folder)
    if current_folder_name not in main_recipes_storage:
         main_recipes_storage[current_folder_name] = storage

#repeat until criteria below is met   
while True:
    menu = []
    calories = 0
    
    #pick out random recipe for each meal
    for category in main_recipes_storage:
            random_book = random.choice(main_recipes_storage[category])
            meal_tuple = random.choice(random_book)
            book_number = main_recipes_storage[category].index(random_book)+1
            meal, page_no = meal_tuple
            calories = calories + meal
            menu_pos = meal, page_no, book_number
            menu.append(menu_pos)
    
    #break if calories fit user's requirement
    if calories > users_intake-200 and calories < users_intake+100:
        break      

calories = 0
#display results
count = 0
for pos in  menu:
    meal, page_no, book_no = pos
    print(f'See page {page_no}, in the book {book_no}, you will be fuelled with {meal} kcal')
    print()
    calories = calories + meal
    

    #extract a complete recipe
    path_desktop = create_paths()
    current_folder = os.path.join(path_desktop, folders_in_nutrition[count], "")
    file_path = current_folder+str(book_no)+".pdf"
    count = count + 1
    reader = PyPDF2.PdfReader(file_path)
    page = reader.pages[page_no]
    
    #redirect content to the file 
    with open("recipe.txt", 'a', encoding='utf-8') as file:
        
        content_en= translate(page.extract_text())
        # Extract Ingredients
        ingredients_pattern = re.compile(r'(\d+\s*g\s*\([^)]+\)\s*\S+(?:\s*\(.*?\))?.*?)(?:\n|$)')
        ingredients_matches = ingredients_pattern.findall(content_en)
        ingredients_list = [match.strip() for match in ingredients_matches]

        # # Print the extracted ingredients
        for ingredient in ingredients_list:
             print(ingredient)
             file.write(f"{str(calories)}\n{ingredient}\n")
        #file.write(f"{str(calories)}\n{content_en}\n")
        # # Extract Instructions
        instructions_pattern = re.compile(r'(?:(?<=^)|(?<=\n))\d\.\s*(.*?)(?:\n\d\.\s*(.*?))*(?:\n|$)')
        instructions_matches = instructions_pattern.findall(content_en)
        instructions_list = [match[0].strip() for match in instructions_matches]

        # Print the extracted instructions
        for instruction in instructions_list:
            print(instruction)


print(f'Your daily intake: {calories}')







