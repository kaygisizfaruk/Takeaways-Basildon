takeaways = {
    "chicken": [{"name": "Smokies Grill", "rating": 3.4, "price": 2/5}],
    "chicken": [{"name": "Slim Chickens", "rating": 3.2, "price": 3/5}],
    "chicken": [{"name": "Pepe's Piri Piri", "rating": 3.9, "price": 5/5}],
    "chicken": [{"name": "Burger King", "rating": 3.5, "price": 4/5}],
    "chicken": [{"name": "British Fried Chicken", "rating": 3.9, "price": 3/5}],
    "chicken": [{"name": "Munchy Chicken", "rating": 3.6, "price": 2/5}],
    "chicken": [{"name": "Bird Box", "rating": 4.0, "price": 5/5}],
    "chicken": [{"name": "Favourite Chicken", "rating": 4.4, "price": 5/5}],
    "burgers": [{"name": "Mega Grill", "rating": 2.3, "price": 1/5}],
    "burgers": [{"name": "Munchy Chicken", "rating": 3.6, "price": 2/5}],
    "burgers": [{"name": "McDonalds", "rating": 2.7, "price": 5/5}],
    "burgers": [{"name": "Cosmos Basildon", "rating": 3.6, "price": 3/5}],
    "burgers": [{"name": "Kings Flavour", "rating": 3.9, "price": 3/5}],
    "burgers": [{"name": "Peri Peri Original", "rating": 4.2, "price": 3/5}],
    "burgers": [{"name": "Five Guys", "rating": 4.0, "price": 3/5}],
    "pizza": [{"name": "Farm Pizza", "rating": 4.3, "price": 5/5}],
    "pizza": [{"name": "New Capital", "rating": 3.7, "price": 4/5}],
    "pizza": [{"name": "Pizza Express", "rating": 3.3, "price": 5/5}],
    "pizza": [{"name": "Pizza GoGo", "rating": 3.8, "price": 4/5}],
    "pizza": [{"name": "Up The Road", "rating": 3.7, "price": 3/5}],
    "pizza": [{"name": "Queens Pizza", "rating": 4.1, "price": 4/5}],
    "kebab": [{"name": "Kingswood Kebab", "rating": 4.6, "price": 4/5}],
    "kebab": [{"name": "Basildon Kitchen", "rating": 4.4, "price": 5/5}],
    "kebab": [{"name": "Pitsea Kebab", "rating": 4.4, "price": 3/5}],
    "kebab": [{"name": "Essex BBQ", "rating": 4.7, "price": 4/5}],
    "asian": [{"name": "Zaika Indian", "rating": 4.7, "price": 5/5}],
    "asian": [{"name": "Canton House", "rating": 4.3, "price": 2/5}],
    "asian": [{"name": "CurryOn", "rating": 3.5, "price": 4/5}],
    "asian": [{"name": "Hot Wok", "rating": 3.2, "price": 1/5}],
    "american": [{"name": "Papa Johns", "rating": 4.3, "price": 5/5}],
    "american": [{"name": "KFC", "rating": 3.7, "price": 4/5}],
    "american": [{"name": "Subway", "rating": 3.6, "price": 3/5}],
    "american": [{"name": "Dominos", "rating": 3.9, "price": 5/5}],
    "american": [{"name": "Burger King", "rating": 3.5, "price": 4/5}],
    "american": [{"name": "Pizza Hut", "rating": 4.0, "price": 3/5}],
    "desserts": [{"name": "Dessert Island", "rating": 4.3, "price": 5/5}],
    "desserts": [{"name": "Creams", "rating": 3.7, "price": 4/5}],
    "desserts": [{"name": "Kaspas", "rating": 3.6, "price": 3/5}],
    "desserts": [{"name": "Sundaes", "rating": 3.9, "price": 5/5}],
    "desserts": [{"name": "Gelato", "rating": 3.5, "price": 4/5}],
    "desserts": [{"name": "Shakeaway", "rating": 4.0, "price": 3/5}],
    "breakfast": [{"name": "McDonalds", "rating": 2.7, "price": 5/5}],
    "breakfast": [{"name": "Greggs", "rating": 3.2, "price": 4/5}],
    "breakfast": [{"name": "Subway", "rating": 3.6, "price": 3/5}],
    "breakfast": [{"name": "Costa", "rating": 3.9, "price": 5/5}],
    "breakfast": [{"name": "Starbucks", "rating": 3.5, "price": 4/5}],
    "breakfast": [{"name": "Cafe Nero", "rating": 4.0, "price": 3/5}],
    "fish": [{"name": "Fish & Chips", "rating": 4.3, "price": 5/5}],
    "fish": [{"name": "Fish House", "rating": 3.7, "price": 4/5}],
    "fish": [{"name": "Fish Inn", "rating": 3.6, "price": 3/5}],
    "fish": [{"name": "Atwal's Chippy", "rating": 3.9, "price": 5/5}],
    "fish": [{"name": "Station Chippy", "rating": 3.5, "price": 4/5}],
    "japanese": [{"name": "Sushi City", "rating": 4.0, "price": 3/5}],
    "japanese": [{"name": "Yokoso", "rating": 3.5, "price": 4/5}],
    "japanese": [{"name": "Sushi House", "rating": 3.6, "price": 3/5}],
    "japanese": [{"name": "Sushi Box", "rating": 3.9, "price": 5/5}],
    "japanese": [{"name": "Sushi Inn", "rating": 3.5, "price": 4/5}],
    "groceries": [{"name": "Tesco", "rating": 3.7, "price": 4/5}],
    "groceries": [{"name": "Asda", "rating": 3.6, "price": 3/5}],
    "groceries": [{"name": "Sainsburys", "rating": 3.9, "price": 5/5}],
    "groceries": [{"name": "Lidl", "rating": 3.5, "price": 4/5}],
    "groceries": [{"name": "Aldi", "rating": 4.0, "price": 3/5}]
}

def merge_sort(data, key):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid], key)
    right = merge_sort(data[mid:], key)
    
    return merge(left, right, key)

def merge(left, right, key):
    sorted_list = []
    while left and right:
        if left[0][key] > right[0][key]:  # Sort in descending order
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    
    sorted_list.extend(left if left else right)
    return sorted_list

def recommend_takeaways(food_type, takeaways):
    if food_type in takeaways:
        sorted_list = merge_sort(takeaways[food_type], "rating")
        return sorted_list
    else:
        return []

def main():
    print("Welcome to the Basildon Takeaway Recommendation System!")
    print("Available food types:")
    for food_type in takeaways.keys():
        print(f"- {food_type.capitalize()}")

    food_type = input("\nPlease enter the type of food you're looking for: ").lower()

    recommendations = recommend_takeaways(food_type, takeaways)

    if recommendations:
        print(f"\nRecommended {food_type} takeaways:")
        for idx, takeaway in enumerate(recommendations, 1):
            print(f"{idx}. {takeaway['name']} - Rating: {takeaway['rating']} - Price: {takeaway['Price']}")
    else:
        print(f"\nSorry, no takeaways found for '{food_type}'. Please try another food type.")

main()
