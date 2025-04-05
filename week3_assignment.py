def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Apply discount only if it is 20% or higher.
    """
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        return price - discount
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied! Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
