from products import Products


def main():
    products = Products()
    while True:
        food_name = input("Enter food name: ")
        try:
            results = products.get_food_list(food_name)
        except Exception:
            print("⚠️ Error while searching. Please try again later ⚠️")
            continue

        if results is None:
            handle_new_item(products, food_name)
        else:
            get_food_selection(products, results, food_name)

        see_total = clean_input(input("Want to see a list of calories for today? y/n "))
        if see_total == "y":
            table = products.show_table()
            print(table)

        end = clean_input(input("Do you want to finish? y/n "))
        if end == "y":
            print("Bye 🤘")
            print("💙 🇺🇦 💛")
            break

def clean_input(text):
    return text.lower().strip()

def handle_new_item(products, food_name):
    create_choise = clean_input(input("There is no such food. Wanna create? y/n "))
    if create_choise == "y":
        try:
            calories = float(input("Enter food calories: "))
            grams = float(input("Enter product grams/ml: "))
            products.create_food(food_name, calories, grams)
            print("Food created ✅")
        except ValueError:
            print("⚠️ Invalid input! Need numbers")


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


if __name__ == "__main__":
    main()
