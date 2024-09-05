class Food(object):
    def __init__(self, name = "", price = "", ):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        new_name = self.name
        
    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        if new_price >= 0:           #Enforce non-negative price
            self.price = new_price
        else: 
            print("Error: Price cannot be negative.")


class Meal(Food):
    def __init__(self, name="", price="", side_order = ""):
        super().__init__(name, price)
        self.side_order = side_order

    def get_side_order(self):
        return self.side_order
    
    def set_side_order(self, new_side_order):
        self.side_order = new_side_order

#asks what the user wants as a side order
    def ask_side_order(self):
        print("Would you like any side orders?")
        available_sides = ["nuggets", "fries", "salad", "onion rings"]  # More options
        choice = input("Please enter your side order(s) from the following (separate with commas):\n" + ", ".join(available_sides) + " ").lower()

        # Handle multiple side orders (comma-separated)
        side_orders = choice.split(",")
        cleaned_sides = [side.strip() for side in side_orders if side.strip() in available_sides]

        if cleaned_sides:
            self.side_order = ", ".join(cleaned_sides)
            print(f"You chose {self.side_order} as your side orders.")
        else:
            print("You did not choose any side orders.")

#class Dessert(Food):

#class Drinks(Object):


# Example usage with enhanced functionality:
if __name__ == '__main__':
    m1 = Meal("Chicken Sandwich", 12.50)
    m1.ask_side_order()  # Ask for side orders dynamically
    print("\nMeal 1's info:")
    print(f"Name: {m1.get_name()}")
    print(f"Price: ${m1.get_price():.2f}")  # Format price with 2 decimal places
    print(f"Side Order(s): {m1.get_side_order()}")

    m2 = Meal("Deluxe Pizza", 18.99, "fries")
    print("\nMeal 2's info:")
    print(m2)  # Default string representation (name and price)

    m3 = Meal()  # Create an empty Meal object
    m3.set_name("Custom Burger")
    m3.set_price(15.00)
    m3.ask_side_order()
    print("\nMeal 3's info:")
    print(m3.name)  # Access attributes directly for flexibility
    print(f"Price: ${m3.price:.2f}")
    print(f"Side Order(s): {m3.side_order}")