#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  minbatches = math.inf;
  try:
    for k in recipe: #basically we gonna compare item by items and even divide (//) and pick the lowest value
      minbatches = ingredients[k]//recipe[k] if ingredients[k]//recipe[k] < minbatches else minbatches;
  except KeyError:
    return 0; #because we got a keyvalue error because there is something in the recipe we dont have
  return minbatches;

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 1132, 'butter': 1248, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients));
