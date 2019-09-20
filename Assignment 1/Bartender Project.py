import random
questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
"e": "For exit!"
}

ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def chooses(questions, ingredients):
  for k,v in questions.items():
    print(k + " : " + v)
  choices = input("Enter your choice: ")
  if choices == "e":
    print("You exited the program !")
    exit(0)
    if choices in ingredients:
      for i,j in ingredients.items():
        if choices == i:
          print(random.choice(j))





print(chooses(questions, ingredients))
