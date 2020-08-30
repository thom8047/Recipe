# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:54:22 2020

@author: Kyle
"""

err = {'001': 'No Recipe Was Found', '002': 'Data Encryption Was Lost', '003': 'Not A Valid User Entry'}

class Meals:
    # Initate variables    
    def __init__(self, textName):
        self.FileName = textName
    
    def get_recipes(self):
        recipe = ''
        
        with open(self.FileName, 'r') as text:
            for line in text.readlines():
                dict_line = eval(line)
                
                recipe += dict_line['title'] + ':\n'
                for ing in dict_line['ingrediants']:
                    recipe += ing[1] + ' of ' + ing[0] + '\n'
                
        # ALWAYS NEED TO CLOSE
            text.close()
            return recipe
    
    def get_recipe(self, recipe):
        with open(self.FileName, 'r') as text:
            try:
                
                for line in text.readlines():
                    dict_line = eval(line)
                    if dict_line['title'].lower() == recipe:
                        recipe_ = recipe.capitalize() + ':\n'
                        for ing in dict_line['ingrediants']:
                            recipe_ += ing[1] + ' of ' + ing[0] + '\n'
                        
                        text.close()
                        return recipe_
                        
                else:
                    # Raise error if no recipe comes back
                    raise()
                    
            except:
                print('No Recipe Was Found: Err #001')
        
    def write_recipe(self):
        recipe = {'title': input("Let's write a recipe!\nTo write a recipe, we'll start with a name.\nNext we'll get the ingrediants with their respective serving size. Please use basic servings, such as '# cups' or '# tablespoons'. If you can read out the ingrediant and servings as '[# serving_size] of [ingrediant]' then you're doing it right! For unknown serving_size use things.\nTo finish the recipe, please DO NOT type any thing, ONLY PRESS THE ENTER KEY when asked for the 'Next Ingrediant: '. This will prompt a confirmation message and a read out of your recipe!\nIf you mess up, or want to delete the recipe, type: 'cancel' or 'x' in any case-setting. [Ex. 'CaNcEl' or 'canceL' or 'X' or 'x']. Thank you for reading through!\n\nName of recipe: ").capitalize(), 'ingrediants': []}
        
        user_ing = input('First Ingrediant: ').capitalize()
        while user_ing:
            if user_ing.lower() == 'cancel' or user_ing.lower() == 'x':
                if input('Are you sure you want to exit? [Y/N]: ').lower() == 'y':
                    user_ing = 'cancel'; break
                else:
                    user_ing = input('Next Ingrediant: ').capitalize()
                    continue
            list_of_ing = [user_ing, input('Number of servings: ').capitalize()]
            
            recipe['ingrediants'].append(list_of_ing)
            user_ing = input('Next Ingrediant: ').capitalize()
        if user_ing == 'cancel':
            return None
        else:
            if input("Are you sure you're finished and want to save the recipe? [Y/N]: ").lower() == 'y':
                print("\nHere's your recipe in a program-like format: ", recipe)
                return '\n' + str(recipe)
            else:
                print('Sorry! Data Encryption Was Lost: Err #002')
                return None
    
    def get_random_recipe(self):
        pass
    
def main():
    menu_text = " - Welcome to the Main Menu or the Recipe Script - \nType\n'get' - to get all recipes\n'write' - to write a new recipe\n'random' - to get random recipe\n\n"
    
    meal = Meals('C:/Users/Kyle/Desktop/Meals/recipes')
    x = input(menu_text).lower()
    while x:
        if x == 'get':
            y = input('Would you like to search up a recipe by title? [Y/N]: ').lower()
            if y == 'y':
                z = input('Title of recipe: ').lower()
                print(meal.get_recipe(z))
                x = input('Next command: ').lower()
            else:
                print(meal.get_recipes())
                x = input('Next command: ').lower()
                
        elif x == 'write':
            y = meal.write_recipe()
            if not(y):
                x = input('Next command: ').lower()
            else:
                with open(meal.FileName, 'a') as text:
                    text.write(x)
                    text.close()
                
                x = input('Next command: ').lower()
            
        elif x == 'random':
            # pass
        
            x = input('Next command: ').lower()
        else:
            print('Err #003: ' + err['003'] + '\n______________________________________________________________________')
            x = input('Next command: ').lower()
    else:
        print('______________________________________________________________________')
        
    
if __name__ == '__main__':
    main()
