import customtkinter as ctk

# Menu Concession
menu = {
    "Tonyo's Special Lugaw": 3.00,
    "Longsilog": 129.00,
    "Tapsilog": 129.00,
    "Tocilog": 129.00,
    "Pansit bihon (Regular)": 189.00,
    "Lumpiang Shanghai (20pcs)": 269.00,
    "Coke Can": 75.05,
    "Iced tea": 80.00,
    "Halo-Halo": 120.00,
}

# Initialize cart and total
cart = []
total = 0

# CustomTkinter application
class MenuApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Menu Concession")
        self.geometry("900x600")

        # Frame for the menu and buttons
        self.menu_frame = ctk.CTkFrame(self, width=400)
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Label for the menu
        self.menu_label = ctk.CTkLabel(self.menu_frame, text="Menu", font=ctk.CTkFont(size=16, weight="bold"))
        self.menu_label.pack(pady=10)

        # Generate individual buttons for menu items
        self.numbered_menu = {str(index): (item, price) for index, (item, price) in enumerate(menu.items(), start=1)}
        for num, (item, price) in self.numbered_menu.items():
            # Create a separate button for each menu item
            item_button = ctk.CTkButton(
                self.menu_frame,
                text=f"{num}. {item} - ₱{price:.2f}",
                command=lambda i=item, p=price: self.add_to_cart(i, p),
            )
            item_button.pack(pady=5, fill="x")

        # Frame for the cart and total
        self.cart_frame = ctk.CTkFrame(self, width=400)
        self.cart_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Label for the cart
        self.cart_label = ctk.CTkLabel(self.cart_frame, text="Cart", font=ctk.CTkFont(size=16, weight="bold"))
        self.cart_label.pack(pady=10)

        # Textbox for the cart
        self.cart_box = ctk.CTkTextbox(self.cart_frame, height=300, width=300)
        self.cart_box.pack(pady=10)

        # Label for the total
        self.total_label = ctk.CTkLabel(self.cart_frame, text="Total: ₱0.00", font=ctk.CTkFont(size=14))
        self.total_label.pack(pady=10)

        # Add Clear Cart button
        self.clear_button = ctk.CTkButton(
            self.cart_frame, text="Clear Cart", command=self.clear_cart, fg_color="red"
        )
        self.clear_button.pack(pady=10)

    def add_to_cart(self, item, price):
        """Add items to the cart and update the total."""
        global total
        cart.append(item)
        total += price

        # Update the cart display
        self.cart_box.insert("end", f"{item}\n")
        self.cart_box.see("end")

        # Update the total
        self.total_label.configure(text=f"Total: ₱{total:.2f}")

    def clear_cart(self):
        """Clear the cart and reset the total."""
        global total
        cart.clear()
        total = 0

        # Clear the cart display and reset the total label
        self.cart_box.delete("1.0", "end")
        self.total_label.configure(text="Total: ₱0.00")

# Run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = MenuApp()
    app.mainloop()
