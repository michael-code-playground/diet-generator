#!/usr/bin/env python3

import PyPDF2 
import os
import re
import random
from collections import OrderedDict

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
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    recipes_path = os.path.join(desktop_path, "NUTRITION")
    return recipes_path

#return folders in the main one
def return_list_of_folders():
    folders_in_nutrition = os.listdir("/home/ubuntu/tests/NUTRITION")
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
    current_folder = os.path.join("/home/ubuntu/tests/NUTRITION", folder)
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



for i in range(0,4):
    
    req_another_run = False 
    
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
        #extract a complete recipe
        
        current_folder = os.path.join("/home/ubuntu/tests/NUTRITION", folders_in_nutrition[count], "")
        file_path = current_folder+str(book_no)+".pdf"
        count = count + 1
        reader = PyPDF2.PdfReader(file_path)
        
        try:
            page = reader.pages[page_no]
        
            calories = calories + meal
            #redirect content to the file 
            with open("recipe.txt", 'a', encoding='utf-8') as file:
            
                file.write(f"{str(calories)}\n{page.extract_text()}\n")

            print(f'See page {page_no}, in the book {book_no}, you will be fuelled with {meal} kcal')
        
        except IndexError:
            
            print("Let me have a think")
            req_another_run = True
            
            with open("recipe.txt", 'w', encoding='utf-8') as file:
                file.write("")

            break

    if req_another_run == False:
        break

print(f'Your daily intake: {calories}')







