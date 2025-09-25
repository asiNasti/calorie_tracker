def handle_new_item(products, food_name):
    create_choise = input("There is no such food. Wanna create? y/n ").lower().strip()
    if create_choise == "y":
        calories = float(input("Enter food calories: "))
        grams = input("Enter product grams/ml: ")
        products.create_food(food_name, calories, grams)
        print("Food created ✅")


def get_food_selection(products, results, food_name):
    print("Found 👇")
    for index, name, calories in results:
        print(f"{index}. {name} - {calories} calories/100g")

    while True:
        try:
            food_index = int(
                input("If your dish is not here, enter '0', otherwise enter the dish number: "))
            food_grams = float(input("Enter product grams/ml: "))
            products.choose_food(food_index, food_grams)

            if food_index == 0:
                calories = float(input("Enter food calories: "))
                products.create_food(food_name, calories, food_grams)
                print("Food created✅")
            else:
                print("Food added✅")
            break
        except (IndexError, ValueError):
            print("⚠️ Invalid number. Please try again ⚠️")