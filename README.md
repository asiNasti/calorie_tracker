# 🍎 Calorie Tracker
#### Video Demo: <>

A learning project for tracking calories implemented as a console application in Python using the OpenFoodFacts API

## Features
- Search for food products via API.
- Add products to your daily list specifying weight in grams.
- Calculate total calories for the day.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/asiNasti/calorie_tracker.git
   cd calorie_tracker
   
2. **(Optional) Create and activate a virtual environment:**
   python -m venv venv
   
   Windows:
      `venv\Scripts\activate`
      
   macOS/Linux:
      `source venv/bin/activate`
   
3. **Install dependencies:**
   
   `pip install -r requirements.txt`

## Usage
Run the main script to start the tracker:
   `python project.py`

## Example Output
Enter food name: apple pie 

Found 👇
1. Mr Kipling Bramley Apple Pies 6pk - 355 calories/100g
2. Cheese & Onion Pasty - 286 calories/100g
3. Apple Pie Bars - 424 calories/100g
   
   ...
   
If your dish is not here, enter '0', otherwise, enter the dish number: 3

Enter product grams/ml: 200

Food added✅

Want to see a list of calories for today? y/n y

+----------------+------------+------------+
| Name           | Grams/ml   | Calories   |
+================+============+============+
| Apple Pie Bars | 200.0      | 848        |
+----------------+------------+------------+
| Total          | -          | 848        |
+----------------+------------+------------+

## How It Works
- User enters the food name
- The program searches for matching products using OpenFoodFacts API
- User selects a product and specifies the amount in grams/ml
- The program adds it to the list and calculates the calories
- The summary table shows all selected items and the total calories
