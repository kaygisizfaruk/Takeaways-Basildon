takeaways = {
    "chicken": [
        {"name": "Smokies Grill", "rating": 3.4, "price": 2/5},
        {"name": "Slim Chickens", "rating": 3.2, "price": 3/5},
        {"name": "Pepe's Piri Piri", "rating": 3.9, "price": 5/5},
        {"name": "Burger King", "rating": 3.5, "price": 4/5},
        {"name": "British Fried Chicken", "rating": 3.9, "price": 3/5},
        {"name": "Munchy Chicken", "rating": 3.6, "price": 2/5},
        {"name": "Bird Box", "rating": 4.0, "price": 5/5},
        {"name": "Favourite Chicken", "rating": 4.4, "price": 5/5}
    ],
    "burgers": [
        {"name": "Mega Grill", "rating": 2.3, "price": 1/5},
        {"name": "Munchy Chicken", "rating": 3.6, "price": 2/5},
        {"name": "McDonalds", "rating": 2.7, "price": 5/5},
        {"name": "Cosmos Basildon", "rating": 3.6, "price": 3/5},
        {"name": "Kings Flavour", "rating": 3.9, "price": 3/5},
        {"name": "Peri Peri Original", "rating": 4.2, "price": 3/5},
        {"name": "Five Guys", "rating": 4.0, "price": 3/5}
    ],
    "pizza": [
        {"name": "Farm Pizza", "rating": 4.3, "price": 5/5},
        {"name": "New Capital", "rating": 3.7, "price": 4/5},
        {"name": "Pizza Express", "rating": 3.3, "price": 5/5},
        {"name": "Pizza GoGo", "rating": 3.8, "price": 4/5},
        {"name": "Up The Road", "rating": 3.7, "price": 3/5},
        {"name": "Queens Pizza", "rating": 4.1, "price": 4/5}
    ],
    "kebab": [
        {"name": "Kingswood Kebab", "rating": 4.6, "price": 4/5},
        {"name": "Basildon Kitchen", "rating": 4.4, "price": 5/5},
        {"name": "Pitsea Kebab", "rating": 4.4, "price": 3/5},
        {"name": "Essex BBQ", "rating": 4.7, "price": 4/5}
    ],
    "asian": [
        {"name": "Zaika Indian", "rating": 4.7, "price": 5/5},
        {"name": "Canton House", "rating": 4.3, "price": 2/5}
    ]
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

def autocomplete(query, takeaways):
    query = query.lower()
    suggestions = [food_type for food_type in takeaways if food_type.startswith(query)]
    return suggestions

def main():
    print("Welcome to the Basildon Takeaway Recommendation System!")
    print("Available food types:")
    for food_type in takeaways.keys():
        print(f"- {food_type.capitalize()}")

    while True:
        query = input("\nStart typing the type of food you're looking for (or press Enter to see all options): ").lower()
        if query == "":
            print("Available food types:")
            for food_type in takeaways.keys():
                print(f"- {food_type.capitalize()}")
            continue

        suggestions = autocomplete(query, takeaways)
        print(f"DEBUG: suggestions = {suggestions}")  # Debug print
        if suggestions:
            print("Did you mean:")
            for suggestion in suggestions:
                print(f"- {suggestion.capitalize()}")
        else:
            print(f"No suggestions found for '{query}'.")

        food_type = input("\nPlease enter the type of food you're looking for: ").lower()
        recommendations = recommend_takeaways(food_type, takeaways)
        print(f"DEBUG: recommendations = {recommendations}")  # Debug print

        if recommendations:
            print(f"\nRecommended {food_type} takeaways:")
            for idx, takeaway in enumerate(recommendations, 1):
                print(f"{idx}. {takeaway['name']} - Rating: {takeaway['rating']} - Price: {takeaway['price']}")
        else:
            print(f"\nSorry, no takeaways found for '{food_type}'. Please try another food type.")


main()
