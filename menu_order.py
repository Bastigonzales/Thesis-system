# Menu Concession

menu = {
    "Tonyo's Speical Lugaw": 3.00,
    "Longsilog": 129.00,
    "Tapsilog": 129.00,
    "Tocilog": 129.00,
    "Pansit bihon (Regular)": 189.00,
    "Lumpiang Shanghai (20pcs)": 269.00,
    "Coke Can": 75.05,
    "Iced tea": 80.00,
    "Halo-Halo": 120.00
}

cart = []
total = 0

# Generate a numbered menu
numbered_menu = {str(index): (item, price) for index, (item, price) in enumerate(menu.items(), start=1)}

# Display the numbered menu
print("--------- Menu ---------")
for num, (item, price) in numbered_menu.items():
    print(f"{num}. {item} - ₱{price:.2f}")

# Function to add items to the cart
def add_to_cart():
    global total
    while True:
        choice = input("Enter the numbers of the items to add to your cart (comma-separated, or type 'done' to finish): ")
        if choice.lower() == "done":
            break
        # Split input by commas, strip spaces, and process each number
        choices = [ch.strip() for ch in choice.split(",")]
        for ch in choices:
            if ch in numbered_menu:
                item, price = numbered_menu[ch]
                cart.append(item)
                total += price
                print(f"Added {item} to your cart. Current total: ₱{total:.2f}")
            else:
                print(f"Invalid choice: {ch}. Please select a valid menu number.")

# Start the ordering process
add_to_cart()

# Display the final cart and total
print("\nYour Cart:")
for item in cart:
    print(f"- {item}")
print(f"Total: ₱{total:.2f}")
