
class GroceryStore:
    def __init__(self, filename="grocery_data.txt"):
        self.filename = filename
        self.products = {}
        self.load_data()

    def load_data(self):
        try:
            file = open(self.filename, "r")
            for line in file:
                line = line.strip()
                if line:
                    name, price, quantity = line.split(",")
                    self.products[name] = {
                        "price": float(price),
                        "quantity": int(quantity)
                    }
            file.close()
        except FileNotFoundError:
            self.products = {}

    
    def save_data(self):
        try:
            file = open(self.filename, "w")
            for name, info in self.products.items():
                file.write(f"{name},{info['price']},{info['quantity']}\n")
            file.close()
        except Exception as e:
            print("Error saving data:", e)

    # Add product
    def add_product(self):
        try:
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the product quantity: "))

            self.products[name] = {"price": price, "quantity": quantity}
            self.save_data()
            print("Product added successfully!\n")

        except ValueError:
            print("Invalid input!\n")

    # View product
    def view_products(self):
        if not self.products:
            print("No products found!\n")
            return

        print("\n--- Product List ---")
        for name, info in self.products.items():
            print(f"Name: {name}, Price: {info['price']}, Quantity: {info['quantity']}")
        print()

    # Update product
    def update_product(self):
        name = input("Enter product name to update: ")

        if name in self.products:
            try:
                price = float(input("Enter the new price: "))
                quantity = int(input("Enter the new quantity: "))

                self.products[name]["price"] = price
                self.products[name]["quantity"] = quantity
                self.save_data()

                print("Product updated successfully!\n")

            except ValueError:
                print("Invalid input!\n")
        else:
            print("Product not found!\n")

    
    def delete_product(self):
        name = input("Enter product name to delete: ")

        if name in self.products:
            del self.products[name]
            self.save_data()
            print("Product deleted successfully!\n")
        else:
            print("Product not found!\n")

    def run(self):
        while True:
            print("""
 Grocery Management System 
-------------- --------------
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Exit
""")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_products()
            elif choice == "3":
                self.update_product()
            elif choice == "4":
                self.delete_product()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!\n")

if __name__ == "__main__":
    store = GroceryStore()
    store.run()
