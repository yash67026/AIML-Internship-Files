# Create an empty shopping cart
cart = []

# Add items to the cart
cart.append("Milk")
cart.append("Bread")
cart.append("Eggs")
cart.append("Rice")

print("Shopping Cart:", cart)

# Remove one item
cart.remove("Bread")

print("\nAfter removing one item:")
print("Shopping Cart:", cart)

# Print total number of items
print("\nTotal items in cart:", len(cart))
