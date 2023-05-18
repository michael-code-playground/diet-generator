# Diet generator - concept

Simple project whose main objective is to facilitate decision-making process and save from the demanding dilemma which recipes to choose, considering we're faced with aboundance of cookbooks, we've accumulated in the hopes of working on our nutrition, in the form of PDF files we don't even want to open, let alone search all of them. The only thing the script expects a user to do, is enter their desired calorie intake, it then iterates through cookbooks and picks out random recipes matching the user's calorie intake (I assumed a slight deviation ~150 kcal). It displays results in a very comprehensive way - the user is provided with the information how many calories each meal contains, what book it comes from, and also what page each recipe is on - which shows the figure below: 

![result](https://github.com/michael-code-playground/diet-generator/assets/126971944/25e9d7d2-d8c4-4aa8-80a8-435ae9a1261f)

Here's also the graph illustarting what values I've got over the course of 10 days. 
![graph](https://github.com/michael-code-playground/diet-generator/assets/126971944/62f05486-6866-442e-8a7d-abbadd102bd1)


# Requirements

Based on my case, I assumed a user creates the catalog called 'NUTRITION', located on their desktop - within the folder there're seperate four dictionaries, I've named them simply breakfast, dinner, snacks, supper - each one contains PDF files with recipes suitable, according to me, for each meal.  

# Remarks

PyPDF2 framework expects PDF files to have a clear, coherent structure - in my case content seems scattered, that's why I defined a function filter_out, because some calorie values extracted from particular pages were mixed with number of a page which is at the bottom of each one, as a result instead of let's say 540 kcal - I got 23540 kcal. I also have to replace a comma with a dot, so that it's possible to convert values into float.I believe redefineing the regex could solve the issue, simplify the code by making it possible to get rid of that function, I haven't come up with an idea for it though.


