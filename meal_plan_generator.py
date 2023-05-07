import PyPDF2 
import os
import re
import random
from collections import OrderedDict


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

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
recipes_path = os.path.join(desktop_path, "NUTRITION")

main_recipes_storage = OrderedDict()
folders_in_nutrition = os.listdir(recipes_path)
for folder in folders_in_nutrition:
    current_folder = os.path.join(recipes_path, folder)
    files = os.listdir(current_folder)
    storage = []
      
    for file in files:
        seperate_file = []
        with open(os.path.join(current_folder, file), 'rb') as file:
            reader = PyPDF2.PdfReader(file, strict = False)
            
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
            
    current_folder_name = os.path.basename(current_folder)
    if current_folder_name not in main_recipes_storage:
         main_recipes_storage[current_folder_name] = storage

#print(main_recipes_storage)         
#print(storage)   

while True:
    menu = []
    calories = 0
    
    for category in main_recipes_storage:
            random_book = random.choice(main_recipes_storage[category])
            meal_tuple = random.choice(random_book)
            book_number = main_recipes_storage[category].index(random_book)+1
            meal, page_no = meal_tuple
            calories = calories + meal
            menu_pos = meal, page_no, book_number
            menu.append(menu_pos)
    
    if calories > 2300 and calories < 2600:
        break      

calories = 0
for pos in  menu:
    meal, page_no, book_no = pos
    print(f'See page {page_no}, in the book {book_no}, you will be fuelled with {meal} kcal')
    calories = calories + meal

print(f'Your daily intake: {calories}')







