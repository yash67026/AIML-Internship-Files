cart = list(input("Enter items separated by space: ").split())
print("\nShopping Cart:", cart)


remove_item = input("Enter item to remove: ")
cart.remove(remove_item)

print("\nAfter removing one item:")
print("Shopping Cart:", cart)

print("\nTotal items in cart:", len(cart))
