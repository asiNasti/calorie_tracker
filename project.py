from products import Products
from handlers import handle_new_item, get_food_selection


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

        see_total = input("Want to see a list of calories for today? y/n ").lower().strip()
        if see_total == "y":
            table = products.show_table()
            print(table)

        end = input("Do you want to finish? y/n ").lower().strip()
        if end == "y":
            print("Bye 🤘")
            print("💙 🇺🇦 💛")
            break


if __name__ == "__main__":
    main()
