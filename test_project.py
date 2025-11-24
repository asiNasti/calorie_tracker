import pytest
from products import Products

def test_create_and_count_total():
    tracker = Products()
    
    tracker.create_food("Apple", 50, 100)
    tracker.create_food("Banana", 100, 100)
    
    assert tracker.count_total() == 150

def test_choose_food_calculation():
    tracker = Products()
    
    tracker.products = [
        {"product_name": "Test Cookie", "nutriments": {"energy-kcal_100g": 500}}
    ]
    tracker.size_dict = 1

    tracker.choose_food(1, 50)

    assert tracker.select[0]["Name"] == "Test Cookie"
    assert tracker.select[0]["Calories"] == 250.0

def test_show_table_empty():
    tracker = Products()
    assert tracker.show_table() == "There is no products"

def test_choose_food_invalid_index():
    tracker = Products()
    tracker.products = []
    tracker.size_dict = 0
    
    with pytest.raises(IndexError):
        tracker.choose_food(5, 100)