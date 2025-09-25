# 🍎 Calorie Tracker
A learning project for tracking calories
Implemented as a console application in Python

## Example Output
Enter food name: apple pie 

Found 👇
1. Mr Kipling Bramley Apple Pies 6pk - 355 calories/100g
2. Cheese & Onion Pasty - 286 calories/100g
3. Apple Pie Bars - 424 calories/100g
   
   ...
   
If your dish is not here, enter '0', otherwise enter the dish number: 3

Enter product grams/ml: 200

Food added✅

Want to see a list of calories for today? y/n y

+----------------+------------+------------+

| Name           | Grams/ml   |   Calories |

+================+============+============+

| Apple Pie Bars | 200.0      |        848 |

+----------------+------------+------------+

| Total          | -          |        848 |

+----------------+------------+------------+

## How It Works
- User enters the food name
- The program searches for matching products using OpenFoodFacts API
- User selects a product and specifies the amount in grams/ml
- The program adds it to the list and calculates the calories
- The summary table shows all selected items and the total calories
